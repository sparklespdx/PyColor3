import serial


class SerialAPI:
    def __init__(self, config):
        self.device = config['SERIAL_DEVICE']
        self.conn = None

    def connect(self):
        self.conn = serial.Serial(self.device)
        return self.conn
