from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError


from schemas import ProfileManagement
from models import ProfileModel 

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
    
user_blp = Blueprint("User", __name__, description = "Profile by username")

@user_blp.route("/getuser/<username>")
class User(MethodView):
    @user_blp.response(200, ProfileManagement (many=False))
    def get(self, username):
        user = ProfileModel.query.filter_by(Username=username).first()
        return user
    

credit_card_blp = Blueprint("Credit Card", __name__, description="Manage credit card information for users")

@credit_card_blp.route("/user/<username>/creditcard")
class UserCreditCard(MethodView):
    def post(self, username):
        user = ProfileModel.query.filter_by(Username=username).first()

        user.CreditCardName = request.json.get('CreditCardName', user.CreditCardName)
        user.CreditCardNumber = request.json.get('CreditCardNumber', user.CreditCardNumber)
        user.CreditCardExpMonth = request.json.get('CreditCardExpMonth', user.CreditCardExpMonth)
        user.CreditCardExpYear = request.json.get('CreditCardExpYear', user.CreditCardExpYear)
        user.CreditCardSecurityCode = request.json.get('CreditCardSecurityCode', user.CreditCardSecurityCode)
        user.CreditCardZipCode = request.json.get('CreditCardZipCode', user.CreditCardZipCode)

        db.session.commit()
        
        return ({"message": "Credit card details updated successfully"}), 200
    

user_update_blp = Blueprint("Update user info", __name__, description = "Updating user info by its username")

@user_update_blp.route("/user/<username>")
class UpdateUser(MethodView):
    def patch(self, username):
        user = ProfileModel.query.filter_by(Username=username).first()
        input_data = request.get_json()
        if 'Username' in input_data:
            user.Username = input_data['Username']
        if 'Password' in input_data:
            user.Password = input_data['Password']
        if 'Name' in input_data:
            user.Name = input_data['Name']
        if 'HomeAddress' in input_data:
            user.HomeAddress = input_data['HomeAddress']

        db.session.commit()
        return ({"message": "User updated successfully"}), 200