import os

from flask import Flask
from flask_smorest import Api


from db import db
import models

from resources.book import blp as BookBlueprint
from resources.profile import new_user_blp as NewUserBlueprint
from resources.rate import blp as RatingBlueprint
from resources.comment import blp as CommentBlueprint
from resources.wishlist import blp as WishlistBlueprint
from resources.authors import blp as AuthorBlueprint
from resources.BookBrowsing import blp as BookBrowsing
from resources.profile import user_blp as Username
from resources.profile import credit_card_blp as AddingCrediCard
from resources.profile import user_update_blp as UpdatedUser

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Books REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

   
    with app.app_context():
        db.create_all()

    api.register_blueprint(BookBlueprint)
    api.register_blueprint(RatingBlueprint)
    api.register_blueprint(CommentBlueprint)
    api.register_blueprint(WishlistBlueprint)    
    api.register_blueprint(NewUserBlueprint)
    api.register_blueprint(AuthorBlueprint)
    api.register_blueprint(BookBrowsing)
    api.register_blueprint(Username)
    api.register_blueprint(AddingCrediCard)
    api.register_blueprint(UpdatedUser)

    return app
