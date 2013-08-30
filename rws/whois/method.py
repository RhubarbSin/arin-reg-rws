from __future__ import absolute_import

from rws import restful
from rws.whois.payload import net

class Cidr(restful.Method):

    payload = net
    url = 'http://whois.arin.net/rest/cidr/'

    def __init__(self, session, cidr):
        super(Cidr, self).__init__(session, 'get')
        self.url += cidr
