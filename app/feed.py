import flask, flask.views

class Feed(flask.views.MethodView):
	def get(self):
		return flask.render_template('feed.html')