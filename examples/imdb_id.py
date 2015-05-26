from googlesearch import GoogleSearch

def imdb_id_for_movie(movie_name):
    """Retrieve the imdb id for a movie 
    from the name (and year if there are remakes)"""
    query = 'site:imdb.com %s' % movie_name
    url = GoogleSearch( query ).top_url()
    import re
    imdb_id = re.search('/tt[0-9]+/', url).group(0).strip('/')
    print 'The imdb id for %s is %s' % (movie_name, imdb_id)
    return imdb_id

if __name__ == '__main__':

    imdb_id_for_movie("Total Recall 1990")
    
        
