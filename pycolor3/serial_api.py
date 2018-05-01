import serial
from functools import wraps


class IColor3SerialError(Exception):
    pass


class SerialAPI:
    def __init__(self, config):
        self.conn = serial.Serial()

        # Settings for iColor3
        self.conn.baudrate = 9600
        self.conn.bytesize = 8
        self.conn.parity = 'N'
        self.conn.stopbits = 1

        # Configured via Flask app
        self.conn.timeout = config['SERIAL_TIMEOUT']
        self.conn.port = config['SERIAL_DEVICE']

    def __enter__(self):
        self.conn.open()
        return self

    def __exit__(self, *args):
        self.conn.close()

    def send_command(self, prefix, input):

        if not self.conn.is_open:
            raise IColor3SerialError('Serial connection is not open.')

        if not isinstance(input, int):
            raise TypeError

        if input > 255 or input < 0:
            raise ValueError('Invalid input value: ' + str(input))

        command = prefix + input.upper()
        self.conn.write(command.encode())

        response = self.conn.read(5)
        if not response:
            return False

        response = response.decode()
        if response.replace('Y', 'X') != command:
            raise IColor3SerialError(response)

        return True

    def play_show(self, show_number):
        return self.send_command("X04", hex(show_number)[2:].zfill(2))

    def turn_off(self):
        return self.send_command("X01", "00")

    def set_brightness(self, brightness):
        return self.send_command("X02", hex(brightness)[2:].zfill(2))
