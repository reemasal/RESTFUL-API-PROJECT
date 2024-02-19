import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('../instance/data.db')
cursor = conn.cursor()


# Path to your CSV file
csv_file_path = './ratings.csv' # change this

# Open and read the CSV file
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the header row if it exists
    next(csv_reader, None)

    # Insert data into the table
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO rate_model (RatingDate, Rating, ISBN, UserID, CommentDate, Comment)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', row)


# Commit the changes and close the connection
conn.commit()
conn.close()
