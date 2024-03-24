from db import db

class AuthorModel(db.Model):
    AuthorID = db.Column(db.String, primary_key=True)
    FirstName = db.Column(db.String)
    LastName = db.Column(db.String)
    Books = db.Column(db.String)
    Biography = db.Column(db.String)
    Publisher = db.Column(db.String)