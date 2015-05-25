
# GoogleSearch
####Search the web with python

`GoogleSearch` is a Python 2 library for searching the web, using
Google's Custom Search JSON/Atom API. `GoogleSearch` provides a simple
python API for this task, as a wrapper around Google's.


```python
from googlesearch import GoogleSearch

gs = GoogleSearch("An intriguing query")
for url in gs.top_urls():
    print url
```


##Examples

Print a list of top hits for a query. 
Like a miniature first page of hits on Google.

```python
from googlesearch import GoogleSearch
from pprint import pprint

gs = GoogleSearch("Bacon")
for hit in gs.top_results():
    pprint(hit)
    print
```
-----------------	

Query Wikipedia and show the top hit.

```python
from googlesearch import GoogleSearch

def search_wikipedia(query):
    gs = GoogleSearch("wikipedia.com: %s" % query)
	print gs.top_result()['titleNoFormatting']
	print gs.top_url()
	return gs.top_url()

wiki_url = search_wikipedia("Porcupine")
```
-----------------	

Which of the two words is used more on the Internet?

```python
from googlesearch import GoogleSearch

def x_vs_y_count_match(x, y):
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

counts = x_vs_y_count_match("color", "colour")
```	
-----------------	

Retrieve the imdb id for a movie using only its name
(and year if there are remakes)

```python
from googlesearch import GoogleSearch
import re
    
def imdb_id_for_movie(movie_name):
	query = 'imdb.com: %s' % movie_name
	url = GoogleSearch( query ).top_url()
	imdb_id = re.search('/tt[0-9]+/', url).group(0).strip('/')
	print 'The imdb id for %s is %s' % (movie_name, imdb_id)
	return imdb_id

TotRecall_id = imdb_id_for_movie("Total Recall 1990")
```
-----------------	
    
## Documentation

*class* googlesearch.**GoogleSearch**(query, use_proxy=True, verbose=True)
A Google search object for a specific query.

**Parameters**:
**query**: str
The search query for this search

**use_proxy**: bool
If True, GoogleSearch will use the proxies defined in the
PROXIES_LIST variable of googlesearch_settings.py to do the
searches. If a proxy starts getting HTTP 403 FORBIDDEN responses,
it will switch to the next proxy in the list. It will raise a
GoogleAPIError only if all proxies get 403 responses. 

**verbose**: bool
If True, GoogleSearch will report to sys.stderr when it switches to
another proxy. No logging at all if False.


GoogleSearch.**top_results()**
Returns a list of results for a google search.
Google API determines how many results are returned, current
default is 4.

A result is a dictionary (json) with the following fields:
cacheUrl
content
title
titleNoFormatting
unescapedUrl
url
visibleUrl


GoogleSearch.**top_result()**
Returns only the top result, the best match.
This is the equivalent of "I feel lucky"
See GoogleSearch.**top_results()** for the keys
in the result dictionary


GoogleSearch.**top_urls()**
Returns a list of urls for a google search.
Google API determines how many urls are returned, current
default is 4.


GoogleSearch.**top_url()**
Returns the url of the top hit.


GoogleSearch.**count()**
Returns the total number of matches to the query.


## Requirements

- Python >= 2.6
- requests

## License

MIT licensed. See the bundled [LICENSE](https://github.com/frrmack/googlesearch/blob/master/LICENSE) file for more details.

