from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import RateModel
from schemas import RatingsSchema

blp = Blueprint("Ratings", __name__, description="Operations on book ratings and comments")

@blp.route("/ratings") # return everything from every data entry in ratings.csv
class RatingList(MethodView):
    @blp.response(200, RatingsSchema(many=True))
    def get(self):
        return RateModel.query.all()
    
@blp.route("/newRating") # post a new rating
class NewRating(MethodView):
    @blp.response(201, RatingsSchema(many=False))
    def post(self):
        input_data = request.get_json()
        newRating = RateModel(**input_data)
        db.session.add(newRating)
        db.session.commit()
        return newRating
    
@blp.route("/ratings/<string:isbn>")
class BookListItem(MethodView): # get all comments for one book
    @blp.response(200, RatingsSchema(many=True))
    def get(self, isbn):
        try:
            # Fetch comments for the specified ISBN
            comments = RateModel.query.filter_by(ISBN=isbn).with_entities(RateModel.Comment).all()

            # Extract comments from the list of tuples
            comments = [comment[0] for comment in comments]

            # Return comments in JSON format
            return jsonify(comments)
        except SQLAlchemyError:
            # Handle any database errors
            abort(500, message="Database error occurred.")

@blp.route("/averageRating/<string:isbn>") # get average rating for one book
class AverageRating(MethodView):
    @blp.response(200, RatingsSchema(many=True))
    def get(self, isbn):
        try:
            # Fetch ratings for the specified ISBN
            ratings = RateModel.query.filter_by(ISBN=isbn).with_entities(RateModel.Rating).all()

            # Extract ratings from the list of tuples
            ratings = [rating[0] for rating in ratings]
            
            ratingsTotal = 0.0 # add up value of all ratings into this variable
            ratingsCount = len(ratings) * 1.0 # number of ratings for a book
            
            for rating in ratings:
                ratingsTotal += rating

            # Get the average rating
            average_rating = ratingsTotal / ratingsCount

            # Return average rating
            return jsonify(average_rating)
        except SQLAlchemyError:
            # Handle any database errors
            abort(500, message="Database error occurred.")