from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_msearch import Search
from flask_mail import Mail
from flask_authorize import Authorize
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])
search = Search()
search.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
authorize=Authorize(app)
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'CraftyWoodDev@hotmail.com'
app.config['MAIL_PASSWORD'] = 'outlook0appdev'
mail = Mail(app)

from ecommercesite import routes