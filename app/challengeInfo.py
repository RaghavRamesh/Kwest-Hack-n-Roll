import flask, flask.views
import datetime	
import database
from flask import request

class ChallengeInfo(flask.views.MethodView):
	def get(self):
		basic = self.getBasic()
		cmts = self.getComments()
		ans = self.getAnswers()
		challengeDict = dict()
		challengeDict.update( {'basic': basic, 'cmts':cmts, 'ans':ans } )
		print challengeDict
		return flask.render_template('challengeInfo.html', challengeDict=challengeDict)

	def acceptChallenge(self):
		print "acceptChallenge"
		email = request.args.get('username')
		chl = UserChallengeJoin(challengeId = self.challengeId, email = email, status = 'accepted')
		db.session.add(chl)
		db.session.commit()
		message = "You have accepted this challenge"

	def upvoteChallenge(self):
		print "upvoteChallenge"

	def downvoteChallenge(self):
		print "downvoteChallenge"

	def commentChallenge(self):
		print "commentChallenge"

	def uploadAnswer(self):
		print "uploadAnswer"

	def getBasic(self):
		resultSet = database.Challenges.query.filter(database.Challenges.challengeId == request.args.get('id')).all()
		return resultSet

	def getComments(self):
		resultSet = database.ChallengeComment.query.filter(database.ChallengeComment.challengeId == request.args.get('id')).all()
		return resultSet

	def getAnswers(self):
		resultSet = database.Answers.query.filter(database.Answers.challengeId == request.args.get('id')).all()
		return resultSet

	def getOwner(self):
		user = database.Challenges.query.get(database.Challenges.challengeId == request.args.get('id'))