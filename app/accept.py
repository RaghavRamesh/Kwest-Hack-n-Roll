import flask, flask.views
from flask import request, url_for
import datetime
import database
from flask import session
class Accept(flask.views.MethodView):
	def get(self,id):
		print("get")
		self.acceptChallenge()
		return HttpResponseRedirect(request.META['HTTP_REFERER'])

	def acceptChallenge(self):
		print "acceptChallenge"
		new_transaction=database.UserChallengeJoin()
		new_transaction.challengeId=id
		new_transaction.email=session['email']
		new_transaction.status='accepted'
		database.db.session.add(new_transaction)
		database.db.session.commit()
		print "acceptChallenge"
		return HttpResponseRedirect(request.META['HTTP_REFERER'])

	def post(self):
		return HttpResponseRedirect(request.META['HTTP_REFERER'])