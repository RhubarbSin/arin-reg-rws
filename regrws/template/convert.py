import re

class DictFromTemplate(object):

    """Method object for converting a template to a dict."""

    _regex = re.compile(r'\d\d\.(.*):(.*)')

    def __init__(self, template):
        """Return a DictFromTemplate object that will convert the
        template string to a dict.
        """

        self.template = template
        self.parsed_template = {}

    def run(self):
        """Return dict containing parsed contents of template string.

        All dict item values are lists because template field labels
        (used for dict keys) can be repeated.
        """

        for line in self.template:
            match = self._regex.match(line)
            if match:
                self._process(match)
        return self.parsed_template

    def _process(self, m):
        # Create/modify dict item
        key = m.group(1).strip()
        value = m.group(2).strip()
        if key in self.parsed_template:
            self.parsed_template[key].append(value)
        else:
            self.parsed_template[key] = [value]
