# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from .forms import ExampleForm, LoginForm
from .models import Record#, Day

import json

VALIDATION_KEY = 'abcd'

LASTDATA = 'NOTHING YET'


def validate_user(data):
	if 'signature' in data.keys():
		if VALIDATION_KEY == data['signature']:
			return data, True
		else:
			return "Unauthorized upload", False
	else:
		return "Invalid input data", False

@app.route('/')
def index():

	data = Record.query.all()
	temp1 = [entry.temp1 for entry in data]
	dates = [entry.datetime.strftime("%Y-%m-%d %H:%M:%S") for entry in data]
	temp2 = [entry.temp2 for entry in data]
	humidity = [entry.humidity for entry in data]
	light1 = [entry.light_1 for entry in data]
	light2 = [entry.light_2 for entry in data]

	return render_template('index.html', display=LASTDATA, temp1_data=temp1, dates=dates,
						   temp2_data = temp2,
						   humidity_data = humidity,
						   light1_data=light1,
						   light2_data=light2)

@app.route('/events', methods=['POST'])
def events():
	event_data = request.json
	if not isinstance(event_data, dict):
		event_data = json.loads(request.json)
	checked_data, valid = validate_user(event_data)
	globals()['LASTDATA'] = str(checked_data)
	if valid:
		json_to_db(checked_data)
	return str(checked_data)


def json_to_db(data):
	record = Record(**data)
	print(record)
	db.session.add(record)

	db.session.commit()