import os

class BaseConfig:

    SERIAL_DEVICE = os.environ.get('PYCOLOR3_SERIAL_DEVICE')
