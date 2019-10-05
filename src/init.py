# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api

from controller.TestSuit import TestSuit
from model.TestSuit import db as TestSuitDB

app = Flask(__name__)

api = Api(app)
api.add_resource(TestSuit, '/testsuit')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite'
TestSuitDB.init_app(app)


if __name__ == '__main__':
	with app.app_context():
		TestSuitDB.create_all()
	app.run(debug=True)