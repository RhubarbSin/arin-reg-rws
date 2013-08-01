#!/usr/bin/env python

import sys
import urllib2
import logging
from BaseHTTPServer import BaseHTTPRequestHandler

from apikey import APIKEY
from regrws import CustomerPayload # , ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s CUSTOMERHANDLE' % sys.argv[0]
    sys.exit(2)

log = logging.getLogger('pyxb.binding.content')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

custhandle = sys.argv[1]
url = 'https://reg.arin.net/rest/customer/%s?apikey=%s' % (custhandle, APIKEY)
try:
    response = urllib2.urlopen(url).read()
except urllib2.HTTPError as exc:
    del CustomerPayload
    from regrws import ErrorPayload
    errorpayload = ErrorPayload.CreateFromDocument(exc.read())
    print errorpayload.message[0]
    sys.exit(1)
else:
    custpayload = CustomerPayload.CreateFromDocument(response)
    print custpayload.toDOM().toprettyxml()
