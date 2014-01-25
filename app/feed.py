import flask, flask.views
import database
from sqlalchemy import desc

class Feed(flask.views.MethodView):
	def get(self):
		challengesPosted = database.Challenges.query(),order_by(desc(Challenges.createdTime)).all()
		name= challengesPosted.challengeName
		level= challengesPosted.challengeLevel 
		chalDict = [{}]
		return flask.render_template('feed.html')

	def acceptChallenge(self, id):
		print "acceptChallenge"

	def upvoteChallenge(self, id):
		print "upvoteChallenge"

	def downvoteChallenge(self, id):
		print "downvoteChallenge"