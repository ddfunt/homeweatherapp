# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from flask_pymongo import PyMongo
from flask_login import LoginManager


app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app) #flask-bootstrap
db = SQLAlchemy(app) #flask-sqlalchemy

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'



from app import views, models, configuration

if not os.path.isfile(configuration.Config.SQLALCHEMY_DATABASE_URI):
    db.create_all()
    db.session.commit()
