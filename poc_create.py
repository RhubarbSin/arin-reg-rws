#!/usr/bin/env python

# from __future__ import absolute_import
import sys
import argparse
import re
from StringIO import StringIO

import pycountry

from regrws import restful
# from arin import regrws.payload.poc
import regrws.method.poc
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

class ParseError(Exception):

    def __init__(self, *args):
        super(ParseError, self).__init__(*args)

epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
arg_parser = argparse.ArgumentParser(epilog=epilog)
arg_parser.add_argument('-k', '--key', help='ARIN API key',
                        required=False if APIKEY else True, dest='api_key')
arg_parser.add_argument('-s', '--source-address', help='Source IP address')
arg_parser.add_argument('template_file', metavar='TEMPLATE_FILE')
args = arg_parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

nums = re.compile('\d+')
payload = regrws.payload.poc.poc()
street_address = regrws.payload.poc.streetAddress()
addr_count = 0
emails = regrws.payload.poc.emails()
phones = regrws.payload.poc.phones()
phone_office = None
for line in open(args.template_file, 'r').readlines():
    if not nums.match(line):
        continue
    name, value = line.split(':', 1)
    if not value.strip():
        continue
    if name == '03. Contact Type (P or R)':
        if value.strip() == 'P':
            payload.contactType = ['PERSON']
        elif value.strip() == 'R':
            payload.contactType=['ROLE']
        else:
            raise ParseError('Invalid value for Contact Type')
    elif name == '04. Last Name or Role Account':
        payload.lastName = [value.strip()]
    elif name == '05. First Name':
        payload.firstName = [value.strip()]
    elif name == '06. Middle Name':
        payload.middleName = [value.strip()]
    elif name == '07. Company Name':
        payload.companyName = [value.strip()]
    elif name == '08. Address':
        addr_count += 1
        addr = regrws.payload.poc.line(addr_count, value.strip())
        street_address.add_line(addr)
    elif name == '09. City':
        payload.city = [value.strip()]
    elif name == '10. State/Province':
        payload.iso3166_2 = [value.strip()]
    elif name == '11. Postal Code':
        payload.postalCode = [value.strip()]
    elif name == '12. Country Code':
        country = pycountry.countries.get(alpha2=value.strip())
        iso3166_1 = regrws.payload.poc.iso3166_1(code2=[country.alpha2],
                                                 code3=[country.alpha3],
                                                 name=[country.name],
                                                 e164=['1'])
        payload.iso3166_1 = [iso3166_1]
    elif name == '13. Office Phone Number':
        type_ = [regrws.payload.poc.type_(code=['O'])]
        phone_office = regrws.payload.poc.phone(number=[value.strip()],
                                                type_=type_)
        phones.add_phone(phone_office)
    elif name == '14. Office Phone Number Extension' and phone_office:
        phone_office.add_extension([value.strip()])
    elif name == '15. E-mail Address':
        emails.add_email(value.strip())
    elif name == '16. Mobile':
        type_ = [regrws.payload.poc.type_(code=['M'])]
        phone_mobile = regrws.payload.poc.phone(number=[value.strip()],
                                                type_=type_)
        phones.add_phone(phone_mobile)
    elif name == '17. Fax':
        type_ = [regrws.payload.poc.type_(code=['F'])]
        phone_fax = regrws.payload.poc.phone(number=[value.strip()],
                                             type_=type_)
        phones.add_phone(phone_fax)

payload.streetAddress = [street_address]
payload.emails = [emails]
payload.phones = [phones]

# payload.export(sys.stdout, 0)
# sys.exit(1)

stringio = StringIO()
payload.export(stringio, 0, pretty_print=False,
               namespace_='',
               namespacedef_=restful.NAMESPACEDEF)
xml = stringio.getvalue()
stringio.close()

session = restful.Session(APIKEY, '66.181.160.152')
method = regrws.method.poc.Create(session)
try:
    pocpayload = method.call(xml)
except restful.RegRwsError as exception:
    print exception.args
