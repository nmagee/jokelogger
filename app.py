#!/usr/bin/python3

import requests
import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="joke.log", encoding="utf-8", level=logging.DEBUG)

url = "https://official-joke-api.appspot.com/random_joke"

try:
    # get the payload
    response = requests.get(url)
    # put it into json format
    response = json.loads(response.text)
    # fetch each data point by key
    id = response['id']
    setup = response['setup']
    punchline = response['punchline']
    # log the data
    logging.warning('%s:%s:%s', id, setup, punchline)
except Exception as e:
    # log the error
    logging.error(e)

