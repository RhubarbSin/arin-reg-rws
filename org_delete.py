#!/usr/bin/env python

import sys

import requests

from apikey import APIKEY
from regrws import OrgPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s ORGHANDLE' % sys.argv[0]
    sys.exit(2)

orghandle = sys.argv[1]
url = 'https://reg.arin.net/rest/org/%s' % orghandle
qargs = {'apikey': APIKEY}
try:
    r = requests.delete(url, params=qargs)
except requests.exceptions.RequestException as e:
    print 'ERROR:', e[0]
    sys.exit(1)
if r.status_code != requests.codes.ok:
    errorpayload = ErrorPayload.parseString(r.content)
    print r.status_code, errorpayload.message[0]
    sys.exit(1)
else:
    orgpayload = OrgPayload.parseString(r.content)
