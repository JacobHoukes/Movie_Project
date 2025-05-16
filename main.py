from storage_json import StorageJson
from movie_app import MovieApp


def main():
    """This function initializes the movie app with JSON storage and starts the main loop."""
    storage = StorageJson("data.json")
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
