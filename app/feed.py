import flask, flask.views
from database import Challenges, Users
import database
from sqlalchemy import desc

class Feed(flask.views.MethodView):
	def get(self):
		challengesPosted = Challenges.query.order_by(desc(Challenges.createdTime)).all()
		chalDict = []
		
		chalDict=dict()
		indiList=[]
		# mailList=[]
		# nameList=[]
		# levelList=[]
		# votesList=[]
		# endTimeList=[]
		# acceptedNumberList=[]
		for eachChallenge in challengesPosted:
			name= eachChallenge.challengeName
			print name
			level= eachChallenge.challengeLevel 
			votes = eachChallenge.votes
			description = eachChallenge.description
			endTime = eachChallenge.endTime
			mail= eachChallenge.createdEmail
			#print mail
			getUsers = database.Users.query.get(mail)
			#print getUsers
			username=getUsers.userName
			acceptedNumber = database.UserChallengeJoin.query.filter_by(challengeId=eachChallenge.challengeId, status='accepted').count()
			individual=dict()
			individual.update({'name':name,
								'level':level,
								'votes':votes,
								'endTime':endTime,
								'mail':mail,
								'description':description,
								'username': username,
								'acceptedNumber':acceptedNumber,
								'challengeId':eachChallenge.challengeId
				})
			# nameList.append(name)
			# levelList.append(level)
			# votesList.append(votes)
			# endTimeList.append(endTime)
			# mailList.append(mail)
			# acceptedNumberList.append(acceptedNumber)
			indiList.append(individual)
		# chalDict=dict()
		# chalDict.update({'names':nameList,
		# 				'levels':levelList,
		# 				'votes':votesList,
		# 				'endTime':endTimeList,
		# 				'mail':mailList,
		# 				'acceptedNumber':acceptedNumberList})
		
		return flask.render_template('feed.html', indiList=indiList)

	def getHigh(self):
		challengesPosted = database.Challenges.query(),order_by(desc(Challenges.votes)).all()
		chalDict = []
		nameList=[]
		levelList=[]
		votesList=[]
		endTimeList=[]
		acceptedNumberList=[]
		for eachChallenge in challengesPosted:
			name= eachChallenge.challengeName
			level= eachChallenge.challengeLevel 
			votes = eachChallenge.votes
			endTime = eachChallenge.endTime
			print eachChallenge.challengeId
			acceptedNumber = database.UserChallengeJoin.query.filter_by(challengeId=eachChallenge.challengeId.str(), status='accepted').count()
			nameList.append(name)
			levelList.append(level)
			votesList.append(votes)
			endTimeList.append(endTime)
			acceptedNumberList.append(acceptedNumber)
		chalDict.update({'names':nameList,
						'levels':levelList,
						'votes':votesList,
						'endTime':endTimeList,
						'acceptedNumber':acceptedNumberList})
		print chalDict
		return flask.render_template('feed.html', chalDict)



	def upvoteChallenge(self, id):
		challengeNeeded=database.Challenges.query.get(challengeId=id)
		votenumber=challengeNeeded.votes
		votenumber+=1
		# stmt = update(Challenges).where(Challenges.challengeId==id).\
		# values(Challenges.votes=votenumber)
		db.session.commit()
		print "upvoteChallenge"

	def downvoteChallenge(self, id):
		challengeNeeded=database.Challenges.query.get(challengeId=id)
		votenumber=challengeNeeded.votes
		votenumber-=1
		# stmt = update(Challenges).where(Challenges.challengeId==id).\
		# values(Challenges.votes=votenumber)
		db.session.commit()
		print "downvoteChallenge"