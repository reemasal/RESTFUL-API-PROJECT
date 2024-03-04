from db import db


class ProfileModel(db.Model):

    # Create DB columns
    Username = db.Column(db.String, unique = True, primary_key=True)
    Password = db.Column(db.String)
    Name = db.Column(db.String(100))
    EmailAddress = db.Column(db.String)
    HomeAddress = db.Column(db.String)
    CreditCardName = db.Column(db.String)
    CreditCardNumber = db.Column(db.String)
    CreditCardExpMonth = db.Column(db.Integer)
    CreditCardExpYear = db.Column(db.Integer)
    CreditCardSecurityCode = db.Column(db.String)
    CreditCardZipCode = db.Column(db.Integer)
  
