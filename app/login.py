import flask, flask.views

class Login(flask.views.MethodView):
	def get(self):
		return "Login comes here"