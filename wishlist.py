from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import WishlistModel
from schemas import WishlistSchema

blp = Blueprint("Wishlist", __name__, description = "Operations on Wishlists")

# list books on wishlist
@blp.route("/wishlist/<string:wishlistID>", methods = ['GET'])
class WishlistGet(MethodView):
    @blp.response(200, WishlistSchema)
    def get(self, wishlistID):
        response = WishlistModel.query.get_or_404(wishlistID)
        return response



# create wishlist that belongs to user and has unique name
# request type: POST
# params sent: wishlist id, user id
#@blp.route('wishlist/new', methods = ['POST'])
#def postNewWishlist():

# add book to wishlist
# request type: POST
# params sent: isbn, wishlist id
#@blp.route('/wishlist/add', methods = ['POST'])
#def postBook():
    
# remove a book from wishlist 
# (then add to shopping cart? logic doesn't specify it must be in cart)
# @blp.route('/wishlist/delete', methods = ['DELETE'])
#def deleteBook():