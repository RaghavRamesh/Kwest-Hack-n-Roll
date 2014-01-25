import flask, flask.views
# from database import *

class Profile(flask.views.MethodView):
	def get(self):
		# created = 
		# accepted = get from the db
		# completed = get from the db
		# xp = get from the db
		# while (there are tuples):
		# 	pending.title		
		# 	pending.timeLeft
		return flask.render_template('profile.html')

		