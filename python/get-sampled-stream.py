import json
import os
import requests
from requests.auth import AuthBase
from pprint import pprint

from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

# Retrieves and stores credential information from the '.env' file
#BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")

options = "&format=default"
stream_url = "https://api.twitter.com/labs/1/tweets/stream/sample"

headers = {
    "Accept-Encoding": "gzip"
}

# Gets a bearer token
class BearerTokenAuth(AuthBase):
    def __init__(self, consumer_key, consumer_secret):
        self.bearer_token_url = "https://api.twitter.com/oauth2/token"
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.bearer_token = self.get_bearer_token()

    def get_bearer_token(self):
        response = requests.post(
            self.bearer_token_url,
            auth=(self.consumer_key, self.consumer_secret),
            data={'grant_type': 'client_credentials'},
            headers={'User-Agent': 'TwitterDevRecentSearxhStreamQuickStartPython'})

        if response.status_code is not 200:
            raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" % (response.status_code, response.text))

        body = response.json()
        return body['access_token']

    def __call__(self, r):
        r.headers['Authorization'] = f"Bearer %s" % self.bearer_token
        r.headers['User-Agent'] = 'TwitterDevFilteredStreamQuickStartPython'
        return r

def stream_connect(auth):
    response = requests.get(stream_url, auth=auth, headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"}, stream=True)
    for response_line in response.iter_lines():
        if response_line:
            pprint(json.loads(response_line))

bearer_token = BearerTokenAuth(CONSUMER_KEY, CONSUMER_SECRET)

# Listen to the stream. This reconnection logic will attempt to reconnect as soon as a disconnection is detected.
while True:
    stream_connect(bearer_token)