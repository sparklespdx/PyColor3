# PyColor3: Flask API for controlling Phillips Color Kinetics IColor3

import logging
import os
import sys

from flask import Flask

from pycolor3.config import BaseConfig
from pycolor3.controllers import icolorapp

dev = False
if os.environ.get('ENVIRONMENT') == 'development':
    dev = True

# Logging setup
logger = logging.getLogger('pycolor3')
if dev:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s %(name)s: %(levelname)s - %(message)s', "[%d/%b/%Y %H:%M:%S]")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Initialize application
app = Flask(__name__)
app.register_blueprint(icolorapp)
app.config.from_object(BaseConfig())
