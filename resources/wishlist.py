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