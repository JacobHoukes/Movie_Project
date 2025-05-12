from istorage import IStorage
import json
import os


class StorageJson(IStorage):
    def __init__(self, file_path):
        """This function initializes the storage with a given file path."""
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump({}, f)

    def _load_movies(self):
        """This function loads and returns the movie data from the JSON file."""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save_movies(self, movies):
        """This function saves the provided movie data to the JSON file."""
        with open(self.file_path, "w") as f:
            json.dump(movies, f, indent=4)

    def list_movies(self):
        """This function returns all stored movies."""
        return self._load_movies()  # private helper method _load_movies() includes the try/except

    def add_movie(self, title, year, rating, poster):
        """This function prompts user to input a movie name and rating, then adds it to the dictionary."""
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating}
        self._save_movies(movies)

    def delete_movie(self, title):
        """This function removes a movie from the dictionary if it exists."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """This function updates the rating of an existing movie."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
