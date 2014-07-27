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
            raise HTTPException(response.status_code, response.reason)
        else:
            try:
                return response.json()
            except ValueError as e:
                raise AltmetricException(e.message)
 

class Citation(object):

    def __init__(self, dic):
        for field, value in dic.iteritems():
            setattr(self, field, value)

    def __repr__(self):
        return '<Citation %s: %s>' % (self.altmetric_id, self.title)

    def __iter__(self):
        """Each iteration returns a field, value tuple."""
        for field, value in (vars(self)).iteritems():
            yield field, value

    def get_fields(self, *args):
        """
        Returns a list containing values of the named fields in '*args'. 
        If named field does not exist, an empty string is returned to the list.
        """
        return [getattr(self, field, '') for field in args]


class CitationCollection(object):
    
    def __init__(self):
        self.citations = list()

    def __iter__(self):
        self.__pos = 0
        return self

    def next(self):
        if self.__pos >= len(self.citations):
            raise StopIteration
        self.__pos += 1
        return self.citations[self.__pos - 1]

    def add_citation(self, *args):
        """Adds a Citation instance, or instances to CitationCollection."""
        self.citations.extend(args)



