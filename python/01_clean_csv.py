from pathlib import Path
import pandas as pd
import os

ROOT = Path(os.getcwd())

RAW = ROOT / "data_raw"
CLEAN = ROOT / "data_clean"
CLEAN.mkdir(exist_ok=True)

ratings_path = RAW / "ratings.csv"
movies_path = RAW / "movies.csv"

ratings = pd.read_csv(ratings_path)
movies = pd.read_csv(movies_path)

# --- Limpieza mínima (pero real) ---
# 1) tipos
ratings["userId"] = ratings["userId"].astype("int64")
ratings["movieId"] = ratings["movieId"].astype("int64")
ratings["rating"] = ratings["rating"].astype("float64")

movies["movieId"] = movies["movieId"].astype("int64")
movies["title"] = movies["title"].astype(str)

# 2) validar nulos críticos
assert ratings[["userId","movieId","rating"]].isna().sum().sum() == 0
assert movies[["movieId","title"]].isna().sum().sum() == 0

# 3) deduplicado simple (por si acaso)
ratings = ratings.drop_duplicates(subset=["userId","movieId","timestamp"], keep="first")
movies = movies.drop_duplicates(subset=["movieId"], keep="first")

# 4) guardar limpio
ratings.to_csv(CLEAN / "ratings_clean.csv", index=False)
movies.to_csv(CLEAN / "movies_clean.csv", index=False)

print("✅ Limpieza lista: data_clean/ratings_clean.csv y movies_clean.csv")
