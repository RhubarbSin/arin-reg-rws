#!/usr/bin/env python

import sys
import argparse

from regrws import restful
from regrws.method import poc as pocmethod
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
parser.add_argument('handle', metavar='HANDLE')
args = parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

# the main action
session = restful.Session(APIKEY, args.source_address)
method = pocmethod.Get(session, args.handle)
try:
    poc_payload = method.call()
except restful.RegRwsError as exception:
    print exception.args

# the rest just displays some values from the payload
else:
    name = ''
    if poc_payload.firstName:
        name += poc_payload.firstName[0] + ' '
    if poc_payload.middleName:
        name += poc_payload.middleName[0] + ' '
    if poc_payload.lastName:
        name += poc_payload.lastName[0]

    print name
    for email in poc_payload.emails[0].email:
        print email
    print poc_payload.companyName[0]
    for line in poc_payload.streetAddress[0].line:
        print line.valueOf_
    print '''%s, %s %s
    %s''' % (poc_payload.city[0], poc_payload.iso3166_2[0],
             poc_payload.postalCode[0], poc_payload.iso3166_1[0].name[0])
