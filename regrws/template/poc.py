from __future__ import absolute_import
import re

import pycountry

from regrws.payload import poc
from regrws.template.exception import ParseError

def parse_lines(template_contents):
    """Return a POC payload from a list of template lines."""

    template_re = re.compile('\d+.*:')
    payload = poc.poc()
    street_address = poc.streetAddress()
    addr_count = 0
    emails = poc.emails()
    phones = poc.phones()
    phone_office = None

    for line in template_contents:
        if not template_re.match(line):
            continue
        name, value = line.split(':', 1)
        value = value.strip()
        if not value:
            continue

        if name == '03. Contact Type (P or R)':
            if value == 'P':
                payload.contactType = ['PERSON']
            elif value == 'R':
                payload.contactType=['ROLE']
            else:
                raise ParseError('Invalid value for Contact Type')
        elif name == '04. Last Name or Role Account':
            payload.lastName = [value]
        elif name == '05. First Name':
            payload.firstName = [value]
        elif name == '06. Middle Name':
            payload.middleName = [value]
        elif name == '07. Company Name':
            payload.companyName = [value]
        elif name == '08. Address':
            addr_count += 1
            street_address.add_line(poc.line(addr_count, value))
        elif name == '09. City':
            payload.city = [value]
        elif name == '10. State/Province':
            payload.iso3166_2 = [value]
        elif name == '11. Postal Code':
            payload.postalCode = [value]
        elif name == '12. Country Code':
            country = pycountry.countries.get(alpha2=value)
            iso3166_1 = poc.iso3166_1(code2=[country.alpha2],
                                      code3=[country.alpha3],
                                      name=[country.name])
            payload.iso3166_1 = [iso3166_1]
        elif name == '13. Office Phone Number':
            type_ = [poc.type_(code=['O'])]
            phone_office = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_office)
        elif name == '14. Office Phone Number Extension' and phone_office:
            phone_office.add_extension(value)
        elif name == '15. E-mail Address':
            emails.add_email(value)
        elif name == '16. Mobile':
            type_ = [poc.type_(code=['M'])]
            phone_mobile = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_mobile)
        elif name == '17. Fax':
            type_ = [poc.type_(code=['F'])]
            phone_fax = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_fax)

    payload.streetAddress = [street_address]
    payload.emails = [emails]
    payload.phones = [phones]
    return payload
