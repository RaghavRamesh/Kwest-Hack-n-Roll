import flask, flask.views
from flask import request, url_for
import datetime
import database

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeCreate.html')

	def post(self):
		print "createChallenge"

		title= request.form['title']
		details = request.form['details']
		level = request.form['level']
		startTime = datetime.date.today()
		endTime = datetime.date.today() + datetime.timedelta(days=5)
		print "comes here"
		chl = database.Challenges(challengeName = title, description = details, challengeLevel = "level", createdTime = startTime, startTime = startTime, endTime = endTime)
		print chl
		db.session.add(chl)
		db.session.commit()
		message = "Challenge created successfully!"
		return flask.render_template('challengeCreate.html')