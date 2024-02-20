from db import db


class RateModel(db.Model):

    # Create DB columns
    UserID = db.Column(db.String, unique = True, primary_key = True)
    ISBN = db.Column(db.String)
    RatingDate = db.Column(db.String)
    Rating = db.Column(db.Integer, nullable=True)
    CommentDate = db.Column(db.String)
    Comment = db.Column(db.String)