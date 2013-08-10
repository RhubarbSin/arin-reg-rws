#!/usr/bin/env python

import sys
from StringIO import StringIO

import requests

from apikey import APIKEY
from regrws import restful, PocPayload, ErrorPayload

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

session = restful.Session(APIKEY, '66.181.160.152')
method = restful.PocCreate(session)
pocpayload = method.call(xml)
