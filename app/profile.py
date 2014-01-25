import flask, flask.views

class Profile(flask.views.MethodView):
	def get(self):

		return flask.render_template('profile.html')