#### EXAMPLE USES #########

from googlesearch import GoogleSearch

def print_top_results(query):
    """ Print a list of top hits for a query. 
    Like a mini returned first page on Google"""
    from pprint import pprint
    gs = GoogleSearch(query)
    for hit in gs.top_results():
        pprint(hit)
        print


def search_wikipedia(query):
    """Query Wikipedia and show the top hit"""
    gs = GoogleSearch("site:wikipedia.com %s" % query)
    print gs.top_result()['titleNoFormatting']
    print gs.top_url()
    return gs.top_url()


def x_vs_y_count_match(x, y):
    """ Which of two words is used 
    more on the Internet?"""
    nx = GoogleSearch(x).count()
    ny = GoogleSearch(y).count()
    print '%s vs %s:' % (x,y)
    if   nx > ny:
        print '%s wins with %i vs %i' % (x,nx,ny)
    elif nx < ny:
        print '%s wins with %i vs %i' % (y,ny,nx)
    else:
        print "it's a tie with %s each!" % nx
    return nx, ny


def imdb_id_for_movie(movie_name):
    """Retrieve the imdb id for a movie 
    from the name (and year if there are remakes)"""
    query = 'site:imdb.com %s' % movie_name
    url = GoogleSearch( query ).top_url()
    import re
    imdb_id = re.search('/tt[0-9]+/', url).group(0).strip('/')
    print 'The imdb id for %s is %s' % (movie_name, imdb_id)
    return imdb_id


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
    

