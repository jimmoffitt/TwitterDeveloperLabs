import argparse
import json
import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
load_dotenv(verbose=True)  # Throws error if it can't find .env file

# Argparse for cli options. Run `python engagement_totals.py -h` to see list of available arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tweet_ids", nargs='+', required=True,
                    help="Enter one or more comma delimited Tweet IDs (for example: `-t '123,456'`)")

args = parser.parse_args()

# Retrieves and stores credential information from the '.env' file
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Generate user context auth (OAuth1)
user_context_auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, TOKEN_SECRET)

# Totals API endpoint (same for all accounts)
endpoint = f"https://api.twitter.com/labs/1/tweets/metrics/private?ids={args.tweet_ids[0]}"

headers = {"Accept-Encoding": "gzip"}

response = requests.get(endpoint, auth=user_context_auth, headers=headers)

parsed = json.loads(response.text)
pretty_print = json.dumps(parsed, indent=2, sort_keys=True)

print (pretty_print)

