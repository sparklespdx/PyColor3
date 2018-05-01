from flask import Blueprint, current_app, jsonify
from pycolor3.serial_api import SerialAPI


icolorapp = Blueprint('icolorapp', __name__)


@icolorapp.route('/play/<int:input>', methods=['PUT'])
def play_show(input):
    with SerialAPI(current_app.config) as s:
        try:
            s.play_show(input)
        except (ValueError, TypeError) as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'played show ' + str(input)}), 200


@icolorapp.route('/brightness/<int:input>', methods=['PUT'])
def brightness(input):
    with SerialAPI(current_app.config) as s:
        try:
            s.set_brightness(input)
        except (ValueError, TypeError) as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'set brightness level ' + str(input)}), 200
