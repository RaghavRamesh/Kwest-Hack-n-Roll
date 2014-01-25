import flask, flask.views
from app import app

# Views
from login import Login 
from profile import Profile
from feed import Feed
from challengeInfo import ChallengeInfo
from challengeCreate import ChallengeCreate
from shop import Shop
from profile import Profile
# Routes
app.add_url_rule('/login',
	view_func=Login.as_view('login'),
	methods=['GET', 'POST'])
app.add_url_rule('/profile',
	view_func=Profile.as_view('profile'),
	methods=['GET', 'POST'])
app.add_url_rule('/feed',
	view_func=Feed.as_view('feed'),
	methods=['GET', 'POST'])
app.add_url_rule('/challengeInfo',
	view_func=ChallengeInfo.as_view('challengeInfo'),
	methods=['GET', 'POST'])
app.add_url_rule('/challengeCreate',
	view_func=ChallengeCreate.as_view('challengeCreate'),
	methods=['GET', 'POST'])
app.add_url_rule('/shop',
	view_func=Shop.as_view('shop'),
	methods=['GET', 'POST'])