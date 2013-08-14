from __future__ import absolute_import
import re

import pycountry

from regrws.payload import org

def parse_lines(template_contents):
    """Return an ORG payload from a list of template lines."""

    template_re = re.compile('\d+.*:')
    payload = org.org()
    street_address = org.streetAddress()
    addr_count = 0
    poc_links = org.pocLinks()

    for line in template_contents:
        if not template_re.match(line):
            continue
        name, value = line.split(':', 1)
        value = value.strip()
        if not value:
            continue

        if name == "03. Organization's Legal Name":
            payload.orgName = [value]
        elif name == "04. Organization's D/B/A":
            payload.dbaName = [value]
        elif name == '05. Business Tax ID Number (DO NOT LIST SSN)':
            payload.taxId = [value]
        elif name == '06. Org Address':
            addr_count += 1
            street_address.add_line(org.line(addr_count, value))
        elif name == '07. Org City':
            payload.city = [value]
        elif name == '08. Org State/Province':
            payload.iso3166_2 = [value]
        elif name == '09. Org Postal Code':
            payload.postalCode = [value]
        elif name == '10. Org Country Code':
            country = pycountry.countries.get(alpha2=value)
            iso3166_1 = org.iso3166_1(code2=[country.alpha2],
                                      code3=[country.alpha3],
                                      name=[country.name])
            payload.iso3166_1 = [iso3166_1]
        elif name == '11. Admin POC Handle':
            poc_links.add_pocLinkRef(org.pocLinkRef(function='AD',
                                                    handle=value))
        elif name == '12. Tech POC Handle':
            poc_links.add_pocLinkRef(org.pocLinkRef(function='T',
                                                    handle=value))
        elif name == '13. Abuse POC Handle':
            poc_links.add_pocLinkRef(org.pocLinkRef(function='AB',
                                                    handle=value))
        elif name == '14. NOC POC Handle':
            poc_links.add_pocLinkRef(org.pocLinkRef(function='N',
                                                    handle=value))

    payload.streetAddress = [street_address]
    payload.pocLinks = [poc_links]
    return payload
