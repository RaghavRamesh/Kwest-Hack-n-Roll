import flask, flask.views

class ChallengeCreate(flask.views.MethodView):
	def get(self):
		return flask.render_template('challengeCreate.html')

	def post(self):
		
		message = "Challenge created successfully!"
		return flask.render_template('challengeCreate.html')