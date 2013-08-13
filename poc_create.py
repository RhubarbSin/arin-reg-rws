#!/usr/bin/env python

# from __future__ import absolute_import
import sys
import argparse

from regrws import restful
import regrws.template.poc
import regrws.method.poc
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
arg_parser = argparse.ArgumentParser(epilog=epilog)
arg_parser.add_argument('-k', '--key', help='ARIN API key',
                        required=False if APIKEY else True, dest='api_key')
arg_parser.add_argument('-s', '--source-address', help='Source IP address')
arg_parser.add_argument('template_file', metavar='TEMPLATE_FILE')
args = arg_parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

with open(args.template_file, 'r') as fh:
    payload_in = regrws.template.poc.parse_lines(fh.readlines())

session = restful.Session(APIKEY, args.source_address)
method = regrws.method.poc.Create(session)
try:
    payload_out = method.call(payload_in)
except restful.RegRwsError as exception:
    print exception.args
