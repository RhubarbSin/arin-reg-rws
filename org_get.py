#!/usr/bin/env python

import sys
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler

from apikey import APIKEY
from regrws import OrgPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s ORGHANDLE' % sys.argv[0]
    sys.exit(2)

orghandle = sys.argv[1]
url = 'https://reg.arin.net/rest/org/%s?apikey=%s' % (orghandle, APIKEY)
try:
    response = urllib2.urlopen(url).read()
except urllib2.HTTPError as exc:
    errorpayload = ErrorPayload.parseString(exc.read())
    print errorpayload.message
    sys.exit(1)
else:
    orgpayload = OrgPayload.parseString(response)
    print '''
Name: %s
Handle: %s
Registration date: %s
''' % (orgpayload.orgName[0],
       orgpayload.handle[0],
       orgpayload.registrationDate[0])
    for line in orgpayload.streetAddress[0].get_line():
        print line.get_valueOf_()
    print '''%s, %s %s
%s''' % (orgpayload.city[0],
         orgpayload.iso3166_2[0],
         orgpayload.postalCode[0],
         orgpayload.iso3166_1[0].name[0])

    print '\nAssociated POCs:'
    for poc_link_ref in orgpayload.pocLinks[0].get_pocLinkRef():
        print poc_link_ref.description, poc_link_ref.handle
