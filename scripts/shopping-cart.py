from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

# ElephantSQL database URL:
DATABASE_URL = 'postgres://khxdvvyv:guMe0P0531KG62ekc3rKCTtRAEWi0qDr@baasu.db.elephantsql.com/khxdvvyv'

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

# Route for getting books from the database.
@app.route('/books')
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    book_list = [{'title': book[1], 'author': book[2], 'price': book[3]} for book in books] 
    return jsonify(book_list)

# Route for adding books to shopping cart.
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO CartItems (UserID, BookID, Quantity) VALUES (%s, %s, %s)',
                (data['UserID'], data['BookID'], data['Quantity']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Book added to cart successfully'}), 201


# Route for removing books from shopping cart.
@app.route('/remove_from_cart', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM CartItems WHERE CartItemID = %s', (data['CartItemID'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Book removed from cart successfully'}), 200

# Route for getting cart subtotal
@app.route('/cart_subtotal/<int:user_id>')
def cart_subtotal(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT SUM(b.Price * ci.Quantity) FROM CartItems ci JOIN Books b ON ci.BookID = b.BookID WHERE ci.UserID = %s', (user_id,))
    subtotal = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({'subtotal': subtotal}), 200

if __name__ == '__main__':
    app.run(debug=True)
