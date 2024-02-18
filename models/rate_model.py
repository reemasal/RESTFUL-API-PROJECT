from db import db


class RateModel(db.Model):

    # Create DB columns
    Rating = db.Column(db.Integer, nullable=True)
    ISBN = db.Column(db.String, primary_key=True)
    userID = db.Column(db.String)
    comment = db.Column(db.String)