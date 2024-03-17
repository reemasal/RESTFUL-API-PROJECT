from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import ProfileModel
from schemas import ProfileManagement

profile_blp = Blueprint("Profile", __name__, description="Profiles details")

@profile_blp.route("/profiles")
class Profiles(MethodView):
    @profile_blp.response(200, ProfileManagement(many=True))
    def get(self):
        return ProfileModel.query.all()

new_user_blp = Blueprint("NewUser", __name__, description='New Profiles')

@new_user_blp.route("/newuser")
class NewUser(MethodView):
    @new_user_blp.response(201, ProfileManagement(many=False))
    def post(self):
        input_data = request.get_json()
        new_profile = ProfileModel(**input_data)
        db.session.add(new_profile)
        db.session.commit()
        return new_profile

