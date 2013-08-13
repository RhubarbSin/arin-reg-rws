#!/usr/bin/env python

import sys
import argparse

import regrws
import regrws.method.poc
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
parser = argparse.ArgumentParser(epilog=epilog)
parser.add_argument('-k', '--key', help='ARIN API key',
                    required=False if APIKEY else True, dest='api_key')
parser.add_argument('-s', '--source-address', help='Source IP address')
parser.add_argument('handle', metavar='HANDLE')
args = parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

session = regrws.restful.Session(APIKEY, args.source_address)
method = regrws.method.poc.Delete(session, args.handle)
try:
    payload_out = method.call()
except regrws.restful.RegRwsError as exception:
    print exception.args
