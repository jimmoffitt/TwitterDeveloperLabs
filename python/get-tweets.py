import argparse
import json
import os
import urllib.parse
import requests
from requests.auth import AuthBase

from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

# Retrieves and stores credential information from the '.env' file
#BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")

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


def get_tweets(auth):

    url = f"https://api.twitter.com/labs/1/tweets?ids={ids}{options}"
    response = requests.get(url, auth=auth, headers = headers)

    if response.status_code is not 200:
        raise Exception(f"Cannot get rules (HTTP %d): %s" % (response.status_code, response.text))

    return response

ids = "1189360732753793024,1186045618340237312"
options = "&format=compact"
bearer_token = BearerTokenAuth(CONSUMER_KEY, CONSUMER_SECRET)

response = get_tweets(bearer_token)

parsed = json.loads(response.text)
pretty_print = json.dumps(parsed, indent=2, sort_keys=True)
print (pretty_print)

