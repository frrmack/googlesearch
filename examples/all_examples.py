from examples.top_results import print_top_results
from examples.top_results_in_spanish import print_top_results_in_spanish
from examples.get_n_results import get_n_results
from examples.search_wikipedia import search_wikipedia
from examples.count_match import x_vs_y_count_match
from examples.imdb_id import imdb_id_for_movie

def showcase_all_examples():
    separator = '\n------------------\n'

    ##### EXAMPLE 1: Top Results for "Bacon" #####
    print_top_results("Bacon")

    print separator

    ##### EXAMPLE 2: Top Results for "Bacon", in spanish #####
    print_top_results_in_spanish("Bacon")

    print separator

    ##### EXAMPLE 3: Search Wikipedia (first hit) #####
    search_wikipedia("Porcupine")

    print separator

    ##### EXAMPLE 4: Which is used more, "color" or "colour"? #####
    x_vs_y_count_match("color", "colour")

    print separator

    ##### EXAMPLE 5: Retrieve imdb id of a movie #####
    imdb_id_for_movie("Total Recall 1990")

    print separator
    

    ##### EXAMPLE 10: Top 12 results for Bacon #####
    get_n_results("Bacon", 12)

    print separator


if __name__ == '__main__':

    showcase_all_examples()
    

