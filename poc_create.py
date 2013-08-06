#!/usr/bin/env python

import sys
from StringIO import StringIO

import requests

from apikey import APIKEY
from regrws import PocPayload, ErrorPayload

NAMESPACEDEF = 'xmlns="http://www.arin.net/regrws/core/v1"'

iso3166_1 = PocPayload.iso3166_1(code2=['US'],
                                 code3=['USA'],
                                 name=['UNITED STATES'],
                                 e164=['1'])
emails = PocPayload.emails(['homer@simpson.org'])
phones = PocPayload.phones([PocPayload.phone(number=['+1.404.246.7890'],
                                             type_=[PocPayload.type_(description=['OFFICE'], code=['O'])])])
streetAddress = PocPayload.streetAddress([PocPayload.line(1, '742 Evergreen Terrace')])
poc = PocPayload.poc(city=['Springfield'],
                     companyName=['Simpson Family'],
                     contactType=['ROLE'],
                     iso3166_1=[iso3166_1],
                     emails=[emails],
                     lastName=['Admin'],
                     phones=[phones],
                     postalCode=['90210'],
                     streetAddress=[streetAddress],
                     iso3166_2=['OR'])

stringio = StringIO()
poc.export(stringio, 0, pretty_print=False,
           namespace_='',
           namespacedef_=NAMESPACEDEF)
xml = stringio.getvalue()
stringio.close()

url = 'https://reg.arin.net/rest/poc;makeLink=true'
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
    pocpayload = PocPayload.parseString(r.content)
