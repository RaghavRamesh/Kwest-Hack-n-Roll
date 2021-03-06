import flask, flask.views
from app import app

# Views
from login import Login 
from Logout import Logout
from profile import Profile
from feed import Feed
from challengeInfo import ChallengeInfo
from challengeCreate import ChallengeCreate
from shop import Shop
from accept import Accept
from profile import Profile
# Routes
app.add_url_rule('/logout',
	view_func=Logout.as_view('logout'),
	methods=['GET'])
app.add_url_rule('/',
	view_func=Login.as_view('login'),
	methods=['GET', 'POST'])
app.add_url_rule('/profile',
	view_func=Profile.as_view('profile'),
	methods=['GET', 'POST'])
app.add_url_rule('/feed',
	view_func=Feed.as_view('feed'),
	methods=['GET', 'POST'])
app.add_url_rule('/challengeInfo/<int:challengeId>',
	view_func=ChallengeInfo.as_view('challengeInfo'),
	methods=['GET', 'POST'])
app.add_url_rule('/challengeCreate',
	view_func=ChallengeCreate.as_view('challengeCreate'),
	methods=['GET', 'POST'])
app.add_url_rule('/shop',
	view_func=Shop.as_view('shop'),
	methods=['GET', 'POST'])
app.add_url_rule('/accepted/<int:id>',
	view_func=Accept.as_view('accept'),
	methods=['GET', 'POST'])
