import flask, flask.views

class ChallengeInfo(flask.views.MethodView):
	def get(self):

		return flask.render_template('challengeInfo.html')

	def acceptChallenge(self):
		print "acceptChallenge"

	def upvoteChallenge(self):
		print "upvoteChallenge"

	def downvoteChallenge(self):
		print "downvoteChallenge"

	def commentChallenge(self):
		print "commentChallenge"

	def uploadAnswer(self):
		print "uploadAnswer"