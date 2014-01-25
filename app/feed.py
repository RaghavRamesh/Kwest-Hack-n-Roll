import flask, flask.views

class Feed(flask.views.MethodView):
	def get(self):
		return "This is the news feed"