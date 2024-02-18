from marshmallow import Schema, fields


class BookDetailsSchema(Schema):
    ISBN = fields.Str(required=True) # book id
    Name = fields.Str()
    Description = fields.Str()
    Price = fields.Int()
    Author = fields.Str()
    Genre = fields.Str()
    Publisher = fields.Str()
    YearPublished = fields.Str()
    Sold =fields.Int()
    Rating = fields.Int()

class RatingsSchema(Schema):
    Rating = fields.Int()
    ISBN = fields.Str(required=True) # book id
    userID = fields.Str(required=True)
    comment = fields.Str()
