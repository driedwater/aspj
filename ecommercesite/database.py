from cryptography.fernet import Fernet
from pandas import describe_option
from ecommercesite import db, login_manager, app, ma
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from datetime import datetime, date
import pyotp
import os
import base64
from marshmallow_sqlalchemy import auto_field

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
        

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user')
    image_file = db.Column(db.String(20), nullable=False, default='defaultpfp.jpg')
    email_verification = db.Column(db.Boolean(), nullable=False, default=False)
    otp_secret = db.Column(db.String(16))
    attempts = db.Column(db.Integer, nullable=False, default=0)

    __mapper_args__ = {
        'polymorphic_on':type,
        'polymorphic_identity':'user'
    }
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.otp_secret is None:
            # generate a random secret
            self.otp_secret = base64.b32encode(os.urandom(10)).decode('utf-8')

    def get_totp_uri(self):
        return f'otpauth://totp/The-Boutique:{self.email}?secret={self.otp_secret}&issuer=The-Boutique'

    def verify_totp(self, token):
        return pyotp.TOTP(self.otp_secret).verify(token)
    
    def get_email_verification_token(self, expires_sec=1800):
        t = Serializer(app.config['SECRET_KEY'], expires_sec)
        return t.dumps({'user_id':self.id}).decode('utf-8')

    def verify_verification_token(token):
        t = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = t.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)


    def __repr__(self):
        return f"User( '{self.username}', '{self.email}')"


class Users(User):
    cart = db.relationship('Items_In_Cart', backref='cart_user', lazy=True)
    review = db.relationship('Review', backref='author', lazy=True)
    product_bought = db.relationship('Product_Bought', backref='product_id_bought', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity':'users'
    }

    def __repr__(self):
        return f"User( '{self.username}', '{self.email}')"

class Staff(User):
    pass

    __mapper_args__ = {
        'polymorphic_identity':'staff'
    }

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product_Bought(db.Model):
    __tablename__ = 'product_bought'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    date_bought = db.Column(db.Date, nullable=False, default=date.today)
    datetime_bought = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Items_In_Cart(db.Model):
    __tablename__ = 'items_in_cart'
    id = db.Column(db.Integer, primary_key=True)
    image_1 = db.Column(db.String(150), nullable=False, default='product-single-1.jpg')
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default='1')
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    user_review = db.Column(db.String(1000), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


class Addproducts(db.Model):
    __searchable__ = ['name','description']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    depth = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))
    price = db.Column(db.Numeric(10,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    image_1 = db.Column(db.String(150), nullable=False, default='product-single-1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='product-single-2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='product-single-3.jpg')
    image_4 = db.Column(db.String(150), nullable=False, default='product-single-4.jpg')
    image_5 = db.Column(db.String(150), nullable=False, default='product-single-5.jpg')


    def __repr__(self):
        return '<Post %r>' % self.name
    

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    

    def __repr__(self):
        return f"{self.name}"

class Customer_Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable = False)
    address = db.Column(db.Text, nullable = False)
    postal_code = db.Column(db.Integer, nullable = False)
    card_number = db.Column(db.Integer, nullable = False)
    expiry = db.Column(db.Integer, nullable = False)

    def __init__(self, full_name, card_number, expiry, postal_code, address):
        
        self.full_name = full_name
        self.card_number = card_number
        self.expiry = expiry
        self.postal_code = postal_code
        self.address = address
        

class CustomerPaymentsSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ('full_name', 'card_number', 'expiry', 'postal_code', 'address')
        # model = Customer_Payments
        # id = ma.auto_field()
        # full_name = ma.auto_field()
        # card_number = ma.auto_field()

class ReviewSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Review
        include_fk = True
    id = auto_field()
    user_review = auto_field()
    product_id = auto_field()
    # user_id = auto_field()
    rating = auto_field()

class AddProductsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Addproducts
        include_fk = True
    id = auto_field()
    name = auto_field()
    description = auto_field()
    length = auto_field()
    width = auto_field()
    depth = auto_field()
    category_id = auto_field()
    category = auto_field()
    price = auto_field()
    image_1 = auto_field()
    image_2 = auto_field()
    image_3 = auto_field()
    image_4 = auto_field()
    image_5 = auto_field()

class AdminAddProductsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Addproducts
        include_fk = True

class CartSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Items_In_Cart
        include_fk = True
    
    id = auto_field()
    image_1 = auto_field()
    name = auto_field()
    price = auto_field()
    quantity = auto_field()
    product_id = auto_field()
    user_id = auto_field()



# class AddProductsSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Addproducts
#         include_fk = True



db.create_all()
CustomerPaymentsSchema = CustomerPaymentsSchema()
reviewschema = ReviewSchema()
reviewsschema = ReviewSchema(many=True)
addProductSchema = AddProductsSchema()
addProductsSchema = AddProductsSchema(many=True)
adminProductSchema = AdminAddProductsSchema()
adminProductsSchema = AdminAddProductsSchema(many=True)
cartSchema = CartSchema()
cartsSchema = CartSchema(many=True)
