# 🎬 Movie Project

A Python-based application designed to manage and store movie information, offering functionalities to add, view, and persist movie data using JSON or CSV formats.

## 📁 Project Structure

- `main.py` – Entry point of the application.
- `movie_app.py` – Contains the core logic for managing movies.
- `istorage.py` – Defines the storage interface for different storage mechanisms.
- `storage_json.py` – Implements JSON-based storage adhering to the storage interface.
- `storage_csv.py` – Implements CSV-based storage adhering to the storage interface.
- `data.json` – Sample JSON file containing movie data.
- `_static/` – Directory for static assets (if any).
- `.idea/` – Project configuration files for IDEs like PyCharm.
- `__pycache__/` – Directory containing compiled Python files.

## 🚀 Features

- **Add Movies**: Input movie details to add to the collection.
- **View Movies**: Display a list of all stored movies.
- **Persistent Storage**: Save and retrieve movie data using JSON or CSV formats.
- **Modular Design**: Easily switch between different storage mechanisms.
