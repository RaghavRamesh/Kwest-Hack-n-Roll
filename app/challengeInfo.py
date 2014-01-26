import flask, flask.views
import datetime	
import database
from flask import request

class ChallengeInfo(flask.views.MethodView):
	def get(self,challengeId):
		basic = self.getBasic(challengeId)
		cmts = self.getComments(challengeId)
		ans = self.getAnswers(challengeId)
		challengeDict = dict()
		challengeDict.update( {'basic': basic, 'cmts':cmts, 'ans':ans } )
		challengeId = challengeId
		# print challengeDict
	
		# for r in challengeDict['basic']:
		# 	print r.description
		# print basic

		return flask.render_template('challengeInfo.html', challengeDict=challengeDict)

	def acceptChallenge(self, challengeId):
		print "acceptChallenge"
		email = request.args.get('username')
		chl = UserChallengeJoin(challengeId = challengeId, email = email, status = 'accepted')
		db.session.add(chl)
		db.session.commit()
		message = "You have accepted this challenge"

	def upvoteChallenge(self):
		challenge = Challenges.query.get(challengeId = self.challengeId)
		challenge.votes = challenge.votes + 1
		db.session.commit()


	def downvoteChallenge(self):
		challenge = Challenges.query.get(challengeId = self.challengeId)
		challenge.votes = challenge.votes - 1
		db.session.commit()

	def commentChallenge(self, challengeId):
		desc = request.form['description']
		postTime = datetime.datetime.now()
		email = session['email']

		commentChallenge = database.commentChallenge(description = desc, postTime = postTime, email = email, challengeId = challengeId)
		db.session.add(chl)
		db.session.commit()
		message = "comment posted successfully!"
		return flask.render_template('challengInfo.html')

	def uploadAnswer(self):
		print "uploadAnswer"

	def getBasic(self, challengeId):
		resultSet = database.Challenges.query.filter(database.Challenges.challengeId == challengeId).all()
		return resultSet

	def getComments(self, challengeId):
		resultSet = database.ChallengeComment.query.filter(database.ChallengeComment.challengeId == challengeId).all()
		return resultSet

	def getAnswers(self, challengeId):
		resultSet = database.Answers.query.filter(database.Answers.challengeId == challengeId).all()
		return resultSet

	def getOwner(self, challengeId):
		user = database.Challenges.query.get(database.Challenges.challengeId == request.args.get('id'))