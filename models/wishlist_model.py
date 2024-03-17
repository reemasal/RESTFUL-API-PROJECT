from db import db

class WishlistModel(db.Model):
    # Create DB columns
    WishlistID = db.Column(db.Integer, primary_key=True)
    WishlistName = db.Column(db.String(50))
    Username = db.Column(db.String)


class WishlistContentsModel(db.Model):
    # Create DB columns
    WishlistID = db.Column(db.String, primary_key=True)
    ISBN = db.Column(db.String, primary_key=True)