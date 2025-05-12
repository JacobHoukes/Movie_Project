from colorama import Fore, init
import random
import movie_storage

init(autoreset=True)


# Functions executing menu item actions

def list_movies():
    """This function displays all movie titles, ratings, and years in green."""
    movies = movie_storage.get_movies()
    print(Fore.GREEN + f"{len(movies)} movies in total")
    for name, details in movies.items():
        print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")


def add_movie():
    """This function prompts user to input a movie name, rating, and year, then adds it to the JSON file."""
    movies = movie_storage.get_movies()

    while True:
        movie_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to add: ").strip()
        if not movie_name:
            print(Fore.RED + "Movie name cannot be empty.")
        elif movie_name in movies:
            print(Fore.YELLOW + f"{movie_name} already exists in the database.")
            return
        else:
            break

    while True:
        try:
            movie_rating = float(input(Fore.YELLOW + "Please enter a rating (1-10): "))
            if 1 <= movie_rating <= 10:
                break
            else:
                print(Fore.RED + "Rating must be between 1 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    while True:
        try:
            movie_year = int(input(Fore.YELLOW + "Please enter the year of release: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid year. Please enter a valid year (e.g. 1994).")

    movie_storage.add_movie(movie_name, movie_year, movie_rating)
    print(Fore.GREEN + f"{movie_name} added successfully.")


def delete_movie():
    """This function removes a movie from the JSON file if it exists."""
    movie_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to remove: ").strip()
    if not movie_name:
        print(Fore.RED + "Movie name cannot be empty.")
        return

    movies = movie_storage.get_movies()
    if movie_name in movies:
        movie_storage.delete_movie(movie_name)
        print(Fore.GREEN + f"{movie_name} deleted successfully.")
    else:
        print(Fore.YELLOW + "The movie is not in the database.")


def update_movie():
    """This function updates the rating of an existing movie."""
    movie_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to update: ").strip()
    movies = movie_storage.get_movies()

    if movie_name not in movies:
        print(Fore.YELLOW + "The movie is not in the database.")
        return

    while True:
        try:
            new_rating = float(input(Fore.YELLOW + "Please enter a new rating (1-10): "))
            if 1 <= new_rating <= 10:
                break
            else:
                print(Fore.RED + "Rating must be between 1 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    movie_storage.update_movie(movie_name, new_rating)
    print(Fore.GREEN + f"{movie_name} updated successfully.")


def get_stats():
    """This function displays average, median, best, and worst movie ratings."""
    movies = movie_storage.get_movies()
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

    best_movies = [name for name, details in movies.items() if details["rating"] == max_rating]
    worst_movies = [name for name, details in movies.items() if details["rating"] == min_rating]

    print(Fore.GREEN + f"Average rating: {avg}")
    print(Fore.GREEN + f"Median rating: {median}")
    print(Fore.GREEN + "Best rated movie(s):")
    for movie in best_movies:
        print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")
    print(Fore.GREEN + "Worst rated movie(s):")
    for movie in worst_movies:
        print(Fore.BLUE + f"{movie}: {movies[movie]['rating']}")


def get_random_movie():
    """This function prints a randomly selected movie and its rating."""
    movies = movie_storage.get_movies()
    if not movies:
        print(Fore.YELLOW + "No movies in the database.")
        return
    name, details = random.choice(list(movies.items()))
    print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")


def search_movie():
    """This function searches for a movie by name and displays its rating and year if found."""
    query = input(Fore.YELLOW + "What movie are you looking for?: ")
    movies = movie_storage.get_movies()
    found = False
    for name, details in movies.items():
        if query.lower() in name.lower():
            print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")
            found = True
    if not found:
        print(Fore.YELLOW + "The movie is not in the database.")


def get_sorted_list_by_rtg():
    """This function displays movies sorted by rating in descending order."""
    movies = movie_storage.get_movies()
    sorted_by_rating = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
    print(Fore.GREEN + "Movies sorted by rating:")
    for name, details in sorted_by_rating:
        print(Fore.BLUE + f"{name} ({details['year']}): {details['rating']}")


# This is the main function

def main():
    """This is the main function that runs the movie database app."""
    show_app_name()
    while True:
        show_menu()
        if not user_input():
            break
        enter_to_continue()


def show_app_name():
    """This function displays the movie database's name."""
    print(Fore.BLUE + "\n********** My Movies Database **********\n")


def show_menu():
    """This function displays the menu items."""
    print(Fore.GREEN + "Menu:")
    print(Fore.GREEN + "0. Exit")
    print(Fore.GREEN + "1. List movies")
    print(Fore.GREEN + "2. Add movie")
    print(Fore.GREEN + "3. Delete movie")
    print(Fore.GREEN + "4. Update movie")
    print(Fore.GREEN + "5. Stats")
    print(Fore.GREEN + "6. Random movie")
    print(Fore.GREEN + "7. Search movie")
    print(Fore.GREEN + "8. Movies sorted by rating\n")


def enter_to_continue():
    """This function asks the user to hit enter to proceed with the program"""
    input(Fore.YELLOW + "\nPress enter to continue \n")


def user_input():
    """This function asks for user input (number(0-8)) and calls functions depending on that input."""
    choice = input(Fore.YELLOW + "Enter choice (0-8): ")
    print("")
    if choice == "0":
        print(Fore.GREEN + "Bye!")
        return False
    elif choice == "1":
        list_movies()
    elif choice == "2":
        add_movie()
    elif choice == "3":
        delete_movie()
    elif choice == "4":
        update_movie()
    elif choice == "5":
        get_stats()
    elif choice == "6":
        get_random_movie()
    elif choice == "7":
        search_movie()
    elif choice == "8":
        get_sorted_list_by_rtg()
    else:
        print(Fore.YELLOW + "Please provide your choice in the form of a number (0-8).")
    return True


if __name__ == "__main__":
    main()
