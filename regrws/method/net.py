from __future__ import absolute_import

from regrws import restful
from regrws.payload import net

class _Method(restful.Method):

    """Base class for calls to NET-related RESTful methods."""

    payload = net  # payload module for this module's classes

class Get(_Method):

    url = 'https://reg.arin.net/rest/net/'

    def __init__(self, session, handle):
        super(Get, self).__init__(session, 'get')
        self.url += handle

class Delete(_Method):

    url = 'https://reg.arin.net/rest/net/'

    def __init__(self, session, handle):
        super(Delete, self).__init__(session, 'delete')
        self.url += handle
