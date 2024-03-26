from db import db


class CommentModel(db.Model):

    # Create DB columns
    UserID = db.Column(db.String, unique = True, primary_key = True)
    ISBN = db.Column(db.String)
    CommentDate = db.Column(db.String)
    Comment = db.Column(db.String)