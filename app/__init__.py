from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
Session(app)
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes and models
from app import routes, models
