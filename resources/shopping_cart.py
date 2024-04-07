from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models.shopping_model import add_book_to_cart, remove_book_from_cart, calculate_cart_subtotal
from schemas import CartItemAddSchema, CartItemRemoveSchema, UserIDSchema


blp = Blueprint('ShoppingCart', __name__, description="Operations on the shopping cart")

# Add to Cart
@blp.route("/add_to_cart", methods=['POST'])
class AddToCart(MethodView):

    @blp.arguments(CartItemAddSchema)
    @blp.response(201, CartItemAddSchema)
    def post(self, cart_item_data):
        try:
            add_book_to_cart(**cart_item_data)
            return {"message": "Book added to cart successfully"}, 201
        except SQLAlchemyError as e:
            abort(400, message=str(e))

# Remove from Cart
@blp.route("/remove_from_cart", methods=['DELETE'])
class RemoveFromCart(MethodView):

    @blp.arguments(CartItemRemoveSchema)
    @blp.response(200, CartItemRemoveSchema)
    def delete(self, cart_item_data):
        try:
            remove_book_from_cart(**cart_item_data)
            return {"message": "Book removed from cart successfully"}, 200
        except SQLAlchemyError as e:
            abort(400, message=str(e))

# Cart Subtotal
@blp.route("/cart_subtotal/<int:user_id>", methods=['GET'])
class CartSubtotal(MethodView):

    @blp.response(200)
    def get(self, user_id):
        try:
            subtotal = calculate_cart_subtotal(user_id)
            return {"subtotal": subtotal}, 200
        except SQLAlchemyError as e:
            abort(400, message=str(e))

