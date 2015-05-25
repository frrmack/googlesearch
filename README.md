# GoogleSearch
#####Search the web with python

GoogleSearch is a Python 2 library for searching the web, using
Google's Custom Search JSON/Atom API. It provides a simple
python API for this task, as a wrapper around Google's.


```python
>>> from googlesearch import GoogleSearch
>>> gs = GoogleSearch("An intriguing query")
>>> for url in gs.top_urls():
...    print url
...
```
```
http://www.torontosun.com/2015/02/08/cbcs-ascension-an-intriguing-sci-fi-drama
http://www.agentquery.com/writer_hq.aspx
http://www.girlfridayproductions.com/2015/02/how-to-write-a-great-query-letter/
http://nelsonagency.com/2015/04/special-treat-rhiannon-thomass-original-query-letter-for-a-wcked-thing/
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
*Output*:
```
{u'GsearchResultClass': u'GwebSearch',
 u'cacheUrl':
 u'http://www.google.com/search?q=cache:JkI9aWzUvbgJ:en.wikipedia.org',
 u'content': u'<b>Bacon</b> is a meat product prepared from a pig and usually cured. It is first cured \nusing large quantities of salt, either in a brine or in a dry packing; the result is \nfresh\xa0...',
 u'title': u'<b>Bacon</b> - Wikipedia, the free encyclopedia',
 u'titleNoFormatting': u'Bacon - Wikipedia, the free encyclopedia',
 u'unescapedUrl': u'http://en.wikipedia.org/wiki/Bacon',
 u'url': u'http://en.wikipedia.org/wiki/Bacon',
 u'visibleUrl': u'en.wikipedia.org'}

{u'GsearchResultClass': u'GwebSearch',
 u'cacheUrl':
 u'http://www.google.com/search?q=cache:_cHIoqEzleAJ:en.wikipedia.org',
 u'content': u'Francis <b>Bacon</b>, 1st Viscount St. Alban, QC (/\u02c8be\u026ak\u0259n/; 22 January 1561 \u2013 9 April \n1626), was an English philosopher, statesman, scientist, jurist, orator, essayist\xa0...',
 u'title': u'Francis <b>Bacon</b> - Wikipedia, the free encyclopedia',
 u'titleNoFormatting': u'Francis Bacon - Wikipedia, the free encyclopedia',
 u'unescapedUrl': u'http://en.wikipedia.org/wiki/Francis_Bacon',
 u'url': u'http://en.wikipedia.org/wiki/Francis_Bacon',
 u'visibleUrl': u'en.wikipedia.org'}

{u'GsearchResultClass': u'GwebSearch',
 u'cacheUrl':
 u'http://www.google.com/search?q=cache:uKyfbazYgokJ:baconaustin.com',
 u'content': u'<b>Bacon</b>. <b>Bacon</b>; 900 W 10th St; Austin, Texas 78703. Hours: Monday - Friday: \n11am - 9pm; Saturday: 9am - 9pm; Sunday: 9am - 3pm. View Larger Map\xa0...',
 u'title': u'<b>Bacon</b>',
 u'titleNoFormatting': u'Bacon',
 u'unescapedUrl': u'http://baconaustin.com/',
 u'url': u'http://baconaustin.com/',
 u'visibleUrl': u'baconaustin.com'}

{u'GsearchResultClass': u'GwebSearch',
 u'cacheUrl': u'http://www.google.com/search?q=cache:oxQ3rEMOdAwJ:www.foodnetwork.com',
 u'content': u'Make <b>bacon</b> the star ingredient in pastas, salads, snacks and more from Food \nNetwork Magazine.',
 u'title': u'50 Things to Make With <b>Bacon</b> : Recipes and Cooking : Food Network',
 u'titleNoFormatting': u'50 Things to Make With Bacon : Recipes and Cooking : Food Network',
 u'unescapedUrl': u'http://www.foodnetwork.com/recipes/articles/50-things-to-make-with-bacon.html',
 u'url': u'http://www.foodnetwork.com/recipes/articles/50-things-to-make-with-bacon.html',
 u'visibleUrl': u'www.foodnetwork.com'}
```
-----------------	

Query Wikipedia and show the top hit.

```python
from googlesearch import GoogleSearch

def search_wikipedia(query):
    gs = GoogleSearch("site:wikipedia.com %s" % query)
	print gs.top_result()['titleNoFormatting']
	print gs.top_url()
	return gs.top_url()

wiki_url = search_wikipedia("Porcupine")
```
*Output*:
```
Porcupine - Wikipedia, the free encyclopedia
http://en.wikipedia.org/wiki/Porcupine
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
*Output*:
```
color vs colour:
color wins with 259000000 vs 55500000
```
-----------------	

Retrieve the imdb id for a movie using only its name
(and year if there are remakes)

```python
from googlesearch import GoogleSearch
import re
    
def imdb_id_for_movie(movie_name):
	query = 'site:imdb.com %s' % movie_name
	url = GoogleSearch( query ).top_url()
	imdb_id = re.search('/tt[0-9]+/', url).group(0).strip('/')
	print 'The imdb id for %s is %s' % (movie_name, imdb_id)
	return imdb_id

TotRecall_id = imdb_id_for_movie("Total Recall 1990")
```
*Output*:
```
The imdb id for Total Recall 1990 is tt0100802
```
-----------------	
    
## Documentation

*class* googlesearch.**GoogleSearch**(query, use_proxy=True, verbose=True)

* A Google search object for a specific query.

* **Parameters**

  * **query**: str   
  The search query for this search

  * **use_proxy**: bool, default: True   
  If True, GoogleSearch will use the proxies defined in the
PROXIES_LIST variable of googlesearch_settings.py to do the
searches. If a proxy starts getting HTTP 403 FORBIDDEN responses,
it will switch to the next proxy in the list. It will raise a
GoogleAPIError only if all proxies get 403 responses. 

  * **verbose**: bool, default: True   
  If True, GoogleSearch will report to sys.stderr when it switches to
another proxy. No logging at all if False.

**Methods**

* GoogleSearch.**top_results()**

  * Returns a list of results for a google search.
Google API determines how many results are returned, current
default is 4.   
A result is a dictionary with the following fields:   
cacheUrl   
content   
title   
titleNoFormatting   
unescapedUrl   
url   
visibleUrl   


* GoogleSearch.**top_result()**

  * Returns only the top result, the best match.
This is the equivalent of "I feel lucky"
See GoogleSearch.top_results() for the keys
in the result dictionary.


* GoogleSearch.**top_urls()**

  * Returns a list of urls for a google search.
Google API determines how many urls are returned, current
default is 4.


* GoogleSearch.**top_url()**

  * Returns the url of the top hit.


* GoogleSearch.**count()**

  * Returns the total number of matches to the query.


## Requirements

- Python >= 2.6
- requests

## License

MIT licensed. See the bundled [LICENSE](https://github.com/frrmack/googlesearch/blob/master/LICENSE) file for more details.

