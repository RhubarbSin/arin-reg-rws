#!/usr/bin/env python

import sys

import requests

from apikey import APIKEY
from regrws import restful, PocPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s POCHANDLE' % sys.argv[0]
    sys.exit(2)

session = restful.Session(APIKEY, '66.181.160.152')
method = restful.PocDelete(session, sys.argv[1])
pocpayload = method.call()

# pochandle = sys.argv[1]
# url = 'https://reg.arin.net/rest/poc/%s' % pochandle
# qargs = {'apikey': APIKEY}
# try:
#     r = requests.delete(url, params=qargs)
# except requests.exceptions.RequestException as e:
#     print 'ERROR:', e[0]
#     sys.exit(1)
# if r.status_code != requests.codes.ok:
#     errorpayload = ErrorPayload.parseString(r.content)
#     print r.status_code, errorpayload.message[0]
#     sys.exit(1)
# else:
#     pocpayload = PocPayload.parseString(r.content)
