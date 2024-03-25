from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from models import WishlistModel, ContentsModel
from schemas import WishlistSchema
from schemas import ContentsSchema

blp = Blueprint("Wishlist", __name__, description = "Operations on Wishlists")
 
@blp.route("/wishlist/<string:wishlistID>")
class WishlistGet(MethodView):
    @blp.response(200, ContentsSchema(many=True))
    def get(self, wishlistID):
        wishlist = ContentsModel.query.filter_by(WishlistID=wishlistID).all()
        return wishlist
    
@blp.route("/wishlist/update")
class WishlistAdd(MethodView):
    @blp.response(201, ContentsSchema)
    def post(self):
        wishlist_data = request.get_json()
        wishlist_add = ContentsModel(**wishlist_data)
        try:
            db.session.add(wishlist_add)
            db.session.commit()
        except IntegrityError:
            abort(400, message = "This book is already on your wishlist.")
        except SQLAlchemyError:
            abort(500, message = "An error occured while adding this book.")
        return wishlist_add
