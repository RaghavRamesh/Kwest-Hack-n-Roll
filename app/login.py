import flask, flask.views
import requests
import database

class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template('login.html')

	def post(self):
		
		success = database.User.loginCheck(request.form['username'],request.form['password'])
		print success
		if(success):
			return flask.render_template('profile.html')
		else:
			return flask.render_template('login.html')