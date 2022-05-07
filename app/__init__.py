from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap    
from flask_mail import Mail

app = Flask(__name__)     

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy(app)

login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'


