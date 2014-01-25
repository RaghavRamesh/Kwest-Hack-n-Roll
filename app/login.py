import flask, flask.views
from flask import request,session
import requests
from database import Users
from profile import Profile

class Login(flask.views.MethodView):
	def __init__(self):
		self.users = Users()
		self.profile = Profile()

	def get(self):
		if(session['email']):
			return self.profile.get()
		else:
			return flask.render_template('login.html')

	def post(self):
		
		print request.form['username']
		session['email'] = request.form['username']
		success = self.users.loginCheck(request.form['username'],request.form['password'])
		print success
		if(success):
			#r = requests.get('http://localhost/profile')
			return self.profile.get()

			#Response(
			#	r.text,
			#	status=r.status_code,
			#	content_type=r.headers['content-type'],
			#	)
		else:
			return flask.render_template('login.html')