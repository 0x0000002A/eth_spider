from urllib import request
from utils import filter

class request_handle:
    def __init__(self):
        pass
    
    def read_url(self, url):
        response = request.urlopen(url)
        self.page_content = response.read()
        return self.page_content


