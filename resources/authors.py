from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import AuthorModel
from schemas import AuthorSchema

blp = Blueprint("Authors", __name__, description="Operations on author details")

@blp.route("/author-details")
class AuthorList(MethodView):
    @blp.response(200, AuthorSchema(many=True))
    def get(self):
        return AuthorModel.query.all()
    
    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, author_data):
        author = AuthorModel(**author_data)
        try:
            db.session.add(author)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A author with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the author.")

        return author

@blp.route("/author-details/<string:author_id>")
class BookListItem(MethodView):
    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        response = AuthorModel.query.get_or_404(author_id)
        return response