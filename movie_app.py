class MovieApp:
    def __init__(self, storage):
        """docstring"""
        self._storage = storage


    def _command_list_movies(self):
        """docstring"""
        movies = self._storage.list_movies()
        pass

    def _command_movie_stats(self):
        """docstring"""
        pass

    ...

    def _generate_website(self):
        """docstring"""
        pass

    def run(self):
        """docstring"""
      # Print menu
      # Get use command
      # Execute command