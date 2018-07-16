# -*- coding: utf-8 -*-

"""Text Local Main module."""

import logging

from  textlocal_python.http_client import send_http_request


class TextLocalClient():
    """Text Local Client Class"""

    sendAPI = 'https://api.textlocal.in/send/'
    getGroupsAPI = 'https://api.textlocal.in/get_groups/'
    getScheduledMessagesAPI = 'https://api.textlocal.in/get_scheduled/'
    shortUrlAPI = 'https://api.textlocal.in/create_shorturl/'
    cancelScheduledMessagesAPI = 'https://api.textlocal.in/cancel_scheduled/'
    getBalanceAPI = 'https://api.textlocal.in/balance/'

    def __init__(self, apikey):
        if apikey is None:
            logging.error('No API Key was provided')
            return
        self.apikey = apikey

    def send_message(self, numbers, message, sender=None, test=False):
        """Sends messages using Text Local, Numbers can be comma separated"""

        params = {'apikey': self.apikey, 'numbers': numbers, 'message': message}

        if sender is not None:
            params['sender'] = sender

        if test:
            params['test'] = 'true'

        return send_http_request(self.sendAPI, params, 'post')

    def schedule_message(self, numbers, message, timestamp, sender=None, test=False):
        """Schedules messages"""

        params = {'apikey': self.apikey, 'numbers': numbers, \
        'message': message, 'timestamp': timestamp}

        if not sender is None:
            params['sender'] = sender

        if test:
            params['test'] = 'true'

        return send_http_request(self.sendAPI, params, 'post')

    def get_scheduled_messages(self):
        """Gets Scheduled messages on Text Local"""

        params = {'apikey': self.apikey}
        return send_http_request(self.get_scheduled_messages, params, 'post')

    def cancel_scheduled_messages(self, sent_id):
        """Cancels Scheduled messages on Text Local"""

        params = {'apikey': self.apikey, 'sent_id': sent_id}
        return send_http_request(self.cancel_scheduled_messages, params, 'post')

    def get_groups(self):
        """Gets Groups on Text Local"""

        params = {'apikey': self.apikey}
        return send_http_request(self.getGroupsAPI, params, 'post')

    def get_cost(self, numbers, message, sender=None):
        """Gets cost of particular message or messages"""
        return self.send_message(numbers, message, sender, True)

    def create_short_url(self, url):
        """Creates short url"""

        params = {'apikey': self.apikey, 'url': url}
        return send_http_request(self.shortUrlAPI, params, 'post')

    def get_balance(self):
        """Gets credits for api"""

        params = {'apikey': self.apikey}
        return send_http_request(self.getBalanceAPI, params, 'post')
