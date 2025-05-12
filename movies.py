from colorama import Fore, init
import random

init(autoreset=True)


class MovieApp:
    def __init__(self, storage):
        """This method initializes MovieApp with a storage backend."""
        self._storage = storage

    def _command_list_movies(self):
        """This method lists all movies in the database."""
        movies = self._storage.get_movies()
        print(Fore.GREEN + f"{len(movies)} movies in total")
        for name, details in movies.items():
            print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def _command_add_movie(self):
        """This method adds a new movie to the database."""
        movies = self._storage.get_movies()

        while True:
            name = input(Fore.YELLOW + "Enter movie name: ").strip()
            if not name:
                print(Fore.RED + "Movie name cannot be empty.")
            elif name in movies:
                print(Fore.YELLOW + f"{name} already exists.")
                return
            else:
                break

        while True:
            try:
                rating = float(input(Fore.YELLOW + "Enter rating (1-10): "))
                if 1 <= rating <= 10:
                    break
                else:
                    print(Fore.RED + "Rating must be between 1 and 10.")
            except ValueError:
                print(Fore.RED + "Invalid input. Enter a number.")

        while True:
            try:
                year = int(input(Fore.YELLOW + "Enter release year: "))
                break
            except ValueError:
                print(Fore.RED + "Invalid input. Enter a valid year.")

        self._storage.add_movie(name, year, rating)
        print(Fore.GREEN + f"{name} added successfully.")

    def _command_delete_movie(self):
        """This method deletes a movie from the database."""
        name = input(Fore.YELLOW + "Enter movie name to delete: ").strip()
        movies = self._storage.get_movies()

        if name in movies:
            self._storage.delete_movie(name)
            print(Fore.GREEN + f"{name} deleted.")
        else:
            print(Fore.YELLOW + "Movie not found.")

    def _command_update_movie(self):
        """This method updates an existing movie's rating."""
        name = input(Fore.YELLOW + "Enter movie name to update: ").strip()
        movies = self._storage.get_movies()

        if name not in movies:
            print(Fore.YELLOW + "Movie not found.")
            return

        while True:
            try:
                new_rating = float(input(Fore.YELLOW + "Enter new rating (1-10): "))
                if 1 <= new_rating <= 10:
                    break
                else:
                    print(Fore.RED + "Rating must be between 1 and 10.")
            except ValueError:
                print(Fore.RED + "Invalid input. Enter a number.")

        self._storage.update_movie(name, new_rating)
        print(Fore.GREEN + f"{name} updated successfully.")

    def _command_movie_stats(self):
        """This method displays movie rating statistics."""
        movies = self._storage.get_movies()
        ratings = [d["rating"] for d in movies.values()]
        if not ratings:
            print(Fore.YELLOW + "No movies in database.")
            return

        avg = round(sum(ratings) / len(ratings), 1)
        sorted_ratings = sorted(ratings)
        n = len(ratings)
        median = sorted_ratings[n // 2] if n % 2 else round((sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2,
                                                            1)
        max_rating = max(ratings)
        min_rating = min(ratings)

        best = [name for name, d in movies.items() if d["rating"] == max_rating]
        worst = [name for name, d in movies.items() if d["rating"] == min_rating]

        print(Fore.GREEN + f"Average rating: {avg}")
        print(Fore.GREEN + f"Median rating: {median}")
        print(Fore.GREEN + "Best rated movie(s):")
        for m in best:
            print(Fore.BLUE + f"{m}: {movies[m]['rating']}")
        print(Fore.GREEN + "Worst rated movie(s):")
        for m in worst:
            print(Fore.BLUE + f"{m}: {movies[m]['rating']}")

    def _command_random_movie(self):
        """This method displays a randomly selected movie."""
        movies = self._storage.get_movies()
        if not movies:
            print(Fore.YELLOW + "No movies available.")
            return
        name, details = random.choice(list(movies.items()))
        print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def _command_search_movie(self):
        """This method searches for movies by name."""
        query = input(Fore.YELLOW + "Enter movie name to search: ")
        movies = self._storage.get_movies()
        found = False
        for name, d in movies.items():
            if query.lower() in name.lower():
                print(Fore.BLUE + f"{name} ({d['year']}): {d['rating']}")
                found = True
        if not found:
            print(Fore.YELLOW + "No matches found.")

    def _command_sorted_by_rating(self):
        """This method displays movies sorted by rating descending."""
        movies = self._storage.get_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        print(Fore.GREEN + "Movies sorted by rating:")
        for name, d in sorted_movies:
            print(Fore.BLUE + f"{name} ({d['year']}): {d['rating']}")

    def _generate_website(self):
        """This method is a placeholder for website generation logic."""
        print(Fore.YELLOW + "Website generation not yet implemented.")

    def run(self):
        """This method is the main program loop."""
        print(Fore.BLUE + "\n********** My Movies Database **********\n")
        options = {
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_movie_stats,
            "6": self._command_random_movie,
            "7": self._command_search_movie,
            "8": self._command_sorted_by_rating,
            "9": self._generate_website,
            "0": lambda: print(Fore.GREEN + "Bye!")
        }

        while True:
            print(Fore.GREEN + "\nMenu:")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Show stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Sort by rating")
            print("9. Generate website")

            choice = input(Fore.YELLOW + "\nEnter your choice (0-9): ").strip()
            action = options.get(choice)
            if action:
                action()
                if choice == "0":
                    break
            else:
                print(Fore.RED + "Invalid choice. Please enter a number between 0 and 9.")
            input(Fore.YELLOW + "\nPress Enter to continue...")
