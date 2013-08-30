from __future__ import absolute_import

from regrws import restful
from regrws.payload import org

class _Method(restful.Method):

    """Base class for calls to ORG-related RESTful methods."""

    payload = org  # payload module for this module's classes

class Get(_Method):

    url = 'https://reg.arin.net/rest/org/'

    def __init__(self, session, handle):
        super(Get, self).__init__(session, 'get')
        self.url += handle

class Create(_Method):

    url = 'https://reg.arin.net/rest/net/%s/org'

    def __init__(self, session, handle):
        super(Create, self).__init__(session, 'post')
        self.url = self.url % handle

class Delete(_Method):

    url = 'https://reg.arin.net/rest/org/'

    def __init__(self, session, handle):
        super(Delete, self).__init__(session, 'delete')
        self.url += handle
