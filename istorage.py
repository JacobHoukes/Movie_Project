from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """This method retrieves all stored movies as a dictionary."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """This method adds a new movie with title, release year, rating, and poster URL."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """This method deletes a movie by its title."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """This method updates the rating of a movie by its title."""
        pass