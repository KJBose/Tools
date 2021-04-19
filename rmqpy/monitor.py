import pika
import requests
import json
import datetime
import os
import sys

sys.path.append(os.environ['CONFIG'])
from config import *

def __init__(self):
    #self.url = url
    self.user = config.rabbitmq.user
    self.passwd = config.rabbitmq.passwd


def get_open_channel(hosturl):
    open_channel = []
    user = config.rabbitmq.user
    passwd = config.rabbitmq.passwd
    endpoint_paginate = "/api/channels/page=1&page_size=50"
    endpoint = "/api/channels"
    #response = requests.get(hosturl+endpoint, auth=(self.user, self.passwd))
    response = requests.get(hosturl+endpoint, auth=(user, passwd))
    results = json.loads(response.text)
    open_channels = len(results)
    return open_channel

def get_open_channel_count(hosturl):
    open_channel_count = 0
    user = config.rabbitmq.user
    passwd = config.rabbitmq.passwd
    endpoint_paginate = "/api/channels/page=1&page_size=50"
    endpoint = "/api/channels"
    #response = requests.get(hosturl+endpoint, auth=(self.user, self.passwd))
    response = requests.get(hosturl+endpoint, auth=(user, passwd))
    results = json.loads(response.text)
    open_channels = len(results)
    return open_channel_count
