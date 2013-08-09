#!/usr/bin/env python

import sys

from apikey import APIKEY
from regrws import restful, PocPayload, ErrorPayload

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s POCHANDLE' % sys.argv[0]
        sys.exit(2)

    method = restful.PocGet(sys.argv[1])
    # session = restful.Session(APIKEY)
    session = restful.Session(APIKEY, '66.181.160.152')
    pocpayload = method.call(session)

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
%s''' % (pocpayload.city[0], pocpayload.iso3166_2[0], pocpayload.postalCode[0],
         pocpayload.iso3166_1[0].name[0])
