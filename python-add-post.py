import flask
from flask import request, jsonify
import json

def main():
    if not request.json:
        abort(400)
    jsonBody = request.json['numbers']
    number1 = int(jsonBody[0]['number1'])
    number2 = int(jsonBody[1]['number2'])
    return (jsonify({'total': number1 + number2}), 200)

