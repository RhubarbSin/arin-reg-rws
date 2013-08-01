#!/usr/bin/env python

import sys

import requests

from apikey import APIKEY
from regrws import CustomerPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s CUSTOMERHANDLE' % sys.argv[0]
    sys.exit(2)

custhandle = sys.argv[1]
url = 'https://reg.arin.net/rest/customer/%s' % custhandle
qargs = {'apikey': APIKEY}
try:
    r = requests.get(url, params=qargs)
except requests.exceptions.RequestException as e:
    print 'ERROR:', e[0]
    sys.exit(1)
if r.status_code != requests.codes.ok:
    errorpayload = ErrorPayload.parseString(r.content)
    print r.status_code, errorpayload.message[0]
    sys.exit(1)
else:
    custpayload = CustomerPayload.parseString(r.content)
    print '''
Name: %s
Parent org handle: %s
Registration date: %s
''' % (custpayload.customerName[0],
       custpayload.parentOrgHandle[0],
       custpayload.registrationDate[0])
    for line in custpayload.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
%s''' % (custpayload.city[0],
         custpayload.iso3166_2[0],
         custpayload.postalCode[0],
         custpayload.iso3166_1[0].name[0])
