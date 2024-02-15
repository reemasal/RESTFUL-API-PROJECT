import os

from flask import Flask, request
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from db import db

# Flask app
def create_app(db_url=None):
    app = Flask(__name__)

# Set Database
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Bookstores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
     #use sqlite as local db, we can change this to our remote db after
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db") 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)
    ma = Marshmallow(app)
   
    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app