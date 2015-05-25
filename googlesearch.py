#!/usr/bin/python
"""
Irmak Sirer, 2013

Python Wrapper around the Google API for search

It returns results for a google search.
A result is a dictionary (json) with the following fields:

cacheUrl
content
title
titleNoFormatting
unescapedUrl
url
visibleUrl

"""
import googlesearch_settings as settings
import sys
import json
import urllib, requests

class GoogleAPIError(Exception):
    pass

class GoogleSearch(object):
    
    api_url_template = settings.GOOGLE_API_URL_TEMPLATE
    proxy_no = 0

    def __init__(self, query, use_proxy=True, verbose=True):
        self.query = query
        self._ajax_query = urllib.urlencode({'q': self.query})
        self._result_data = None
        self.use_proxy = use_proxy
        self.verbose = verbose
        if use_proxy and not settings.PROXY_LIST:
            msg = ("If you want to use proxies, you need to define a "
                   "non-empty PROXT_LIST in googlesearch_settings")
            raise ValueError(msg)
        
    @property
    def proxy(self):
        if self.use_proxy:
            return {"http": settings.PROXY_LIST[self.proxy_no]}
        else:
            return {"http": None}

    def switch_to_next_proxy(self):
        num_proxies = len(settings.PROXY_LIST)
        GoogleSearch.proxy_no = (self.proxy_no + 1) % num_proxies
        if self.verbose:
            print >> sys.stderr, ('GoogleSearch switched to '
                                  'proxy number %i' % self.proxy_no)
        
    @property
    def result_data(self):
        if self._result_data is None:
            query_url = self.api_url_template % self._ajax_query
            self._result_data = self.hit_the_search_api(query_url)
        return self._result_data
    
    def hit_the_search_api(self, query_url):
            tried_proxies = 0
            while True:
                search_response = requests.get(query_url, proxies=self.proxy)
                try:
                    response_dict = json.loads(search_response.text)
                    results = response_dict['responseData']
                except ValueError, KeyError:
                    msg = 'HTTP %s\n%s' % (search_response.status_code,
                                           search_response.text)
                    raise GoogleAPIError(msg)

                status = response_dict['responseStatus']
                details = response_dict['responseDetails']
                if status == 403 and self.use_proxy:
                    self.switch_to_next_proxy()
                    tried_proxies += 1
                    if tried_proxies >= len(settings.PROXY_LIST):
                        msg = ('Tried all proxies but all received a 403 FORBIDDEN '
                               'response from the Google API. Either wait for a while '
                               'or add more proxies to the PROXY_LIST in settings')
                        raise GoogleAPIError(msg)
                    continue
                elif status != 200:
                    raise GoogleAPIError(details)

                return results
        
    def top_result(self):
        """ First hit (what "I'm feeling lucky" would return)"""
        return self.result_data['results'][0]

    def top_results(self):
        """ Top hits (only four by default) """
        return self.result_data['results']

    def top_url(self):
        """ URL of the first hit """
        return self.top_result()['unescapedUrl']

    def top_urls(self):
        """ URLs of the top hits """
        get_url = lambda result: result['unescapedUrl']
        return map(get_url, self.top_results())

    def count(self):
        "Number of results"
        return int(self.result_data['cursor']['estimatedResultCount'])



# Apply the tests/examples
if __name__ == '__main__':

    import googlesearch_examples as examples
    examples.showcase_all_examples()


