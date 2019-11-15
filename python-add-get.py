import flask
from flask import request, jsonify


def main():
    query_parameters = request.args
    if 'number1' in request.args:
        number1 = int(request.args.get('number1'))
    else:
        return 'Error: No number1 field provided. Please specify an number1.'

    if 'number2' in request.args:
        number2 = int(request.args.get('number2'))
    else:
        return 'Error: No number2 field provided. Please specify an number2.'

    return (jsonify({'total': number1 + number2}), 200)
