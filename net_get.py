#!/usr/bin/env python 

import sys
from BaseHTTPServer import BaseHTTPRequestHandler

import ipaddr
import requests

from apikey import APIKEY
from whoisrws import network
from regrws.payload import net as NetPayload, error as ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s CIDR' % sys.argv[0]
    sys.exit(2)

net = ipaddr.IPNetwork(sys.argv[1])
url = 'http://whois.arin.net/rest/cidr/%s' % net
try:
    r = requests.get(url)
except requests.exceptions.RequestException as e:
    print 'ERROR:', e[0]
    sys.exit(1)
if r.status_code != requests.codes.ok:
    print r.status_code, BaseHTTPRequestHandler.responses[r.status_code][1]
    sys.exit(1)
else:
    whoispayload = network.parseString(r.content)

nethandle = whoispayload.handle
print '''
Net name: %s
Net handle: %s
''' % (whoispayload.name, nethandle)
url = 'https://reg.arin.net/rest/net/%s' % nethandle
qargs = {'apikey': APIKEY}
try:
    r = requests.get(url, params=qargs)
except requests.exceptions.RequestException as e:
    print 'ERROR:', e[0]
    sys.exit(1)
if r.status_code != requests.codes.ok:
    errorpayload = ErrorPayload.parseString(r.content)
    print r.status_code, errorpayload.message[0]
    sys.exit(1)
else:
    netpayload = NetPayload.parseString(r.content)
    print '''
CIDR length: %s
Address range: %s - %s
Registration date: %s
Description: %s
''' % (netpayload.netBlocks[0].netBlock[0].cidrLength[0],
       netpayload.netBlocks[0].netBlock[0].startAddress[0],
       netpayload.netBlocks[0].netBlock[0].endAddress[0],
       netpayload.registrationDate[0],
       netpayload.netBlocks[0].netBlock[0].description[0])

    if netpayload.customerHandle:
        print 'Customer handle: %s' % netpayload.customerHandle[0]
    elif netpayload.orgHandle:
        print 'Org handle: %s' % netpayload.orgHandle[0]

    # for poclink in netpayload.pocLinks:
    #     print poclink.pocLinkRef
