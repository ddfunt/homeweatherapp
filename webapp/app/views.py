# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm
from .forms import ExampleForm, LoginForm
from .models import Record, Day

import json

VALIDATION_KEY = 'abcd'

def validate_user(data):
	if 'signature' in data.keys():
		if VALIDATION_KEY == data['signature']:
			return data
		else:
			return "Unauthorized upload"
	else:
		return "Invalid input data"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/events', methods=['POST'])
def events():
	event_data = json.loads(request.json)
	checked_data = validate_user(event_data)
	return str(checked_data)
