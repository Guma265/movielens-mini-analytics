import sqlite3
from pathlib import Path
import pandas as pd
import os

ROOT = Path(os.getcwd())
CLEAN = ROOT / "data_clean"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

db_path = ROOT / "movielens.db"
conn = sqlite3.connect(db_path)

ratings = pd.read_csv(CLEAN / "ratings_clean.csv")
movies = pd.read_csv(CLEAN / "movies_clean.csv")

# cargar a sqlite (recrear)
conn.executescript("""
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
  movieId INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  genres TEXT
);

CREATE TABLE ratings (
  userId INTEGER NOT NULL,
  movieId INTEGER NOT NULL,
  rating REAL NOT NULL,
  timestamp INTEGER,
  FOREIGN KEY(movieId) REFERENCES movies(movieId)
);
""")

movies.to_sql("movies", conn, if_exists="append", index=False)
ratings.to_sql("ratings", conn, if_exists="append", index=False)

# Reporte 1: Top 10 películas por número de ratings
q1 = """
SELECT m.title, COUNT(*) AS n_ratings, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
ORDER BY n_ratings DESC
LIMIT 10;
"""
top_movies = pd.read_sql(q1, conn)
top_movies.to_csv(OUT / "top_movies_by_volume.csv", index=False)

# Reporte 2: Películas mejor calificadas (con mínimo 50 ratings)
q2 = """
SELECT m.title, COUNT(*) AS n_ratings, AVG(r.rating) AS avg_rating
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
HAVING COUNT(*) >= 50
ORDER BY avg_rating DESC
LIMIT 10;
"""
best_movies = pd.read_sql(q2, conn)
best_movies.to_csv(OUT / "best_movies_min50.csv", index=False)

print("✅ DB creada:", db_path)
print("✅ Outputs:", OUT)

conn.close()
