# -*- coding: utf-8 -*-

"""HTTP Client Module"""

import logging
import json


try:
    import requests
except ImportError:
    REQUEST_IMPORT = False
    import urllib
else:
    REQUEST_IMPORT = True
    version = requests.__version__
    major, minor, patch = [int(i) for i in version.split('.')]


def send_http_request(url, data, method, headers={}):
    """Sends http request"""

    if not isinstance(data, dict):
        logging.error('Data parameter should be of type dict')
        return

    if not isinstance(headers, dict):
        logging.error('headers parameter should be of type dict')
        return

    if REQUEST_IMPORT:
        client = RequestClient()
    else:
        client = UrllibClient()

    return client.request(url, data, method, headers)

class RequestClient(object):
    """Request HTTP Client"""

    def request(self, url, data, method, headers={} ):
        'Sends HTTP Request through Request Library'

        if not REQUEST_IMPORT:
            logging.error('Something is wrong')
            return

        if method not in ('get', 'post'):
            logging.error('Invalid method type')
            return

        try:
            if method is 'post':
                response = requests.post(url, data=json.dumps(data), headers=headers)
            elif method is 'get':
                response = requests.get(url, params=data, headers=headers)
            
            return (response.json(), response.status_code, response.headers)
        except requests.exceptions.RequestException as exe:
            self.handle_request_error(exe)
            return (exe.response.json(), exe.response.status_code, exe.response.headers)


    def handle_request_error(self, url_exe):
        """Handles http url error"""

        msg = 'Unexpected error communicating with TalkLocal.' + \
        'If this problem persists' + \
        ', let us know at https://github.com/makarand-mac/talklocal_python/issues'
        logging.error(msg)


class UrllibClient(object):
    """Urllib HTTP Client"""

    def request(self, url, data, method, headers={}):
        'Sends http request'

        if method not in ('get', 'post'):
            logging.error('Invalid method type')
            return

        req = urllib.request.Request(url, data, headers, method=method)

        try:
            response = urllib.request.urlopen(req)
            rbody = response.read()
            rcode = response.code

            headers = dict(response.info())

            return (rbody, rcode, headers)

        except urllib.error.HTTPError as exe:
            ecode = exe.code
            ebody = exe.read()
            headers = dict(exe.info())

            return (ebody, ecode, headers)

        except (urllib.error.URLError, ValueError) as url_exe:
            self.handle_request_error(url_exe)

    def handle_request_error(self, url_exe):
        """Handles http url error"""

        msg = 'Unexpected error communicating with TalkLocal.' + \
        'If this problem persists' + \
        ', let us know at https://github.com/makarand-mac/talklocal_python/issues'
        logging.error(msg)
