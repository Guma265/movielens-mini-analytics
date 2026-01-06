-- 01_reports.sql
-- MovieLens Mini Analytics
-- Reportes en SQL puro (SQLite)

-- 1) Top 10 películas por número de ratings
SELECT
    m.title,
    COUNT(*) AS n_ratings,
    ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings r
JOIN movies m
  ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
ORDER BY n_ratings DESC
LIMIT 10;

-- 2) Películas mejor calificadas (mínimo 3 ratings)
SELECT
    m.title,
    COUNT(*) AS n_ratings,
    ROUND(AVG(r.rating), 2) AS avg_rating
FROM ratings r
JOIN movies m
  ON r.movieId = m.movieId
GROUP BY m.movieId, m.title
HAVING COUNT(*) >= 3
ORDER BY avg_rating DESC
LIMIT 10;

-- 3) Usuarios más activos
SELECT
    userId,
    COUNT(*) AS total_ratings
FROM ratings
GROUP BY userId
ORDER BY total_ratings DESC;
