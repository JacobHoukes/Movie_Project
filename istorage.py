from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def get_movies(self):
        """This function retrieves all stored movies as a dictionary."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """This function adds a new movie with title, release year, rating, and poster URL."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """This function deletes a movie by its title."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """This function updates the rating of a movie by its title."""
        pass