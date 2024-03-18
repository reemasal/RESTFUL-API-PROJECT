from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import BookModel
from schemas import BookDetailsSchema

blp = Blueprint("Books", __name__, description="Operations on book details")

@blp.route("/book-details")
class BookList(MethodView):
    @blp.response(200, BookDetailsSchema(many=True))
    def get(self):
        return BookModel.query.all()
    
    @blp.arguments(BookDetailsSchema)
    @blp.response(201, BookDetailsSchema)
    def post(self, book_data):
        book = BookModel(**book_data)
        try:
            db.session.add(book)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A book with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the book.")

        return book

@blp.route("/book-details/<string:isbn>")
class BookListItem(MethodView):
    @blp.response(200, BookDetailsSchema)
    def get(self, isbn):
        response = BookModel.query.get_or_404(isbn)
        return response
    
    
    
# @blp.route("/book-details/<string:author>")
# class AuthorList(MethodView):
#     @blp.response(200,BookDetailsSchema)
#     def get(self, author):
#         response = BookModel.query.get_or_404(author)

# @blp.route("/author-details")
# class AuthorList(MethodView):
#     @blp.response(200, AuthorListSchema(many=True))
#     def get(self):
#         return AuthorListModel.query.all()

#     @blp.arguments(AuthorListSchema)
#     @blp.response(201, AuthorListSchema)
#     def post(self, book_data):
#         # item = AuthorListModel(**book_data)

#         try:
#             db.session.add(author)
#             db.session.commit()
#         except SQLAlchemyError:
#             abort(500, message="An error occured.")

#         return author