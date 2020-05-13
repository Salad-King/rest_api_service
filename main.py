from flask import Flask, redirect, request
from helpers import Helpers
import logging

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/clock_angles')


@app.route('/clock_angles', methods=['GET', 'POST'])
def calculate_angles():
    """
    returns the angle between the hour hand and the minute hand

    Request to be sent should be POST and should have a json payload containing
    ifo on location of hour hand and minute hand
    """
    if request.method == 'GET':
        return Helpers.bad_request('GET request received. Expected POST with application/json body')

    else:
        request_data = request.get_json()
        result = Helpers.validate_input(request_data['hour_hand'], request_data['minute_hand'])
        if result:
            hour, minute = result

            hour_angle = 0.5 * (hour * 60 + minute)
            minute_angle = 6 * minute

            angle = abs(hour_angle - minute_angle)

            return Helpers.success(min(360 - angle, angle))
        else:
            return Helpers.bad_request("Invalid arguments sent. "
                                       "Expected integer values between 0 and 24 for hour and "
                                       "between 0 and 60 for minute...")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
