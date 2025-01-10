# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load configurations from config.py
    app.config.from_object(Config)
    
    # Initialize the database with the app
    db.init_app(app)

    # Return the app object to be used in run.py
    return app
