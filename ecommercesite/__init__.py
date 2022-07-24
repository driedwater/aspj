from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_msearch import Search
from flask_mail import Mail
from flask_authorize import Authorize
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "a0e9be06ce393344214c51be5c753fa58aef93b7c318e9375a0438a54fa1eab4"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
app.config['SECRET_KEY'] = '53e4ea4f348001e62295b81953988e9cbd25a49ced46adc6f3742c83284835a1'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
search = Search()
search.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
authorize=Authorize(app)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '5718ebb8bb03c2'
app.config['MAIL_PASSWORD'] = '8991fafdf77d0f'
mail = Mail(app)

from ecommercesite import routes