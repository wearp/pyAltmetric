import json
import requests


class AltmetricException(Exception):
    pass


class HTTPException(Exception):
    def __init__(self, status_code, message):
        super(HTTPException, self).__init__(status_code, message)
        self.status_code = status_code
        self.message = message


class Altmetric(object):
    """
    Altmetric builds a URL to query the Altmetric.com database. The response 
    from Altmetric is a dict.
    
    Usage:

        a = Altmetric()
        a.citations("1w", num_results=100, cited_in='reddit')
        a.doi('10.1038/nature1379')

    More information on querying the database and response object is available
    at api.altmetric.com.
    """
    host = "http://api.altmetric.com/"
    api_version = "v1/"
    base_url = host + api_version

    def __init__(self, api_key=None):
        self.params = {}
        if api_key:
            self.params = {'key': api_key}

    def __getattr__(self, mode):
        def get(self, *args, **kwargs):
            return self.fetch(mode, *args, **kwargs) 
        return get.__get__(self)
    
    def __repr__(self):
        if self.api_key:
            return '<Altmetric %s: %s>' % (self.api_version, self.api_key)
        else:
            return '<Altmetric %s>' % self.api_version

    def fetch(self, mode, *args, **kwargs):
        url = self.base_url + mode + "/" + "/".join([a for a in args])
        if kwargs != None:
            self.params.update(kwargs)
       
        try:
            response = requests.get(url, params=self.params)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            if response.status_code == 404 and response.reason == 'Not Found':
                return None
            raise HTTPException(response.status_code, response.reason)
        else:
            try:
                return response.json()
            except ValueError as e:
                raise AltmetricException(e.message)
 

class Citation(object):
    """
    Citation is initialized using a response object from the Altmetric class. 
    These are succesful responses from all modes ('doi', 'id', etc.), 
    except 'citations'.

    Usage:
        
        a = Altmetric()
        c = a.id("108989")  
        
        c = Citation(b) # or Citation(a.id("108989"))
        print c.title
    """
    def __init__(self, dic):
        # 'altmetric_id' is a required field in a citation
        if 'altmetric_id' in dic:
            for field, value in dic.iteritems():
                setattr(self, field, value)
        else:
            raise AltmetricException("Not a valid citation object")

    def get_fields(self, *args):
        """
        Returns a list containing values of the named fields in '*args'. 
        If named field does not exist, an empty string is returned to the list.
        """
        return [getattr(self, field, '') for field in args]
    
    def __repr__(self):
        stats = self.get_fields('title', 'doi', 'journal', 
            'cited_by_posts_count', 'cited_by_tweeters_count', 
            'cited_by_fbwalls_count', 'cited_by_gplus_count',
            'cited_by_rdts_count', 'cited_by_feeds_count')
       
        # replace '' with '0'
        for i in range(len(stats)):
            if not stats[i]:
                stats[i] = '0'

        return ('Altmetrics on: "{0}" with doi {1} published in {2}.\n\n' 
                '{3:11s} {4:>5}\n'
                '{5:11s} {6:>5}\n'
                '{7:11s} {8:>5}\n'
                '{9:11s} {10:>5}\n'
                '{11:11s} {12:>5}\n'
                '{13:11s} {14:>5}\n\n').format(stats[0], stats[1], stats[2],
                            'All Posts', stats[3], 'Tweets', stats[4], 
                            'Facebook', stats[5], 'Google+', stats[6],
                            'Reddit', stats[7], 'Blogs', stats[8])


