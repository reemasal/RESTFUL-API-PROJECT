from db import db


class BookModel(db.Model):

    # Create DB columns
    ISBN = db.Column(db.String, primary_key=True)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String)
    Price = db.Column(db.Integer, nullable=True)
    AuthorID = db.Column(db.String, db.ForeignKey('author_model.AuthorID'))
    Genre = db.Column(db.String)
    Publisher = db.Column(db.String)
    YearPublished = db.Column(db.String)
    Sold = db.Column(db.Integer, nullable=True)
    Rating = db.Column(db.Integer, nullable=True)

    author = db.relationship('AuthorModel', backref='books')