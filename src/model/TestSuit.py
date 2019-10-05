# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class TestSuit(db.Model):
    id = db.Column(db.String, primary_key=True)
    test_suit_name = db.Column(db.String, unique=True, nullable=False)

def add_testsuit(suit_name):
	db.session.add(TestSuit(id=str(uuid.uuid1()), test_suit_name=suit_name))
	db.session.commit()

