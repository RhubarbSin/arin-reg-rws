#!/usr/bin/env python

import sys
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler

from apikey import APIKEY
from regrws import CustomerPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s CUSTOMERHANDLE' % sys.argv[0]
    sys.exit(2)

custhandle = sys.argv[1]
url = 'https://reg.arin.net/rest/customer/%s?apikey=%s' % (custhandle, APIKEY)
try:
    response = urllib2.urlopen(url).read()
except urllib2.HTTPError as exc:
    errorpayload = ErrorPayload.parseString(exc.read())
    print errorpayload.message
    sys.exit(1)
else:
    custpayload = CustomerPayload.parseString(response)
    print '''
Name: %s
Parent org handle: %s
Registration date: %s
''' % (custpayload.customerName[0],
       custpayload.parentOrgHandle[0],
       custpayload.registrationDate[0])
    for line in custpayload.streetAddress[0].get_line():
        print line.get_valueOf_()
    print '''%s, %s %s
%s''' % (custpayload.city[0],
         custpayload.iso3166_2[0],
         custpayload.postalCode[0],
         custpayload.iso3166_1[0].name[0])
