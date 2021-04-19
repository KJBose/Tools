import pytest
import rmqpy
import sys
import os
from unittest.mock import Mock
from tests.__mocks__ import pika

sys.path.append(os.environ['CONFIG'])
from config import *

@pytest.mark.unit
def test_channel_sets_parameters(monkeypatch):
    mocked_pika = Mock()
    mocked_pika.URLParameters.return_value = 'BOSE'
    monkeypatch.setattr('rmqpy.channel.pika', mocked_pika)

    rmqpy.channel.create('BOSE HOST')

    mocked_pika.URLParameters.assert_called_once_with('BOSE HOST')


@pytest.mark.unit
def test_channel_creates_connection(monkeypatch):
    mocked_pika = Mock()
    mocked_pika.URLParameters.return_value = 'BOSE'
    mocked_pika.BlockingConnection.return_value = pika.Connection()
    monkeypatch.setattr('rmqpy.channel.pika', mocked_pika)

    rmqpy.channel.create('BOSE HOST')

    mocked_pika.BlockingConnection.assert_called_once_with('BOSE')
