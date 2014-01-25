import flask, flask.views

class ChallengeInfo(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeInfo.html')