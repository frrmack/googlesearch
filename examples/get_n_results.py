from googlesearch import GoogleSearch

def get_n_results(query, n):
    """ Print a list of n hits from Google"""
    from pprint import pprint
    gs = GoogleSearch(query)
    for hit in gs.get_results(n):
        pprint(hit)
        print

if __name__ == '__main__':

    print_top_results("Bacon", 12)
    
        
