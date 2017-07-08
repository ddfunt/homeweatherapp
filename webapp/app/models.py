# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    addresses = db.relationship('Record', backref='day',
                                lazy='dynamic')

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))
    date = db.Column(db.DateTime)

