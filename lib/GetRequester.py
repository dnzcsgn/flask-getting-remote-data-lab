import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        #raise an error if the request failed
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content
#converting bytes to a string
    def load_json(self):
        raw_body = self.get_response_body()
        return json.loads(raw_body.decode("utf-8"))