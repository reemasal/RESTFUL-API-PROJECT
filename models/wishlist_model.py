from db import db

class WishlistModel(db.Model):
    
    # Create DB columns
    WishlistID = db.Column(db.String, primary_key=True)
    ISBN0 = db.Column(db.String)
    ISBN1 = db.Column(db.String)
    ISBN2 = db.Column(db.String)