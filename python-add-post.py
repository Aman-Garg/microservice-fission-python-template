import flask
from flask import request, jsonify
import json


def main():
    jsonBody = request.json['numbers']
    number1 = int(jsonBody[0]['number'])
    number2 = int(jsonBody[1]['number'])
    return (jsonify({'total': number1 + number2}), 200)
