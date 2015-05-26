from googlesearch import GoogleSearch

def search_wikipedia(query):
    """Query Wikipedia and show the top hit"""
    gs = GoogleSearch("site:wikipedia.com %s" % query)
    print gs.top_result()['titleNoFormatting']
    print gs.top_url()
    return gs.top_url()

if __name__ == '__main__':

    wiki_url = search_wikipedia("Bacon")
