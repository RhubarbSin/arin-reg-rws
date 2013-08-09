from httplib import HTTPSConnection

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import PoolManager, HTTPSConnectionPool

import PocPayload

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

    def __init__(self, api_key, src_addr=None):
        super(Session, self).__init__()
        self.params = {'apikey': api_key}
        self.mount('https://', MyAdapter(src_addr=src_addr))

class RegRwsException(Exception):

    def __init__(self, *args):
        super(RegRwsException, self).__init__(*args)

class Method(object):

    """Base class for classes that implement ARIN Reg-RWS RESTful calls."""

    def call(self, session):
        try:
            r = session.get(self.url)
        except requests.exceptions.RequestException as e:
            raise RegRwsException(*e.args)
        self._check_status(r)
        return self.payload.parseString(r.content)

    def _check_status(self, response):
        if response.status_code != requests.codes.ok:
            errorpayload = ErrorPayload.parseString(response.content)
            raise RegRwsException(response.status_code,
                                  errorpayload.message[0])

class PocGet(Method):

    url = 'https://reg.arin.net/rest/poc/'
    payload = PocPayload

    def __init__(self, poc_handle):
        self.url += poc_handle
