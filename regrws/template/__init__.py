import re

def dict_from_template_file(filename):
    template_re = re.compile(r'\d\d\.(.*):(.*)')
    template_input = {}
    with open(filename, 'r') as fh:
        for line in fh:
            m = template_re.match(line)
            if m:
                key = m.group(1).strip()
                value = m.group(2).strip()
                if key in template_input:
                    if isinstance(template_input[key], str):
                        template_input[key] = [template_input[key]]
                    template_input[key].append(value)
                else:
                    template_input[key] = value
    return template_input
