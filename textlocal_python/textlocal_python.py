# -*- coding: utf-8 -*-

"""Talk Local Main module."""

from  talklocal_python.http_client import send_http_request


class TalkLocalClient():
    """Talk Local Client Class"""

    sendAPI = 'https://api.textlocal.in/send/'
    getGroupsAPI = 'https://api.textlocal.in/get_groups/'
    getScheduledMessagesAPI = 'https://api.textlocal.in/get_scheduled/'
    shortUrlAPI = 'https://api.textlocal.in/create_shorturl/'
    cancelScheduledMessagesAPI = 'https://api.textlocal.in/cancel_scheduled/'

    def __init__(self, apikey):
        self.apikey = apikey

    def send_message(self, numbers, message, sender=None, test=False):
        """Sends messages using Talk Local, Numbers can be comma separated"""

        params = {'apikey': self.apikey, 'numbers': numbers, 'message': message}

        if not sender is None:
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
        """Gets Scheduled messages on Talk Local"""

        params = {'apikey': self.apikey}
        return send_http_request(self.get_scheduled_messages, params, 'post')

    def cancel_scheduled_messages(self, sent_id):
        """Cancels Scheduled messages on Talk Local"""

        params = {'apikey': self.apikey, 'sent_id': sent_id}
        return send_http_request(self.cancel_scheduled_messages, params, 'post')

    def get_groups(self):
        """Gets Groups on Talk Local"""

        params = {'apikey': self.apikey}
        return send_http_request(self.getGroupsAPI, params, 'post')

    def get_cost(self, numbers, message, sender=None):
        """Gets cost of particular message or messages"""

        response, code, headers = self.send_message(numbers, message, sender, True)
        if response['status'] is 'success':
            return response['code']

        return response, code, headers

    def create_short_url(self, url):
        """Creates short url"""

        params = {'apikey': self.apikey, 'url': url}
        return send_http_request(self.shortUrlAPI, params, 'post')
