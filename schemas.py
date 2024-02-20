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
    RatingDate = fields.Str()
    Rating = fields.Int()
    ISBN = fields.Str(required=True) # book id
    UserID = fields.Str(required=True)
    CommentDate = fields.Str()
    Comment = fields.Str()


class CartItemAddSchema(Schema):
    UserID = fields.Str(required=True)
    BookID = fields.Str(required=True)
    Quantity = fields.Int(required=True, validate=lambda n: n > 0)

class CartItemRemoveSchema(Schema):
    CartItemID = fields.Str(required=True)

class UserIDSchema(Schema):
    UserID = fields.Str(required=True)
