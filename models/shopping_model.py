from app import db

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=False)
    book_id = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

def add_book_to_cart(user_id, book_id, quantity):
    new_cart_item = CartItem(user_id=user_id, book_id=book_id, quantity=quantity)
    db.session.add(new_cart_item)
    db.session.commit()

def remove_book_from_cart(cart_item_id):
    cart_item = CartItem.query.filter_by(id=cart_item_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()

def calculate_cart_subtotal(user_id):
    subtotal = db.session.query(db.func.sum(CartItem.quantity * 10)).filter_by(user_id=user_id).scalar()
    return subtotal if subtotal else 0

