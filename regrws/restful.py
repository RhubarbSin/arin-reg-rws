"""Classes supporting calls to ARIN's Registration RESTful Web Service
(Reg-RWS) via the Python Requests package.

https://www.arin.net/resources/restful-interfaces.html
https://www.arin.net/resources/restfulmethods.html
https://www.arin.net/resources/restfulpayloads.html
"""

from httplib import HTTPSConnection

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import PoolManager, HTTPSConnectionPool

from regrws.payload import error as errorpayload

NAMESPACEDEF = 'xmlns="http://www.arin.net/regrws/core/v1"'

class MyAdapter(HTTPAdapter):

    """This transport adapter and its supporting subclasses of
    PoolManager and HTTPSConnectionPool support specifying a source
    address via keyword arg "src_addr" ultimately propagated to the
    socket creation (requires "source_address" arg added to
    HTTPSConnection in Python 2.7).
    """

    def __init__(self, *args, **kwargs):
        # src_addr MUST be a keyword arg
        self.src_addr = kwargs.pop('src_addr', None)
        super(MyAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs['src_addr'] = self.src_addr
        self.poolmanager = MyPoolManager(*args, **kwargs)

class MyPoolManager(PoolManager):

    def __init__(self, *args, **kwargs):
        self.src_addr = kwargs.pop('src_addr', None)
        super(MyPoolManager, self).__init__(*args, **kwargs)

    def _new_pool(self, scheme, host, port):
        kwargs = self.connection_pool_kw
        if scheme == 'http':
            kwargs = self.connection_pool_kw.copy()
            for kw in SSL_KEYWORDS:
                kwargs.pop(kw, None)
        kwargs['src_addr'] = self.src_addr
        return MyHTTPSConnectionPool(host, port, **kwargs)

class MyHTTPSConnectionPool(HTTPSConnectionPool):

    def __init__(self, *args, **kwargs):
        self.src_addr = kwargs.pop('src_addr', None)
        super(MyHTTPSConnectionPool, self).__init__(*args, **kwargs)

    def _new_conn(self):
        # original method is more elaborate (uses VerifiedHTTPSConnection)
        self.num_connections += 1
        source_address = (self.src_addr, 0) if self.src_addr else None
        return HTTPSConnection(host=self.host,
                               port=self.port,
                               strict=self.strict,
                               source_address=source_address)

class Session(requests.Session):

    """Class for Requests Sessions that make calls to ARIN Reg-RWS
    methods.
    """

    def __init__(self, api_key, src_addr=None):
        super(Session, self).__init__()
        self.params = {'apikey': api_key}  # all calls need API key
        if src_addr:  # MyAdapter supports source address
            self.mount('https://', MyAdapter(src_addr=src_addr))

class RegRwsError(Exception):

    """Trivial subclass for exceptions in regrws."""

    def __init__(self, *args):
        super(RegRwsError, self).__init__(*args)

class Method(object):

    """Base class for calls to ARIN Reg-RWS RESTful methods."""

    def __init__(self, session, query_type):
        self.query_method = getattr(session, query_type)

    def call(self):
        """This method is overridden by subclasses that need to
        provide extra keyword arguments to self._call().
        """

        return self._call()

    def _call(self, **kwargs):
        try:
            r = self.query_method(self.url, **kwargs)
        except requests.exceptions.RequestException as e:
            raise RegRwsError(*e.args)
        self._check_status(r)
        return self.payload.parseString(r.content)

    def _check_status(self, response):
        if response.status_code != requests.codes.ok:
            payload = errorpayload.parseString(response.content)
            args = [response.status_code, payload.message[0]]
            if payload.components[0].hasContent_():
                for c in payload.components[0].component:
                    args.append('%s: %s' % (c.name[0], c.message[0]))
            raise RegRwsError(*args)

