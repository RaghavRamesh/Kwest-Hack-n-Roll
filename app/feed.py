import flask, flask.views

class Feed(flask.views.MethodView):
	def get(self):
		return flask.render_template('feed.html')

	def acceptChallenge(self, id):
		print "acceptChallenge"

	def upvoteChallenge(self, id):
		print "upvoteChallenge"

	def downvoteChallenge(self, id):
		print "downvoteChallenge"