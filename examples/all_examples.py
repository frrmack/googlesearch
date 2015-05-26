from examples.top_results import print_top_results
from examples.search_wikipedia import search_wikipedia
from examples.count_match import x_vs_y_count_match
from examples.imdb_id import imdb_id_for_movie

def showcase_all_examples():
    separator = '\n------------------\n'

    ##### EXAMPLE 1: Top Results for "Testing" #####
    print_top_results("Bacon")

    print separator

    ##### EXAMPLE 2: Search Wikipedia (first hit) #####
    search_wikipedia("Porcupine")

    print separator

    ##### EXAMPLE 3: Which is used more, "color" or "colour"? #####
    x_vs_y_count_match("color", "colour")

    print separator

    ##### EXAMPLE 4: Retrieve imdb id of a movie #####
    imdb_id_for_movie("Total Recall 1990")

    print separator
    

if __name__ == '__main__':

    showcase_all_examples()
    

