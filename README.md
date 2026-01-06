🎬 MovieLens Mini Analytics
Mini proyecto de análisis de datos y ETL usando Python, pandas y SQLite, enfocado en transformar datos crudos (CSV) en reportes listos para análisis.
Este proyecto demuestra un pipeline reproducible de principio a fin:
CSV → limpieza → base de datos → consultas → outputs.

Dataset
Dataset sintético tipo MovieLens, compuesto por:
ratings.csv: calificaciones de usuarios a películas
movies.csv: catálogo de películas
Los datos se separan en:
data_raw/: datos originales
data_clean/: datos limpios y validados

Qué demuestra este proyecto
Limpieza y validación de datos con pandas
Control de calidad de datos (nulos, duplicados, tipos)
Carga de datos a SQLite
Análisis mediante SQL y Python
Generación automática de reportes
Estructura clara tipo ETL junior

Estructura del repositorio
movielens-mini-analytics/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data_raw/
│   ├── ratings.csv
│   └── movies.csv
│
├── data_clean/
│   ├── ratings_clean.csv
│   └── movies_clean.csv
│
├── python/
│   ├── 01_clean_csv.py
│   └── 02_load_sqlite_and_reports.py
│
├── sql/
│   └── 01_reports.sql
│
├── outputs/
│   ├── top_movies_by_volume.csv
│   └── best_movies_min50.csv
│
└── movielens.db

Requisitos
Python 3.10+
pandas
Instalación:
pip install -r requirements.txt

Cómo ejecutar el pipeline
Desde la raíz del proyecto:

Limpieza de datos
python python/01_clean_csv.py
Genera:
data_clean/ratings_clean.csv
data_clean/movies_clean.csv

Carga a SQLite y reportes
python python/02_load_sqlite_and_reports.py
Genera:
movielens.db
Reportes en outputs/:
top_movies_by_volume.csv
best_movies_min50.csv

Reportes generados
Top películas por número de ratings
Películas mejor calificadas (con mínimo de ratings)
Consultas equivalentes disponibles en SQL puro (sql/01_reports.sql)

Tecnologías utilizadas
Python
pandas
SQLite
SQL
Git / GitHub

Notas
El dataset es sintético y controlado, creado con fines educativos.
El enfoque del proyecto es demostrar estructura, lógica y buenas prácticas, no volumen de datos.

Autor
Guillermo
Proyecto personal de aprendizaje en análisis e ingeniería de datos.
