import flask, flask.views

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return "Create a challenge"