# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from model.TestSuit import add_testsuit

Jobs = {}

class TestSuit(Resource):
    def get(self):
        return {}

    def post(self):
        Jobs['userId'] = request.form['userId']
        return {'userId': Jobs['userId']}

