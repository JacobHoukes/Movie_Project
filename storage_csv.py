from istorage import IStorage
import os


class StorageCsv(IStorage):
    def __init__(self, file_path):
        """This method sets the file path and creates an empty file if it doesn't exist."""
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                pass

    def _load_movies(self):
        """This method loads all movies from the file into a dictionary."""
        movies = {}
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    title, year, rating = parts
                    movies[title] = {
                        "year": year,
                        "rating": float(rating)
                    }
        return movies

    def _save_movies(self, movies):
        """This method saves the entire movie dictionary to the file."""
        with open(self.file_path, "w") as file:
            for title, data in movies.items():
                file.write(f"{title},{data['year']},{data['rating']}\n")

    def list_movies(self):
        """This method returns all movies as a dictionary."""
        return self._load_movies()

    def add_movie(self, title, year, rating, poster=None):
        """This method adds a new movie to the collection."""
        movies = self._load_movies()
        movies[title] = {
            "year": year,
            "rating": float(rating)
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """This method deletes a movie by title."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """This method updates the rating of a movie."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = float(rating)
            self._save_movies(movies)
