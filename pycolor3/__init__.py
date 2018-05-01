# PyColor3: Flask API for controlling Phillips Color Kinetics IColor3
# http://www.colorkinetics.com/support/userguides/iPlayer_3_UG.pdf

import logging
import os
import sys

from flask import Flask

from pycolor3.config import BaseConfig

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

#blueprints = [samlapp, problemapp, hostapp, vulnapp, vulndefapp, miscapp]
#for bp in blueprints:
#    app.register_blueprint(bp)

app.config.from_object(BaseConfig())
