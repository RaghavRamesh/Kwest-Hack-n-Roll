import flask, flask.views
from flask import session
# from database import *
from app import database

class Profile(flask.views.MethodView):
	def get(self):
		#name = 
		# Level = 
		#Experience
		#money
		# created = 
		# accepted = get from the db
		# completed = get from the db
		# xp = get from the db
		# while (there are tuples):
		# 	pending.title		
		# 	pending.timeLeft
		#	pending.id
		result = database.UserChallengeJoin.query.all()
		to_do = []
		counter = 0
		accepted = 0
		for check in result:
			if check.email ==session['email']:
				if check.status=='created':
					counter+=1
				if check.status=='accepted':
					accepted+=1
					todo.append(check.challengeId)
		userStat = database.Users.query.get(session['email'])
		name = userStat.userName
		level = userStat.userLevel
		xp = userStat.experience
		money = userStat.money
		xprequired = userStat.userLevel * 1000

		pending_title = []
		pending_timeLeft = []
		won = 0
		for chalId in to_do:
			checkChallenges = database.Challenges.query.get(chalId)
			pending_title.append(checkChallenges.challengeName)	
			pending_timeLeft.append(checkChallenges.endTime.strftime("%A, %d. %B %Y %I:%M%p"))
 

		#won- challenge id = sub query  and answer.status = 1
		checkAnswers = database.Answers.query.all()
		for ans in checkAnswers:
			if (ans.challengeId in to_do) and (ans.status == True):
				won+=1
		profileDict = dict()
		profileDict.update( {'name': name,  
							'level':level, 
							'xp':xp,
							'xprequired':xprequired,
							'money':money,
							'to_do': to_do,
							'pending_title': pending_title,
							'pending_timeLeft': pending_timeLeft,
							'created': counter,
							'accepted': accepted,
							'completed':won	} )

		return flask.render_template('profile.html', profileDict=profileDict)


	def post(self):
		print profileDict['name']
		return flask.render_template('profile.html', profileDict=profileDict)

