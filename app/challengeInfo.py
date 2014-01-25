import flask, flask.views

class ChallengeInfo(flask.views.MethodView):
	def get(self):

		return flask.render_template('challengeInfo.html')

	def acceptChallenge(self):
		print "acceptChallenge"
		id = request.args.get('id')
		name = request.args.get('name')
		email = request.args.get('username')
		description = request.args.get('description')
		level = request.args.get('level')
		createdTime = request.args.get('createdTime')
		startTime = request.args.get('startTime')
		endTime = request.args.get('endTime')
		votes = request.args.get('votes')
		chl = Challenges(challengeId = id, challengeName = name, createdEmail = email, startTime = startTime, createdTime = createdTime, endTime = endTime, votes = votes)
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