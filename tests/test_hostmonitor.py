import pytest
import rmqpy
import sys
import os
from unittest.mock import Mock
from tests.__mocks__ import pika
import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

sys.path.append(os.environ['CONFIG'])
from config import *

@pytest.mark.integration
def test_get_open_channel(host=config.rabbitmq.host):
    '''channel = pika.Channel()
    channel.basic_publish = Mock()

    rmqpy.sender.publish(channel, 'BOSE')

    channel.basic_publish.assert_called_once_with(
        routing_key=config.rabbitmq.queue,
        exchange=config.rabbitmq.exchange,
        body='BOSE'
    )'''
    rmqhost = host
    open_channel = rmqpy.monitor.get_open_channel(rmqhost)
    print("list of open channels: %r", open_channel)

@tl.job(interval=timedelta(seconds=300))
def test_get_open_channel_count(host):
    '''channel = pika.Channel()
    channel.basic_publish = Mock()

    rmqpy.sender.publish(channel, 'BOSE')

    channel.basic_publish.assert_called_once_with(
        routing_key=config.rabbitmq.queue,
        exchange=config.rabbitmq.exchange,
        body='BOSE'
    )'''
    rmqhost = host
    open_channel = rmqpy.monitor.get_open_channel_count(rmqhost)
    print("list of open channels: %r", open_channel)

'''def test_monitor_threshold(config.rabbitmq.host):
    continue2monitor = 1
    for continue2monitor != 0:
        open_channel = rmqpy.get_open_channel_count(rmqhost)
        if open_channel > 10:
            raise alarm
        if datetime.time > 1hr:
            print('continue_to_monitor?')
            interupt = raw_input()
            if interupt == 'stop':
                continue2monitor = 0
            else sleep(5)
                continue2monitor += 1
        else:
            continue'''

rmqhost=config.rabbitmq.host
open_channel = test_get_open_channel_count(rmqhost)
print("open channel count: %r", open_channel)
