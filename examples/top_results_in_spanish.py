from googlesearch import GoogleSearch

def print_top_results_in_spanish(query):
    """ Print a list of top hits for a query. 
    Like a mini returned first page on Google.
    Language setted in parameter hl"""
    from pprint import pprint
    gs = GoogleSearch(query, hl='es')
    for hit in gs.top_results():
        pprint(hit)
        print

if __name__ == '__main__':

    print_top_results_in_spanish("Bacon")
    