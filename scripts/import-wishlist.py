import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('instance\data.db')
cursor = conn.cursor()

# Path to your CSV file
csv_file_path = 'scripts\wishlists.csv'

# Open and read the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if it exists
    next(csv_reader, None)

    # Insert data into the table
    for row in csv_reader:
        cursor.execute('''
            INSERT OR IGNORE INTO wishlist_model (WishlistID, Username, ISBN0, ISBN1, ISBN2, ISBN3, ISBN4, ISBN5, ISBN6, ISBN7, ISBN8, 
                       ISBN9, ISBN10, ISBN11, ISBN12, ISBN13, ISBN14, ISBN15, ISBN16, ISBN17, ISBN18, ISBN19, ISBN20, ISBN21, 
                       ISBN22, ISBN23, ISBN24, ISBN25, ISBN26, ISBN27, ISBN28, ISBN29)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            ''', row)

# Commit the changes and close the connection
conn.commit()
conn.close()
