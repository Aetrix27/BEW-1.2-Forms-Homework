from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
import os
# books_app/__init__.py
from flask_login import LoginManager
login_manager = LoginManager()

from .models import User

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(user_id)

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

from grocery_app.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()
