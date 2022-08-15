from flask import Flask
import logging
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
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
import flask_monitoringdashboard as dashboard
from ecommercesite.logger import setup_logger


app = Flask(__name__)
dashboard.bind(app)


jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "a0e9be06ce393344214c51be5c753fa58aef93b7c318e9375a0438a54fa1eab4"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
app.config["JWT_TOKEN_LOCATION"] = ['headers']
app.config['SECRET_KEY'] = '53e4ea4f348001e62295b81953988e9cbd25a49ced46adc6f3742c83284835a1'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.jinja_env.autoescape = True


root_logger = setup_logger('', 'logs/root.log')
users_logger = setup_logger('users', 'logs/users.log')
admin_logger = setup_logger('admin', 'logs/admin.log')
api_logger = setup_logger('api', 'logs/api.log')
product_logger = setup_logger('product', 'logs/product.log')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["20 per minute"])
search = Search()
search.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
authorize=Authorize(app)
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '8cea723599be2d'
app.config['MAIL_PASSWORD'] = 'fd968ddf02a284'
mail = Mail(app)

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s %(name)s %(threadName)s : %(message)s')

from ecommercesite import routes