import flask, flask.views
from flask import request, url_for
import datetime
from database import Challenges,db,UserChallengeJoin
from flask import session

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeCreate.html')

	def post(self):
		print "createChallenge"
		print session['email']
		title= request.form['title']
		print 'titl'
		details = request.form['details']
		print 'det'
		level = request.form['level']
		print 'level'
		startTime = datetime.date.today()
		endTime = datetime.date.today() + datetime.timedelta(days=5)
		print "comes here"
		chl = Challenges(challengeName = title,createdEmail = session['email'], description = details, challengeLevel = "level", createdTime = startTime, startTime = startTime, endTime = endTime)
		print chl
		db.session.add(chl)
		db.session.commit()
		chj = UserChallengeJoin(email = session['email'], challengeId = chl.challengeId, status = 'created')
		db.session.add(chj)
		db.session.commit()
		message = "Challenge created successfully!"
		return flask.render_template('challengeCreate.html')