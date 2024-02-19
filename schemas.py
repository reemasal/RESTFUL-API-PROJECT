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
    RatingDate = fields.Str()
    Rating = fields.Int()
    ISBN = fields.Str(required=True) # book id
    UserID = fields.Str(required=True)
    CommentDate = fields.Str()
    Comment = fields.Str()
