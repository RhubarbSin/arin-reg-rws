#!/usr/bin/env python

import sys
import argparse

import regrws.convert
import regrws.payload.org
import regrws.method.org
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

description = 'Create ARIN recipient ORG from template'
epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
arg_parser = argparse.ArgumentParser(description=description, epilog=epilog)
arg_parser.add_argument('-k', '--key', help='ARIN API key',
                        required=False if APIKEY else True, dest='api_key')
arg_parser.add_argument('-s', '--source-address', help='Source IP address')
arg_parser.add_argument('net_handle', metavar='NET_HANDLE')
arg_parser.add_argument('-t', '--test', action='store_true',
                        help='Test mode: omit actual RESTful call')
arg_parser.add_argument('template_file', metavar='TEMPLATE_FILE')
args = arg_parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

with open(args.template_file, 'r') as fh:
    template = fh.readlines()
parser = regrws.convert.DictFromTemplate(template)
converter = regrws.convert.PayloadFromDict(parser.run(),
                                           regrws.payload.org.org)
payload_in = converter.run()

if args.test:
    payload_in.export(sys.stderr, 0)
else:
    session = regrws.restful.Session(APIKEY, args.source_address)
    method = regrws.method.org.Create(session, args.net_handle)
    try:
        payload_out = method.call(payload_in)
    except regrws.restful.RegRwsError as exception:
        print exception.args
