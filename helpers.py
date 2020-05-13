import json
from flask import Response


class Helpers:
    STATUS_OK = 200
    STATUS_BAD_REQUEST = 400
    STATUS_SERVER_ERROR = 500

    @staticmethod
    def standard_response(status, payload):
        json_data = json.dumps({
            'response': payload
        }, sort_keys=True, indent=4, separators=(',', ': '))
        resp = Response(json_data, status=status, mimetype='application/json')
        return resp

    @staticmethod
    def success(payload):
        return Helpers.standard_response(Helpers.STATUS_OK, payload)

    @staticmethod
    def error(status, error_info):
        return Helpers.standard_response(status, {
            'error': error_info
        })

    @staticmethod
    def bad_request(error_info):
        return Helpers.error(Helpers.STATUS_BAD_REQUEST, error_info)

    @staticmethod
    def validate_input(hour: int, minute: int):
        if type(hour) != int or type(minute) != int:
            return False

        if 0 <= hour <= 24 and 0 <= minute <= 60:
            hour = hour % 12
            minute = minute % 60
            return hour, minute
        else:
            return False
