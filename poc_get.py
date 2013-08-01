#!/usr/bin/env python

import sys

import requests

from apikey import APIKEY
from regrws import PocPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s POCHANDLE' % sys.argv[0]
    sys.exit(2)

pochandle = sys.argv[1]
url = 'https://reg.arin.net/rest/poc/%s' % pochandle
qargs = {'apikey': APIKEY}
r = requests.get(url, params=qargs)
if r.status_code != requests.codes.ok:
    errorpayload = ErrorPayload.parseString(r.content)
    print r.status_code, errorpayload.message[0]
    sys.exit(1)
else:
    pocpayload = PocPayload.parseString(r.content)
    name = ''
    if pocpayload.firstName:
        name += pocpayload.firstName[0]
    if pocpayload.middleName:
        name += pocpayload.middleName[0]
    if pocpayload.lastName:
        name += pocpayload.lastName[0]
    print name
    for email in pocpayload.emails[0].email:
        print email
    print pocpayload.companyName[0]
    for line in pocpayload.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
%s''' % (pocpayload.city[0],
         pocpayload.iso3166_2[0],
         pocpayload.postalCode[0],
         pocpayload.iso3166_1[0].name[0])
