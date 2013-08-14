from __future__ import absolute_import

import pycountry

from regrws.payload import poc
from regrws.template.exception import ParseError

def payload_from_dict(template_input):
    """Return a POC payload from a dict of template input."""

    def contact_type():
        if value == 'P':
            payload.contactType = ['PERSON']
        elif value == 'R':
            payload.contactType = ['ROLE']
        else:
            raise ParseError('Invalid value for Contact Type')

    def address():
        if isinstance(value, str):
            street_address.add_line(poc.line(1, value))
        else:
            for count, item in enumerate(value, 1):
                street_address.add_line(poc.line(count, item))

    def country_code():
        country = pycountry.countries.get(alpha2=value)
        iso3166_1 = poc.iso3166_1(code2=[country.alpha2],
                                  code3=[country.alpha3],
                                  name=[country.name])
        payload.iso3166_1 = [iso3166_1]

    # map of dict keys to handler functions
    dispatch = {'Contact Type (P or R)': contact_type,
                'Address': address,
                'Country Code': country_code}
    # map of dict keys to payload's simple list attributes
    simple = {'Last Name or Role Account': 'lastName',
              'First Name': 'firstName',
              'Middle Name': 'middleName',
              'Company Name': 'companyName',
              'City': 'city',
              'State/Province': 'iso3166_2',
              'Postal Code': 'postalCode'}
    payload = poc.poc()
    street_address = poc.streetAddress()
    emails = poc.emails()
    phones = poc.phones()
    phone_office = None

    for key, value in template_input.iteritems():
        if key in dispatch:
            dispatch[key]()
        elif key == 'Office Phone Number':
            type_ = [poc.type_(code=['O'])]
            phone_office = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_office)
        elif key == 'Office Phone Number Extension' and phone_office:
            phone_office.add_extension(value)
        elif key == 'E-mail Address':
            emails.add_email(value)
        elif key == 'Mobile':
            type_ = [poc.type_(code=['M'])]
            phone_mobile = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_mobile)
        elif key == 'Fax':
            type_ = [poc.type_(code=['F'])]
            phone_fax = poc.phone(number=[value], type_=type_)
            phones.add_phone(phone_fax)
        else:
            if getattr(payload, simple.get(key, ''), None) is not None:
                setattr(payload, simple[key], [value])

    payload.streetAddress = [street_address]
    payload.emails = [emails]
    payload.phones = [phones]
    return payload
