#!/usr/bin/env python

import sys

import requests

from apikey import APIKEY
from regrws import OrgPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s ORGHANDLE' % sys.argv[0]
    sys.exit(2)

orghandle = sys.argv[1]
url = 'https://reg.arin.net/rest/org/%s' % orghandle
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
    orgpayload = OrgPayload.parseString(r.content)
    print '''
Name: %s
Handle: %s
Registration date: %s
''' % (orgpayload.orgName[0],
       orgpayload.handle[0],
       orgpayload.registrationDate[0])
    for line in orgpayload.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
%s''' % (orgpayload.city[0],
         orgpayload.iso3166_2[0],
         orgpayload.postalCode[0],
         orgpayload.iso3166_1[0].name[0])

    print '\nAssociated POCs:'
    for poc_link_ref in orgpayload.pocLinks[0].pocLinkRef:
        print poc_link_ref.description, poc_link_ref.handle
