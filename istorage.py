from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """This function displays all movie titles and ratings."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """This function prompts user to input a movie name and rating, then adds it to the dictionary."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """This function removes a movie from the dictionary if it exists."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """This function updates the rating of an existing movie."""
        pass
