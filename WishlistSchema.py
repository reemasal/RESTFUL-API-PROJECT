from marshmallow import Schema, fields

class WishlistContentsSchema(Schema):     # actual wishlists
    WishlistID = fields.Int(dump=True)
    UserID = fields.Int()
    ISBN = fields.Str()

class WishlistOwnershipSchema(Schema):   # list holding all wishlists on site w/user_ids
    UserID = fields.Int(dump=True)
    WishlistID = fields.Int()