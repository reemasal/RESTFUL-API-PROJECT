from marshmallow import Schema, fields


class BookDetailsSchema(Schema):
    ISBN = fields.Str(required=True) # book id
    Name = fields.Str()
    Description = fields.Str()
    Price = fields.Int()
    AuthorID = fields.Str()
    Genre = fields.Str()
    Publisher = fields.Str()
    YearPublished = fields.Str()
    Sold =fields.Int()
    Rating = fields.Int()

class AuthorSchema(Schema):
    AuthorID = fields.Str(required=True)
    FirstName = fields.Str()
    LastName = fields.Str()
    Books = fields.Str()
    Biography = fields.Str()
    Publisher = fields.Str()
    

class ProfileManagement(Schema):
    Username = fields.Str(required = True)
    Password = fields.Str(required = True)
    Name = fields.Str()
    EmailAddress = fields.Str()
    HomeAddress = fields.Str()
    CreditCardName = fields.Str()
    CreditCardNumber = fields.Str()
    CreditCardExpMonth = fields.Int()
    CreditCardExpYear = fields.Int()
    CreditCardSecurityCode = fields.Str()
    CreditCardZipCode = fields.Int()

class RatingsSchema(Schema):
    UserID = fields.Str(required = True)
    ISBN = fields.Str() # book id
    RatingDate = fields.Str()
    Rating = fields.Int()
    CommentDate = fields.Str()
    Comment = fields.Str()

class WishlistSchema(Schema):
    WishlistID = fields.Int(required=True)
    ISBN0 = fields.Str()
    ISBN1 = fields.Str()
    ISBN2 = fields.Str()
