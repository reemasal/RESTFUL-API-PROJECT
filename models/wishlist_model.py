from db import db

class WishlistModel(db.Model):
    
    # Create DB columns
    WishlistID = db.Column(db.String, primary_key=True)
    Username = db.Column(db.String)
    ISBNList = db.Column(db.String)