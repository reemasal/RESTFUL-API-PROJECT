from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError

from models import BookModel
from schemas import CartItemAddSchema, CartItemRemoveSchema, UserIDSchema
from flask import Blueprint, jsonify, request
from models.shopping_model import add_book_to_cart, remove_book_from_cart, calculate_cart_subtotal

shopping_cart_bp = Blueprint('shopping_cart', __name__)

@shopping_cart_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    add_book_to_cart(data['UserID'], data['BookID'], data['Quantity'])
    return jsonify({'message': 'Book added to cart successfully'}), 201

@shopping_cart_bp.route('/remove_from_cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    remove_book_from_cart(data['CartItemID'])
    return jsonify({'message': 'Book removed from cart successfully'}), 200

@shopping_cart_bp.route('/cart_subtotal/<int:user_id>')
def cart_subtotal(user_id):
    subtotal = calculate_cart_subtotal(user_id)
    return jsonify({'subtotal': subtotal}), 200
