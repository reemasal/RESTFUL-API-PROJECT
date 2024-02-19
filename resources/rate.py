from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import RateModel
from schemas import RatingsSchema

blp = Blueprint("Ratings", __name__, description="Operations on book ratings and comments")

@blp.route("/book-rating/<string:ISBN>")
class RatingList(MethodView):
    @blp.response(200, RatingsSchema(many=True))
    def get(self, isbn):
        # Assuming RateModel returns a list of ratings for a given ISBN
        ratings = RateModel.query.filter_by(isbn=isbn).all()
        if not ratings:
            # Assuming RateModel does not have a built-in method get_or_404()
            return {'message': 'Ratings not found'}, 404
        return ratings, 200
    ##def get(self, ISBN):
        ##response = RateModel.query.get_or_404(ISBN)
        ##return response
