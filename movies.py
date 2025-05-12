from colorama import Fore, Back, Style, init
import random

init(autoreset=True)

movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7
}


# Functions executing menu item actions


def list_movies():
    """This function displays all movie titles and ratings in green."""
    print(Fore.GREEN + f"{len(movies)} movies in total")
    for name, rating in movies.items():
        print(Fore.BLUE + f"{name}: {rating}")


def add_movie():
    """This function prompts user to input a movie name and rating, then adds it to the dictionary."""
    movie_name = input(Fore.YELLOW + "Please enter the name of the movie you'd like to add: ")
    movie_rating = input(Fore.YELLOW + "Please enter a rating (a number between 1-10): ")
    movies[movie_name] = float(movie_rating)


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
        movies[movie_key] = float(new_rating)


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
    for name, rating in movies.items():
        if query.lower() in name.lower():
            print(Fore.BLUE + f"{name}: {rating}")
            found = True
    if not found:
        print(Fore.YELLOW + "The movie is not in the database.")


def get_sorted_list_by_rtg():
    """This function displays movies sorted by rating in descending order."""
    sorted_by_val = dict(sorted(movies.items(), reverse=True, key=lambda movie: movie[1]))
    print(Fore.GREEN + "Movies sorted by rating:")
    for name, rating in sorted_by_val.items():
        print(Fore.BLUE + f"{name}: {rating}")


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
    sum_ratings = 0
    for name, rating in movies.items():
        sum_ratings += float(rating)
    avg_rtg = round(sum_ratings / len(movies), 1)
    return Fore.GREEN + f"The average rating of all movie ratings in the database is {avg_rtg}"


def get_median_rating():
    """This function returns the median movie rating."""
    sorted_rtg_list = sorted(movies.values())
    n = len(sorted_rtg_list)
    if n % 2 != 0:
        # if n odd, median is the middle number of the sorted list
        return Fore.GREEN + f"The median rating of all ratings in the database is {sorted_rtg_list[n // 2]}.\n"
    else:
        # if n even, median is the average of the two middle numbers
        even_median = round((sorted_rtg_list[n // 2 - 1] + sorted_rtg_list[n // 2]) / 2, 1)
        return Fore.GREEN + f"The median rating of all ratings in the database is {even_median}.\n"


def get_best_movie():
    """This function returns the best-rated movie(s)."""
    best_movies_dict = {}
    for name, rating in movies.items():
        if rating >= max(movies.values()):
            best_movies_dict[name] = rating
    best_movies = ""
    for movie, rtg in best_movies_dict.items():
        best_movies += Fore.BLUE + f"{movie}: {rtg}\n"
    return Fore.GREEN + f"The movie(s) with the highest rating:\n{best_movies}"


def get_worst_movie():
    """This function returns the worst-rated movie(s)."""
    worst_movies_dict = {}
    for name, rating in movies.items():
        if rating <= min(movies.values()):
            worst_movies_dict[name] = rating
    worst_movies = ""
    for movie, rtg in worst_movies_dict.items():
        worst_movies += Fore.BLUE + f"{movie}: {rtg}\n"
    return Fore.GREEN + f"The movie(s) with the lowest rating:\n{worst_movies}"


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
