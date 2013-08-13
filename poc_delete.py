#!/usr/bin/env python

import sys
import argparse

from regrws import restful
from regrws.method import poc as pocmethod
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

session = restful.Session(APIKEY, args.source_address)
method = pocmethod.Delete(session, args.handle)
try:
    pocpayload = method.call()
except restful.RegRwsError as exception:
    print exception.args
