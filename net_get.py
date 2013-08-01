#!/usr/bin/env python 

import sys
import urllib2
import logging
from BaseHTTPServer import BaseHTTPRequestHandler

import pyxb
import ipaddr

from apikey import APIKEY
from whoisrws import network
from regrws import NetPayload, ErrorPayload

if len(sys.argv) != 2:
    print 'Usage: %s CIDR' % sys.argv[0]
    sys.exit(2)

log = logging.getLogger('pyxb.binding.content')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

net = ipaddr.IPNetwork(sys.argv[1])
url = 'http://whois.arin.net/rest/cidr/%s' % net
try:
    response = urllib2.urlopen(url).read()
except urllib2.HTTPError as exc:
    print exc.code, BaseHTTPRequestHandler.responses[exc.code][1]
    sys.exit(1)
else:
    whoispayload = network.CreateFromDocument(response)

nethandle = whoispayload.handle[0]
print '''
Net name: %s
Net handle: %s
''' % (whoispayload.name[0], nethandle)
url = 'https://reg.arin.net/rest/net/%s?apikey=%s' % (nethandle, APIKEY)
try:
    response = urllib2.urlopen(url).read()
except urllib2.HTTPError as exc:
    errorpayload = ErrorPayload.CreateFromDocument(exc.read())
    print errorpayload.message[0]
    sys.exit(1)
else:
    netpayload = NetPayload.CreateFromDocument(response)
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

    netpayload.comment.append(pyxb.BIND(pyxb.BIND('Comment 1', number=1)))

    # print netpayload.toDOM().toprettyxml()
