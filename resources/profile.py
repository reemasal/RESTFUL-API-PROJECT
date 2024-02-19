from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import ProfileModel
from schemas import ProfileManagement

blp = Blueprint("Profiles", __name__, description="Profiles details")

@blp.route("/profiles")
class BookList(MethodView):
    @blp.response(200, ProfileManagement(many=True))
    def get(self):
        return ProfileModel.query.all()

