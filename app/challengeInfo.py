import flask, flask.views
import datetime	

class ChallengeInfo(flask.views.MethodView):
	def get(self):
		basic = self.getBasic()
		cmts = self.getComments()
		ans = self.getAnswers()
		challengeDict = dict()
		challengeDict.update( {'basic': basic, 'cmts':cmts, 'ans':ans}
		return flask.render_template('challengeInfo.html', challengeDict= challengeDict)

	def acceptChallenge(self):
		print "acceptChallenge"
		email = request.args.get('username')
		chl = UserChallengeJoin(challengeId = self.challengeId,email = email, status =  )
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
		resultSet = Challenges.query.filter(Challenges.challengeId== self.challengeId)
		return resultSet

	def getComments(self):
		resultSet = ChallengeComment.query.filter(ChallengeComment.challengeId = self.challengeId)
		return resultSet

	def getAnswers(self):
		resultSet = Answers.query.filter(Answers.challengeId = self.challengeId)
		return resultSet
	def getOwner(self):
		user = Challenges.query.get(Challenges.challengeId== self.challengeId )