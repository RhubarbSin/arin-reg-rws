from __future__ import absolute_import

import pycountry

import regrws.payload
from regrws.restful import RegRwsError

class PayloadFromDict(object):

    """Method object for converting a dict to a payload."""

    # map of dict keys to handler method names
    handler = {'Contact Type (P or R)': '_contact_type',
               'Address': '_address',
               'Country Code': '_country_code',
               'Office Phone Number': '_office_phone_number',
               'Office Phone Number Extension': '_office_extension',
               'E-mail Address': '_email_address',
               'Mobile': '_mobile',
               'Fax': '_fax'}
    # map of dict keys to payload's simple list attributes
    simple = {'Last Name or Role Account': 'lastName',
              'First Name': 'firstName',
              'Middle Name': 'middleName',
              'Company Name': 'companyName',
              'City': 'city',
              'State/Province': 'iso3166_2',
              'Postal Code': 'postalCode'}
    # dict keys to ignore (not used in payload)
    ignore = ('API Key', 'Registration Action (N,M, or R)',
              'Existing POC Handle', 'Public Comments')

    def __init__(self, source, target):
        self.source = source
        self.module = target.__module__
        self.payload = target()

    def run(self):
        """Return payload built from dict."""

        for key, value in self.source.iteritems():
            if key in self.handler:
                # call the corresponding handler
                method = getattr(self, self.handler[key])
                method(value)
            elif key in self.simple:
                # assign value to attribute if payload has that attribute
                self._verify_attribute(self.simple[key])
                setattr(self.payload, self.simple[key], [value])
            elif key in self.ignore:
                continue
            else:
                raise RegRwsError('%s has no attribute corresponding to key %s' % (self.payload.__class__, key))
        return self.payload

    def _contact_type(self, value):
        self._verify_attribute('contactType')
        if value == 'P':
            self.payload.contactType = ['PERSON']
        elif value == 'R':
            self.payload.contactType = ['ROLE']

    def _address(self, value):
        pass
        # if isinstance(value, str):
        #     street_address.add_line(poc.line(1, value))
        # else:
        #     for count, item in enumerate(value, 1):
        #         street_address.add_line(poc.line(count, item))

    def _country_code(self, value):
        pass
        # country = pycountry.countries.get(alpha2=value)
        # iso3166_1 = poc.iso3166_1(code2=[country.alpha2],
        #                           code3=[country.alpha3],
        #                           name=[country.name])
        # payload.iso3166_1 = [iso3166_1]

    def _office_phone_number(self, value):
        pass

    def _office_extension(self, value):
        pass

    def _email_address(self, value):
        pass

    def _mobile(self, value):
        pass

    def _fax(self, value):
        pass

    def _verify_attribute(self, attr):
        # Input dict should not contain keys that do not correspond to
        # input payload class's data attributes.
        if getattr(self.payload, attr, None) is None:
            raise RegRwsError('%s does not have attribute %s' %
                              (self.payload.__class__, attr))
