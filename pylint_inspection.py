"""
This module is used for checking
the project code for compliance with PEP8.

"""


import pylint.lint


pylint_opts = [
    '--ignore-imports=yes',
    # '--disable=C0114',
    # '--disable=C0115',
    # '--disable=C0116',
    '__init__.py',
    'pylint_inspection.py',
    'main.py',
]
pylint.lint.Run(pylint_opts)
