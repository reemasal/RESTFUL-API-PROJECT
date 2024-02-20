from db import db


class RateModel(db.Model):

    # Create DB columns
    ISBN = db.Column(db.String, primary_key = True)
    RatingDate = db.Column(db.String)
    Rating = db.Column(db.Integer, nullable=True)
    UserID = db.Column(db.String)
    CommentDate = db.Column(db.String)
    Comment = db.Column(db.String)