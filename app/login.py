import flask, flask.views
from flask import request
from database import Users

class Login(flask.views.MethodView):
	def __init__(self):
		self.users = Users()

	def get(self):
		return flask.render_template('login.html')

	def post(self):
		
		print request.form['username']
		success = self.users.loginCheck(request.form['username'],request.form['password'])
		print success
		if(success):
			return flask.render_template('profile.html')
		else:
			return flask.render_template('login.html')