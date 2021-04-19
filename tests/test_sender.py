import pytest
import rmqpy
import sys
import os
from unittest.mock import Mock
from tests.__mocks__ import pika

sys.path.append(os.environ['CONFIG'])
from config import *

@pytest.mark.unit
def test_sender_publish_new_message(monkeypatch):
    channel = pika.Channel()
    channel.basic_publish = Mock()

    rmqpy.sender.publish(channel, 'BOSE')

    channel.basic_publish.assert_called_once_with(
        routing_key=config.rabbitmq.queue,
        exchange=config.rabbitmq.exchange,
        body='BOSE'
    )
