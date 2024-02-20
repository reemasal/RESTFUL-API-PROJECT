import psycopg2

# ElephantSQL database URL:
DATABASE_URL = 'postgres://khxdvvyv:guMe0P0531KG62ekc3rKCTtRAEWi0qDr@baasu.db.elephantsql.com/khxdvvyv'

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def add_book_to_cart(user_id, book_id, quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO CartItems (UserID, BookID, Quantity) VALUES (%s, %s, %s)',
                (user_id, book_id, quantity))
    conn.commit()
    cur.close()
    conn.close()

def remove_book_from_cart(cart_item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM CartItems WHERE CartItemID = %s', (cart_item_id,))
    conn.commit()
    cur.close()
    conn.close()

def calculate_cart_subtotal(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT SUM(b.Price * ci.Quantity) FROM CartItems ci JOIN Books b ON ci.BookID = b.BookID WHERE ci.UserID = %s', (user_id,))
    subtotal = cur.fetchone()[0]
    cur.close()
    conn.close()
    return subtotal
