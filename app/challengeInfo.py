import flask, flask.views

class ChallengeInfo(flask.views.MethodView):
	def get(self):
		return "The Challenge page"