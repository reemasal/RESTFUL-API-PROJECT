from db import db

class WishlistModel(db.Model):
    
    # Create DB columns
    WishlistID = db.Column(db.String, unique = True, primary_key=True)
    UserID = db.Column(db.String)
    Books = db.List(db.String)  # will "List" work??