from __future__ import absolute_import

from regrws import restful
from regrws.payload import poc

class _Method(restful.Method):

    """Base class for calls to POC-related RESTful methods."""

    payload = poc  # payload module for this module's classes

class Get(_Method):

    url = 'https://reg.arin.net/rest/poc/'

    def __init__(self, session, handle):
        super(Get, self).__init__(session, 'get')
        self.url += handle

class Create(_Method):

    url = 'https://reg.arin.net/rest/poc;makeLink=true'

    def __init__(self, session):
        super(Create, self).__init__(session, 'post')

class Delete(_Method):

    url = 'https://reg.arin.net/rest/poc/'

    def __init__(self, session, handle):
        super(Delete, self).__init__(session, 'delete')
        self.url += handle
