#!/usr/bin/env python

import sys
from StringIO import StringIO
from BaseHTTPServer import BaseHTTPRequestHandler

import requests

from apikey import APIKEY
from regrws import CustomerPayload, ErrorPayload

NAMESPACEDEF = 'xmlns="http://www.arin.net/regrws/core/v1"'

iso3166_1 = CustomerPayload.iso3166_1(code2=['US'],
                                      code3=['USA'],
                                      name=['UNITED STATES'],
                                      e164=['1'])
streetAddress = CustomerPayload.streetAddress([CustomerPayload.line(1, '742 Evergreen Terrace')])
cust = CustomerPayload.customer(city=['Springfield'],
                                iso3166_1=[iso3166_1],
                                customerName=['Simpson Family'],
                                parentOrgHandle=['BARDL'],
                                postalCode=['90210'],
                                privateCustomer=['false'],
                                streetAddress=[streetAddress],
                                iso3166_2=['OR'])

stringio = StringIO()
cust.export(stringio, 0, pretty_print=False,
            namespace_='',
            namespacedef_=NAMESPACEDEF)
xml = stringio.getvalue()
stringio.close()

parentnethandle = 'NET-206-220-184-0-1'
url = 'https://reg.arin.net/rest/net/%s/customer' % parentnethandle
qargs = {'apikey': APIKEY}
headers = {'content-type': 'application/xml'}
try:
    r = requests.post(url, params=qargs, data=xml, headers=headers)
except requests.exceptions.RequestException as e:
    print 'ERROR:', e[0]
    sys.exit(1)
if r.status_code != requests.codes.ok:
    errorpayload = ErrorPayload.parseString(r.content)
    print r.status_code, errorpayload.message[0]
    sys.exit(1)
else:
    custpayload = CustomerPayload.parseString(r.content)
