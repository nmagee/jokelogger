#!/usr/local/bin/python3

# Note different shebang above - for devcontainer

import requests
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="joke.log", encoding="utf-8")

url = "https://official-joke-api.appspot.com/random_joke"

try:
    # get the payload
    response = requests.get(url)
    status = response.status_code
    # check to see that we got a good 200-OK status from the request
    if (status == 200):
        logging.info('Request successful')
        # put it into json format
        response = json.loads(response.text)
        # fetch each data point by key
        id = response['id']
        setup = response['setup']
        punchline = response['punchline']
        # log the data
        logging.warning('%s:%s:%s', id, setup, punchline)
    # in case we got a bad status response
    else:
        logging.error('Request failed: %s', status)
except Exception as e:
    # log the error
    logging.error(e)

# Notes:
# If you add a random character to the URL, you will force the "else" stanza to run.
# If you try a URL that does not exist you will force the exception to run.