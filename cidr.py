#!/usr/bin/env python
"""Get WHOIS data for CIDR address."""

import sys

import rws
import rws.whois.method

session = rws.restful.Session()
method = rws.whois.method.Cidr(session, sys.argv[1])
try:
    payload_out = method.call()
except rws.restful.RwsError as exception:
    print exception.args

payload_out.export(sys.stdout, 0)
