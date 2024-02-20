from db import db

class WishlistModel(db.Model):
    
    # Create DB columns
    WishlistID = db.Column(db.String, unique = True, primary_key=True)
    ISBN0 = db.Str()
    ISBN1 = db.Str()
    ISBN2 = db.Str()