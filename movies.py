from colorama import Fore, Back, Style, init
import random

init(autoreset=True)

movies = {
    "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
    "Pulp Fiction": {"rating": 8.8, "year": 1994},
    "The Room": {"rating": 3.6, "year": 2003},
    "The Godfather": {"rating": 9.2, "year": 1972},
    "The Godfather: Part II": {"rating": 9.0, "year": 1974},
    "The Dark Knight": {"rating": 9.0, "year": 2008},
    "12 Angry Men": {"rating": 8.9, "year": 1957},
    "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
    "Forrest Gump": {"rating": 8.8, "year": 1994},
    "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
}


# Functions executing menu item actions


def list_movies():
    """This function displays all movie titles and ratings in green."""
    print(Fore.GREEN + f"{len(movies)} movies in total")
    for name, info in movies.items():
        print(Fore.BLUE + f"{name} ({info['year']}): {info['rating']}")


def add_movie():
    """This function prompts user to input a movie name and rating, then adds it to the dictionary."""
    movie_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to add: ")
    movie_rating = input(Fore.YELLOW + "Please enter a rating (a number between 1-10): ")
    movie_year = input(Fore.YELLOW + "Please enter the year of release: ")
    movies[movie_name] = {"rating": float(movie_rating), "year": int(movie_year)}



def delete_movie():
    """This function removes a movie from the dictionary if it exists."""
    provided_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to remove: ")
    is_found, movie_key = find_db_movie(provided_name)
    if is_found:
        del movies[movie_key]


def update_movie():
    """This function updates the rating of an existing movie."""
    provided_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to update: ")
    is_found, movie_key = find_db_movie(provided_name)
    if is_found:
        new_rating = input(Fore.YELLOW + "Please enter a new rating: ")
        movies[movie_key]["rating"] = float(new_rating)


def get_stats():
    """This function displays average, median, best, and worst movie ratings."""
    average_rating = get_average_rating()
    median_rating = get_median_rating()
    best_movie = get_best_movie()
    worst_movie = get_worst_movie()
    print(average_rating)
    print(median_rating)
    print(best_movie)
    print(worst_movie)


def get_random_movie():
    """This function prints a randomly selected movie and its rating."""
    name, rating = random.choice(list(movies.items()))
    print(Fore.BLUE + f"{name}: {rating}")


def search_movie():
    """This function searches for a movie by name and displays its rating if found."""
    query = input(Fore.YELLOW + "What movie are you looking for?: ")
    found = False
    for name, info in movies.items():
        if query.lower() in name.lower():
            print(Fore.BLUE + f"{name} ({info['year']}): {info['rating']}")
            found = True
    if not found:
        print(Fore.YELLOW + "The movie is not in the database.")


def get_sorted_list_by_rtg():
    """This function displays movies sorted by rating in descending order."""
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
    print(Fore.GREEN + "Movies sorted by rating:")
    for name, info in sorted_movies:
        print(Fore.BLUE + f"{name} ({info['year']}): {info['rating']}")


# Functions for general actions, such as finding a movie in the dictionary, etc.


def find_db_movie(query):
    """This function takes a query and searches the movies dictionary for it.
        It outputs a boolean (either True or False)
        and either the found movie name as a string, or an empty string."""
    for movie_key in movies.keys():
        if query.lower() == movie_key.lower():
            return True, movie_key
    else:
        print(Fore.YELLOW + "The movie is not in the database.")
        return False, ""


def get_average_rating():
    """This function sums up all ratings included in the movies dictionary
        and divides that sum by the amount of ratings in the dictionary, rounded to one decimal place."""
    ratings = [info["rating"] for info in movies.values()]
    avg = round(sum(ratings) / len(ratings), 1)
    return Fore.GREEN + f"The average rating of all movie ratings in the database is {avg}"


def get_median_rating():
    """This function returns the median movie rating."""
    ratings = sorted([info["rating"] for info in movies.values()])
    n = len(ratings)
    if n % 2 != 0:
        return Fore.GREEN + f"The median rating is {ratings[n // 2]}.\n"
    else:
        median = round((ratings[n // 2 - 1] + ratings[n // 2]) / 2, 1)
        return Fore.GREEN + f"The median rating is {median}.\n"


def get_best_movie():
    """This function returns the best-rated movie(s)."""
    max_rating = max(info["rating"] for info in movies.values())
    best = [f"{name} ({info['year']}): {info['rating']}" for name, info in movies.items() if
            info["rating"] == max_rating]
    return Fore.GREEN + "Best rated movie(s):\n" + "\n".join(Fore.BLUE + m for m in best)


def get_worst_movie():
    """This function returns the worst-rated movie(s)."""
    min_rating = min(info["rating"] for info in movies.values())
    worst = [f"{name} ({info['year']}): {info['rating']}" for name, info in movies.items() if
             info["rating"] == min_rating]
    return Fore.GREEN + "Worst rated movie(s):\n" + "\n".join(Fore.BLUE + m for m in worst)


# This is the main function


def main():
    """This is the main function that runs the movie database app."""
    show_app_name()
    while True:
        show_menu()
        user_input()
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
    """This function asks for user input (number(1-8)) and calls functions depending on that input."""
    choice = input(Fore.YELLOW + "Enter choice (1-8): ")
    print("")
    if choice == "0":
        print(Fore.BLUE + "Bye!")
        exit()
    if choice == "1":
        list_movies()
    if choice == "2":
        add_movie()
    if choice == "3":
        delete_movie()
    if choice == "4":
        update_movie()
    if choice == "5":
        get_stats()
    if choice == "6":
        get_random_movie()
    if choice == "7":
        search_movie()
    if choice == "8":
        get_sorted_list_by_rtg()
    if choice not in "1, 2, 3, 4, 5, 6, 7, 8":
        print(Fore.YELLOW + "Please provide your choice in the form of a number (1-8).")


if __name__ == "__main__":
    main()
