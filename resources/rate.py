from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import RateModel
from schemas import RatingsSchema

blp = Blueprint("Ratings", __name__, description="Operations on book ratings and comments")

@blp.route("/rating")
class BookList(MethodView):
    @blp.response(200, RatingsSchema(many=True))
    def get(self):
        return RateModel.query.Rating()
