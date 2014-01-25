import flask, flask.views

class Shop(flask.views.MethodView):
	def get(self):
		return "Shop!!!"