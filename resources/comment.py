from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import CommentModel
from schemas import CommentsSchema

blp = Blueprint("Comments", __name__, description="Operations on book comments")

@blp.route("/newComment") # post a new comment
class NewComment(MethodView):
    @blp.response(201, CommentsSchema(many=False))
    def post(self):
        input_data = request.get_json()
        newComment = CommentModel(**input_data)
        db.session.add(newComment)
        db.session.commit()
        return newComment
    
@blp.route("/comments/<string:isbn>") # get all comments for one book
class CommentListOneBook(MethodView):
    @blp.response(200, CommentsSchema(many=True))
    def get(self, isbn):
        try:
            # Fetch comments for the specified ISBN
            comments = CommentModel.query.filter_by(ISBN=isbn).with_entities(CommentModel.Comment).all()

            # Extract comments from the list of tuples
            comments = [comment[0] for comment in comments]

            # Return comments in JSON format
            return jsonify(comments)
        except SQLAlchemyError:
            # Handle any database errors
            abort(500, message="Database error occurred.")
