from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import RateModel
from schemas import RatingsSchema

blp = Blueprint("Ratings", __name__, description="Operations on book ratings and comments")

@blp.route("/ratings")
class RatingList(MethodView):
    @blp.response(200, RatingsSchema(many=True))
    def get(self):
        return RateModel.query.all()
    
@blp.route("/ratings/<string:isbn>")
class BookListItem(MethodView): # get all comments for one book
    @blp.response(200, RatingsSchema(many=True))
    def get(self, isbn):
        try:
            print("Before comments\n")
            # Fetch comments for the specified ISBN
            comments = RateModel.query.filter_by(ISBN=isbn).all()

            print("Before comments_data\n")
            # Serialize comments using schema
            comments_data = RatingsSchema(many=True).dump(comments)

            print("Before return statement\n")
            # Return comments in JSON format
            return jsonify(comments_data)
        except SQLAlchemyError:
            # Handle any database errors
            abort(500, message="Database error occurred.")