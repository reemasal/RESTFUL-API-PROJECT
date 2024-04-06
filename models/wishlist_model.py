from db import db

class WishlistModel(db.Model):
    # Create DB columns
    WishlistID = db.Column(db.Integer, primary_key=True)
    WishlistName = db.Column(db.String(50))
    Username = db.Column(db.String)

class ContentsModel(db.Model):
    # Create DB columns
    Row = db.Column(db.Integer, primary_key=True)
    WishlistID = db.Column(db.Integer)
    ISBN = db.Column(db.String)