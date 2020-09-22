from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

def create_app():
    if app.config["ENV"] == "production":
        app.config.from_object("config.Production")
    else:
        app.config.from_object("config.Development")
    db.init_app(app)
    with app.app_context():
        from application import views
        db.create_all()  # Create sql tables for our data models
    return app