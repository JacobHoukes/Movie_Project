from colorama import Fore, init
import random

init(autoreset=True)


class MovieApp:
    def __init__(self, storage):
        """This method initializes MovieApp with a storage backend."""
        self._storage = storage

    def list_movies(self):
        """This method lists all movies in the database."""
        movies = self._storage.list_movies()
        print(Fore.GREEN + f"{len(movies)} movies in total")
        for name, details in movies.items():
            print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")

    def add_movie(self):
        """This method adds a new movie to the database."""
        movies = self._storage.list_movies()

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

        poster = "N/A"
        self._storage.add_movie(name, year, rating, poster)
        print(Fore.GREEN + f"{name} added successfully.")

    def delete_movie(self):
        """This method deletes a movie from the database."""
        name = input(Fore.YELLOW + "Enter movie name to delete: ").strip()
        movies = self._storage.list_movies()

        if name in movies:
            self._storage.delete_movie(name)
            print(Fore.GREEN + f"{name} deleted.")
        else:
            print(Fore.YELLOW + "Movie not found.")

    def update_movie(self):
        """This method updates an existing movie's rating."""
        name = input(Fore.YELLOW + "Enter movie name to update: ").strip()
        movies = self._storage.list_movies()

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

    def movie_stats(self):
        """This method displays movie rating statistics."""
        movies = self._storage.list_movies()
        ratings = [details["rating"] for details in movies.values()]
        if not ratings:
            print(Fore.YELLOW + "No movies in database.")
            return

        avg = round(sum(ratings) / len(ratings), 1)
        sorted_ratings = sorted(ratings)
        n = len(ratings)
        median = sorted_ratings[n // 2] if n % 2 else round((sorted_ratings[n // 2 - 1] + sorted_ratings[n // 2]) / 2, 1)
        max_rating = max(ratings)
        min_rating = min(ratings)

        best = [name for name, details in movies.items() if details["rating"] == max_rating]
        worst = [name for name, details in movies.items() if details["rating"] == min_rating]

        print(Fore.GREEN + f"Average rating: {avg}")
        print(Fore.GREEN + f"Median rating: {median}")
        print(Fore.GREEN + "Best rated movie(s):")
        for movie in best:
            print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")
        print(Fore.GREEN + "Worst rated movie(s):")
        for movie in worst:
            print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")

    def random_movie(self):
        """This method displays a randomly selected movie."""
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.YELLOW + "No movies available.")
            return
        name, detail = random.choice(list(movies.items()))
        print(Fore.BLUE + f"{name} ({detail['year']}): {detail['rating']}")

    def search_movie(self):
        """This method searches for movies by name."""
        query = input(Fore.YELLOW + "Enter movie name to search: ")
        movies = self._storage.list_movies()
        found = False
        for name, detail in movies.items():
            if query.lower() in name.lower():
                print(Fore.BLUE + f"{name} ({detail['year']}): {detail['rating']}")
                found = True
        if not found:
            print(Fore.YELLOW + "No matches found.")

    def sorted_by_rating(self):
        """This method displays movies sorted by rating descending."""
        movies = self._storage.list_movies()
        sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
        print(Fore.GREEN + "Movies sorted by rating:")
        for name, detail in sorted_movies:
            print(Fore.BLUE + f"{name} ({detail['year']}): {detail['rating']}")

    def generate_website(self):
        """This method is a placeholder for website generation logic."""
        print(Fore.YELLOW + "Website generation not yet implemented.")

    def run(self):
        """This method is the main program loop."""
        print(Fore.BLUE + "\n********** My Movies Database **********\n")

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

            if choice == "0":
                print(Fore.GREEN + "Bye!")
                break
            elif choice == "1":
                self.list_movies()
            elif choice == "2":
                self.add_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                self.update_movie()
            elif choice == "5":
                self.movie_stats()
            elif choice == "6":
                self.random_movie()
            elif choice == "7":
                self.search_movie()
            elif choice == "8":
                self.sorted_by_rating()
            elif choice == "9":
                self.generate_website()
            else:
                print(Fore.RED + "Invalid choice. Please enter a number between 0 and 9.")

            input(Fore.YELLOW + "\nPress Enter to continue...")
