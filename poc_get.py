#!/usr/bin/env python

import sys
import argparse

import regrws
import regrws.method.poc
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
parser.add_argument('poc_handle', metavar='POC_HANDLE')
args = parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

# the main action
session = regrws.restful.Session(APIKEY, args.source_address)
method = regrws.method.poc.Get(session, args.poc_handle)
try:
    payload_out = method.call()
except regrws.restful.RegRwsError as exception:
    print exception.args

# the rest just displays some values from the payload
else:
    name = ''
    if payload_out.firstName:
        name += payload_out.firstName[0] + ' '
    if payload_out.middleName:
        name += payload_out.middleName[0] + ' '
    if payload_out.lastName:
        name += payload_out.lastName[0]

    print name
    for email in payload_out.emails[0].email:
        print email
    print payload_out.companyName[0]
    for line in payload_out.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
    %s''' % (payload_out.city[0], payload_out.iso3166_2[0],
             payload_out.postalCode[0], payload_out.iso3166_1[0].name[0])
