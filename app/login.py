import flask, flask.views
import requests
import database

class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template('login.html')

	def post(self):
		user = database.Users(email = request.form['username'],password = request.form['password'])
		success = database.User.loginCheck(user)
		if(success):
			return flask.render_template('profile.html')
		else:
			return flask.render_template('login.html')