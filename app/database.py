from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///..//test1.db'
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class ChallengeComment(db.Model):
	__tablename__="ChallengeComment"
	postTime = db.Column(db.DateTime)
	email = db.Column(db.String(50),db.ForeignKey('Users.email'))
	challengeId = db.Column(db.String, db.ForeignKey('Challenges.challengeId'),primary_key = True)
	commentid = db.Column(db.Integer, primary_key = True)
	description = db.Column(db.Text)
	
	def __init__(self,**kwargs):
		self.postTime = kwargs.get('postTime', datetime.datetime.now())
		self.email = kwargs.get('email')
		self.challengeId = kwargs.get('challengeId')
		self.commentId = kwargs.get('commentId')
		self.description = kwargs.get('description')


class Comments(db.Model):
	__tablename__="Comments"
	postTime = db.Column(db.DateTime)
	email = db.Column(db.String(50),db.ForeignKey('Users.email'))
	challengeId = db.Column(db.String, db.ForeignKey('Challenges.challengeId'),primary_key = True)
	commentId = db.Column(db.Integer, primary_key = True)
	description = db.Column(db.Text)
	answerId = db.Column(db.Integer, db.ForeignKey('Answers.answerId'),primary_key = True)

def __init__(self,**kwargs):
		self.postTime = kwargs.get('postTime', datetime.datetime.now())
		self.email = kwargs.get('email')
		self.challengeId = kwargs.get('challengeId')
		self.commentId = kwargs.get('commentId')
		self.answerId = kwargs.get('answerid')
		self.description = kwargs.get('description')


class Users(db.Model):
	__tablename__="Users"
	email = db.Column(db.String(50), primary_key = True)
	userName = db.Column(db.String(50))
	userLevel = db.Column(db.Integer)
	password = db.Column(db.String(100))
	experience = db.Column(db.Integer)
	money = db.Column(db.Integer)
	
	def __init__ (self, **kwargs):
		self.email = kwargs.get('email')
		self.userName = kwargs.get('userName')
		self.userLevel = kwargs.get('userLevel',1)
		self.password = kwargs.get('password')
		self.experience = kwargs.get('experience',0)
		self.money = kwargs.get('money',0)

	def loginCheck(self,mail,pas):
		return db.session.query(Users).filter_by(email = mail, password=pas).count()

class Answers(db.Model):
	__tablename__="Answers"
	status = db.Column(db.Boolean)
	email = db.Column(db.String(50), db.ForeignKey('Users.email'))
	challengeId = db.Column(db.String(50), db.ForeignKey('Challenges.challengeId'),  primary_key=True)
	description = db.Column(db.Text)
	answerId = db.Column(db.Integer, primary_key=True)
	postTime = db.Column(db.DateTime)

	def __init__(self, **kwargs):
		self.challengeId = kwargs.get('challengeId')
		self.answerId = kwargs.get('answerId')
		self.email = kwargs.get('email')
		self.postTime=kwargs.get('postTime', datetime.datetime.now())
		self.status = kwargs.get('status')
		self.description = kwargs.get('description')

	def __repr__(self):
		return '<answerId: %r email: %r description: %r challengeLevel: %r' % (self.answerId, self.email, self.createdEmail, self.challengeLevel)
		

class Challenges(db.Model):
	__tablename__="Challenges"
	challengeId=db.Column(db.String, primary_key = True)
	challengeName = db.Column(db.String(50))
	createdEmail=db.Column(db.String(50), unique = True)
	description = db.Column(db.String(200))
	challengeLevel = db.Column(db.Integer)
	createdTime = db.Column(db.DateTime)
	startTime = db.Column(db.DateTime)
	endTime = db.Column(db.DateTime)
	votes = db.Column(db.Integer)

	def __init__(self, **kwargs):
		self.challengeName=kwargs.get('challengeName')
		self.challengeId=kwargs.get('challengeId')
		self.createdEmail=kwargs.get('createdEmail')
		self.description=kwargs.get('description')
		self.createdTime=kwargs.get('createdTime', datetime.datetime.now())
		self.challengeLevel=kwargs.get('challengeLevel', 1)
		self.startTime=kwargs.get('startTime')
		self.endTime=kwargs.get('endTime')
		self.votes=kwargs.get('votes', 0)
		self.adjust_price()

	def __repr__(self):
		return '<challengeName: %r createdEmail: %r description: %r challengeLevel: %r' % (self.challengeName, self.description, self.createdEmail, self.challengeLevel)

class UserChallengeJoin(db.Model):
	__tablename__ = 'UserChallengesJoin'
	email = db.Column(db.String, db.ForeignKey('Users.email'), primary_key = True)
	challengeId = db.Column(db.String,db.ForeignKey('Challenges.challengeId') , primary_key = True)
	status = db.Column(db.String)

	def __init__(self, **kwargs):
		self.email = kwargs.get('email')
		self.challengeId = kwargs.get('challengeId')
		self.status = kwargs.get('status','open')

	def __repr__(self):
		return '<email: %r challengeId: %r status: %r' % (self.email, self.challengeId, self.status)

