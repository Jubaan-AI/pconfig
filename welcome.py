
"""
testing that the python env: pconfig works
"""

import os
import sys


print("Virtual Environment:", os.path.basename(sys.prefix))
print("Virtual Environment working dir:", os.environ.get('VIRTUAL_ENV', 'Not in a virtual environment'))
print(f"working on: {os.name}")
