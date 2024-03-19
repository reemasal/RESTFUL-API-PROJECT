from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import BookModel
from schemas import BookDetailsSchema, RatingsSchema

blp = Blueprint("Books1", __name__, description="Operations on book details")

@blp.route("/books/<string:genre>")
class BookList(MethodView):
    @blp.response(200, BookDetailsSchema(many=True))
    def get(self, genre):
        response = BookModel.query.filter_by(Genre=genre).all()
        return response
    
@blp.route("/books/top10")
class BookList(MethodView):
    @blp.response(200, BookDetailsSchema(many=True))
    def get(self):
        allbooks = BookModel.query.all()
        sortedBooks = sorted(allbooks, key=lambda book: book.Sold, reverse=True)
        return sortedBooks[0:10]

@blp.route("/books/<int:rating>")
class BookList(MethodView):
    @blp.response(200, BookDetailsSchema(many=True))
    def get(self, rating):
        response = BookModel.query.filter(BookModel.Rating>=rating)
        return response