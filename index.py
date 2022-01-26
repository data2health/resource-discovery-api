""" 
Mygene Web Server Entry Point
    Examples:
>>> python index.py
>>> python index.py --debug
>>> python index.py --port=8000
"""

import config
#from biothings.web.index_base import main
from biothings.web.launcher import main
from web.handlers import EXTRA_HANDLERS

if __name__ == "__main__":
    main(EXTRA_HANDLERS)