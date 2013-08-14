from httplib import HTTPSConnection

from requests.adapters import HTTPAdapter
from requests.packages.urllib3 import PoolManager, HTTPSConnectionPool

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
