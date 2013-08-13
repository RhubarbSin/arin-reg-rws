#!/usr/bin/env python

import sys
import argparse

import regrws
import regrws.method.org
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

# parsing of arguments
epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
parser = argparse.ArgumentParser(epilog=epilog)
parser.add_argument('-k', '--key', help='ARIN API key',
                    required=False if APIKEY else True, dest='api_key')
parser.add_argument('-s', '--source-address', help='Source IP address')
parser.add_argument('handle', metavar='ORG_HANDLE')
args = parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

# the main action
session = regrws.restful.Session(APIKEY, args.source_address)
method = regrws.method.org.Get(session, args.handle)
try:
    payload_out = method.call()
except regrws.restful.RegRwsError as exception:
    print exception.args

# the rest just displays some values from the payload
else:
    print '''
Name: %s
Handle: %s
Registration date: %s
''' % (payload_out.orgName[0],
       payload_out.handle[0],
       payload_out.registrationDate[0])
    for line in payload_out.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
%s''' % (payload_out.city[0],
         payload_out.iso3166_2[0],
         payload_out.postalCode[0],
         payload_out.iso3166_1[0].name[0])

    print '\nAssociated POCs:'
    for poc_link_ref in payload_out.pocLinks[0].pocLinkRef:
        print poc_link_ref.description, poc_link_ref.handle

payload_out.exportLiteral(sys.stdout, 0)
