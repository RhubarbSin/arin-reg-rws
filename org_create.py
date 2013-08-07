#!/usr/bin/env python

import sys
from StringIO import StringIO

import requests

from apikey import APIKEY
from regrws import OrgPayload, ErrorPayload

NAMESPACEDEF = 'xmlns="http://www.arin.net/regrws/core/v1"'

if len(sys.argv) != 2:
    print 'Usage: %s POCHANDLE' % sys.argv[0]
    sys.exit(2)

pochandle = sys.argv[1]

iso3166_1 = OrgPayload.iso3166_1(code2=['US'],
                                 code3=['USA'],
                                 name=['UNITED STATES'],
                                 e164=['1'])
streetAddress = OrgPayload.streetAddress([OrgPayload.line(1, '742 Evergreen Terrace')])
pocLinks = OrgPayload.pocLinks([OrgPayload.pocLinkRef('T', pochandle, 'Tech'),
                                OrgPayload.pocLinkRef('AD', pochandle, 'Admin'),
                                OrgPayload.pocLinkRef('AB', pochandle, 'Abuse')])
org = OrgPayload.org(city=['Springfield'],
                     iso3166_1=[iso3166_1],
                     orgName=['Simpson Family'],
                     dbaName=['DBA Simpson Family Farms'],
                     taxId=['A Tax ID'],
                     postalCode=['90210'],
                     streetAddress=[streetAddress],
                     iso3166_2=['OR'],
                     pocLinks=[pocLinks])

stringio = StringIO()
org.export(stringio, 0, pretty_print=False,
           namespace_='',
           namespacedef_=NAMESPACEDEF)
xml = stringio.getvalue()
stringio.close()

parentnethandle = 'NET-206-220-184-0-1'
url = 'https://reg.arin.net/rest/net/%s/org' % parentnethandle
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
    orgpayload = OrgPayload.parseString(r.content)
