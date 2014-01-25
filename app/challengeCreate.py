import flask, flask.views
from flask import request, url_for
from Kwest import Challenges
from datetime import datetime

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeCreate.html')

	def post(self):
		print("Entered")
		title= request.form['title']
		details = request.form['details']
		endTime = datetime.date.today()+5 
		level = request.args.get['level']
		chl = Challenges(challengeName = title, description = details, challengeLevel = "level", createdTime = datetime.date.today(), startTime = datetime.date.today(), endTime = datetime.date.today() + 5)
		db.session.add(chl)
		db.session.commit()
		message = "Challenge created successfully!"
		return flask.render_template('challengeCreate.html')