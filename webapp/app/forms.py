# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from wtforms import Form, TextField, TextAreaField, DateTimeField, PasswordField
#from wtforms import Required

class ExampleForm(Form):
	title = TextField('Título', )
	content = TextAreaField('Conteúdo')
	date = DateTimeField('Data', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField('Usuário', )
	password = PasswordField('Senha', )
