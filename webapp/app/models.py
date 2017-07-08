# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

#class Day(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    records = db.relationship('Record', backref='day',
#                                lazy='dynamic')
#    date = db.Column(db.DateTime)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))
    temp1 = db.Column(db.Float)
    temp2 = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    light_1 = db.Column(db.Integer)
    light_2 = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                print(key, value)
                if key == 'light':
                    self.light_1 = value[0]
                    self.light_2 = value[1]
                else:
                    setattr(self, key, value)

    def __repr__(self):
        return '{}{}'.format(self.temp1, self.temp2)