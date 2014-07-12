import json
import requests

class Altmetric:

    host = "http://api.altmetric.com"
    base_path = "/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key

    def __getattr__(self, mode):
        def get(self, *args, **kwargs):
            return self.fetch(mode, *args, **kwargs)
        return get.__get__(self)
    """
    def fetch(self):
        url = self.construct_url()
        r = requests.get(url, params=self.params)
        return r.json()
    """
    """
    def construct_url(self):
        if self.mode == 'citations':
            request_url = host + base_path + '/'
            
            if self.timeframe:
                request_url += self.timeframe

        return request_url
    """


 
                
