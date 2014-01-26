import flask, flask.views
from flask import request,session

class Logout(flask.views.MethodView):
	def get(self):
		session.pop('email', None)
		return flask.render_template('login.html')