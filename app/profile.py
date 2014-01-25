import flask, flask.views

class Profile(flask.views.MethodView):
	def get(self):
		return "User profile page"