#!/usr/bin/env python

import sys
import argparse

import regrws
import regrws.template
import regrws.template.poc
import regrws.method.poc
try:
    from apikey import APIKEY
except ImportError:
    APIKEY = None

description = 'Create ARIN POC from template'
epilog = 'API key can be omitted if APIKEY is defined in apikey.py'
arg_parser = argparse.ArgumentParser(description=description, epilog=epilog)
arg_parser.add_argument('-k', '--key', help='ARIN API key',
                        required=False if APIKEY else True, dest='api_key')
arg_parser.add_argument('-s', '--source-address', help='Source IP address')
arg_parser.add_argument('template_file', metavar='TEMPLATE_FILE')
args = arg_parser.parse_args()
if args.api_key:
    APIKEY = args.api_key

converter_t = regrws.template.DictFromTemplateFile(args.template_file)
payload_in = regrws.template.poc.payload_from_dict(converter_t.run())
payload_in.export(sys.stdout, 0)
sys.exit()

session = regrws.restful.Session(APIKEY, args.source_address)
method = regrws.method.poc.Create(session)
try:
    payload_out = method.call(payload_in)
except regrws.restful.RegRwsError as exception:
    print exception.args
