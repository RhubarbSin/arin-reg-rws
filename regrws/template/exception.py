from __future__ import absolute_import

from regrws import restful

class ParseError(restful.RegRwsError):

    def __init__(self, *args):
        super(ParseError, self).__init__(*args)
