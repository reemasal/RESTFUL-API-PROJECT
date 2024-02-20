import logging
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
    def get(self, ISBN):
        try:
            # Assuming RateModel returns a list of ratings for a given ISBN
            ratings = RateModel.query.filter_by(ISBN=ISBN).all()
            if not ratings:
                # Assuming RateModel does not have a built-in method get_or_404()
                return {'message': 'Ratings not found'}, 404
            return ratings, 200
        except Exception as e:
            logging.error("This error occurred while processing the request: %s", e)
            abort(500, message="Internal server error")
    ##def get(self, ISBN):
        ##response = RateModel.query.get_or_404(ISBN)
        ##return response
