import flask
from flask import request, jsonify


def main():
    number1 = int(request.args.get('number1'))
    number2 = int(request.args.get('number2'))
    return (jsonify({'total': number1 + number2}), 200)
