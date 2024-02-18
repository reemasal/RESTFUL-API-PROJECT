from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import BookModel
from schemas import BookDetailsSchema

blp = Blueprint("Books", __name__, description="Operations on book details")

@blp.route("/book")
class BookList(MethodView):
    @blp.response(200, BookDetailsSchema(many=True))
    def get(self):
        return BookModel.query.all()
