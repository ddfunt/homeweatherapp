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
import datetime
from datetime import timezone
import logging

# CONSTANTS...move to config file
VALIDATION_KEY = 'abcd'
LASTDATA = 'NOTHING YET'


logger = logging.getLogger(__file__)

def validate_user(data):
	if 'signature' in data.keys():
		if VALIDATION_KEY == data['signature']:
			return data, True
		else:
			return "Unauthorized upload", False
	else:
		return "Invalid input data", False

def pa_to_mmhg(pressure):
	pa_per_atm = 9.80665E4
	mmhg_per_atm = 760

	return (pressure / pa_per_atm) * mmhg_per_atm

def utc_to_local(utc_dt, tz=None):
	if not tz:
		tz = datetime.timezone(datetime.timedelta(hours=-4), name='MYTZ')
	return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=tz)

def celcius_to_faren(deg_c):
	return (deg_c * 9 / 5) + 32

def json_to_db(data):

	record = Record(**data)
	logger.info('STORING NEW DATA')
	db.session.add(record)

	db.session.commit()

@app.route('/')
def index():

	data = Record.query.all()
	temp1, dates, temp2, humidity, pressure, light1, light2 = [], [], [], [], [], [], []
	for entry in data:
		temp1.append(celcius_to_faren(entry.temp1))
		dates.append(utc_to_local(entry.datetime).strftime("%Y-%m-%d %H:%M:%S"))
		temp2.append(celcius_to_faren(entry.temp2))
		humidity.append(entry.humidity)
		pressure.append(pa_to_mmhg(entry.pressure))
		light1.append(entry.light_1)
		light2.append(entry.light_2)

	return render_template('index.html', display=LASTDATA, temp1_data=temp1, dates=dates,
						   temp2_data = temp2,
						   humidity_data = humidity,
						   light1_data=light1,
						   light2_data=light2,
						   pressure_data=pressure)

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


