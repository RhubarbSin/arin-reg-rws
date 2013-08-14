import re

class DictFromTemplateFile(object):

    """Method object for converting a template to a dict."""

    _regex = re.compile(r'\d\d\.(.*):(.*)')

    def __init__(self, filename):
        self.filename = filename
        self.parsed_template = {}

    def run(self):
        """Return dict containing parsed contents of template file."""

        with open(self.filename, 'r') as fh:
            for line in fh:
                match = self._regex.match(line)
                if match:
                    self._process(match)
        return self.parsed_template

    def _process(self, m):
        # Create/modify dict item, assigning value as list instead of
        # str if key is encountered more than once.
        key = m.group(1).strip()
        value = m.group(2).strip()
        if key in self.parsed_template:
            if isinstance(self.parsed_template[key], str):
                self.parsed_template[key] = [self.parsed_template[key]]
            self.parsed_template[key].append(value)
        else:
            self.parsed_template[key] = value
