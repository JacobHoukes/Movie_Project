from .istorage import IStorage
import json
import os


class StorageJson(IStorage):
    def __init__(self, file_path):
        """This method initializes the storage with a given file path."""
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _load_movies(self):
        """This helper method loads and returns the movie data from the JSON file."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_movies(self, movies):
        """This helper method saves the provided movie data to the JSON file."""
        with open(self.file_path, "w") as f:
            json.dump(movies, f, indent=4)

    def list_movies(self):
        """This method returns all stored movies."""
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        """This method prompts user to input a movie name and rating, then adds it to the dictionary."""
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating}
        self._save_movies(movies)

    def delete_movie(self, title):
        """This method removes a movie from the dictionary if it exists."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """This method updates the rating of an existing movie."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
