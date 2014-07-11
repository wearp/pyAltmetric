import json

import requests

class Altmetric:

    def __init__(self, mode, timeframe=None, **kwargs):
        self.mode = mode
        self.timeframe = timeframe
        self.params = kwargs 
        self.base_url = 'http://api.altmetric.com/v1/'
    
    def fetch(self):
        url = self.construct_url()
        r = requests.get(url, params=self.params)
        return r.json()
           
    def construct_url(self):
        if self.mode == 'citations':
            request_url = self.base_url + self.mode + '/'
            
            if self.timeframe:
                request_url += self.timeframe

        return request_url

 
                
