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
 
                
