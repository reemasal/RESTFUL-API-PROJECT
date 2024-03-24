from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import CommentModel
from schemas import CommentsSchema

blp = Blueprint("Comments", __name__, description="Operations on book comments")

@blp.route("/newComment")
class NewComment(MethodView):
    @blp.response(201, CommentsSchema(many=False))
    def post(self):
        input_data = request.get_json()
        newComment = CommentModel(**input_data)
        db.session.add(newComment)
        db.session.commit()
        return newComment