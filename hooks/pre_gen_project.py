import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)


if not type({{ cookiecutter.line_length }}) == int:
    print('ERROR: The line length must be a number')
    sys.exit(1)

if not {{ cookiecutter.test }} and {{ cookiecutter.travis }}:
    print('ERROR: Cannot use continuous integration without unit tests')
