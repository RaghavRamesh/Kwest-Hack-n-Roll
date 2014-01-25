import flask, flask.views
from flask import request, url_for
from datetime import datetime

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeCreate.html')

	def post(self):
		print("Entered")
		title= request.form['title']
		details = request.form['details']
		level = request.args.get['level']
		startTime = datetime.date.today()
		endTime = datetime.date.today()+5 
		chl = Challenges(challengeName = title, description = details, challengeLevel = "level", createdTime = startTime, startTime = startTime, endTime = endTime)
		db.session.add(chl)
		db.session.commit()
		message = "Challenge created successfully!"
		return flask.render_template('challengeCreate.html')