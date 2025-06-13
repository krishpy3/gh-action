import os
import sys
import logging

if os.getenv('a'):
    logging.info('Got Env')
    sys.exit(0)
else:
    logging.error('No env')
    sys.exit(1)

    