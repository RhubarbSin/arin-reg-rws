"""Classes supporting calls to ARIN's Registration RESTful Web Service
(Reg-RWS) via the Python Requests package.

https://www.arin.net/resources/restful-interfaces.html
https://www.arin.net/resources/restfulmethods.html
https://www.arin.net/resources/restfulpayloads.html
"""

from StringIO import StringIO

import requests

from rws.reg.payload import error
from rws.myrequests import MyAdapter

_NAMESPACEDEF = 'xmlns="http://www.arin.net/regrws/core/v1"'

class Session(requests.Session):

    """Class for Requests Sessions that make calls to ARIN Reg-RWS
    methods.
    """

    def __init__(self, api_key=None, src_addr=None):
        super(Session, self).__init__()
        if api_key:
            self.params = {'apikey': api_key}  # all Reg-RWS calls need API key
        if src_addr:  # MyAdapter supports source address
            self.mount('https://', MyAdapter(src_addr=src_addr))

class RwsError(Exception):

    """Trivial subclass for exceptions in rws package."""

    def __init__(self, *args):
        super(RwsError, self).__init__(*args)

class Method(object):

    """Base class for calls to ARIN RWS RESTful methods."""

    def __init__(self, session, query_type):
        self.query_method = getattr(session, query_type)

    def call(self, payload=None):
        if payload:
            headers = {'content-type': 'application/xml'}
            kwargs = {'headers': headers, 'data': self._export_to_xml(payload)}
        else:
            kwargs = {}
        try:
            r = self.query_method(self.url, **kwargs)
        except requests.exceptions.RequestException as e:
            raise RwsError(*e.args)
        self._check_status(r)
        return self.payload.parseString(r.content)

    def _export_to_xml(self, payload):
        stringio = StringIO()
        payload.export(stringio, 0, pretty_print=False, namespace_='',
                       namespacedef_=_NAMESPACEDEF)
        xml = stringio.getvalue()
        stringio.close()
        return xml

    def _check_status(self, response):
        if response.status_code != requests.codes.ok:
            payload = error.parseString(response.content)
            args = ['%s: %s' % (response.status_code, payload.message[0])]
            if payload.components[0].hasContent_():
                args.extend(['%s: %s' % (c.name[0], c.message[0])
                             for c in payload.components[0].component])
            if payload.additionalInfo[0].hasContent_():
                args.extend([m for m in payload.additionalInfo[0].message])
            raise RegRwsError(*args)
