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
    Rating = fields.Int()
    ISBN = fields.Str(required=True) # book id
    userID = fields.Str(required=True)
    comment = fields.Str()

# need to pull then add mine later
class WishlistSchema(Schema):     # list of books by wishlists
    WishlistID = fields.Int(required=True)
    ISBN0 = fields.Str()
    ISBN1 = fields.Str()
    ISBN2 = fields.Str()