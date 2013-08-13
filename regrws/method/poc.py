from __future__ import absolute_import

from regrws import restful
from regrws.payload import poc

class Method(restful.Method):

    payload = poc

class Get(Method):

    url = 'https://reg.arin.net/rest/poc/'

    def __init__(self, session, handle):
        super(Get, self).__init__(session, 'get')
        self.url += handle

class Create(Method):

    url = 'https://reg.arin.net/rest/poc;makeLink=true'

    def __init__(self, session):
        super(Create, self).__init__(session, 'post')

    def call(self, payload):
        headers = {'content-type': 'application/xml'}
        kwargs = {'headers': headers, 'data': self._export_to_xml(payload)}
        return self._call(**kwargs)

class Delete(Method):

    url = 'https://reg.arin.net/rest/poc/'

    def __init__(self, session, handle):
        super(Delete, self).__init__(session, 'delete')
        self.url += handle
