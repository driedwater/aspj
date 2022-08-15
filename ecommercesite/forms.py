from wtforms import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from ecommercesite.database import Users, User, Staff, Addproducts, Category
from flask_login import current_user
from wtforms import SubmitField, IntegerField, FloatField, StringField, TextAreaField, validators, SelectField, BooleanField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    last_name = StringField('Last Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=20), Regexp('^[a-zA-Z0-9_\d-]+$', message='Only alphabets, numbers, dash and underscore allowed')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    pot = StringField('random pot')
    submit = SubmitField('Register')

    def validate_pot(self, pot):
        if pot.data:
            raise ValidationError('If you are a human and see this invisible field, do not fill in this blank.')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20), Regexp('^[a-zA-Z0-9!@#$&*]+$', message='Enter alphabets, numbers and special characters(!@#$&*) only')])
    token = PasswordField('Token', validators=[DataRequired(), Length(min=6, max=6), Regexp('^[0-9]+$')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateUserAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    last_name = StringField('Last Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    username =  StringField('Username', validators=[DataRequired(), Length(min=2, max=20), Regexp('^[a-zA-Z0-9_\d-]*$', message='Only alphabets, numbers, dash and underscore allowed')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is taken.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('email is taken.')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(f'There is no account named {email.data}.')

class ResetPasswordForm(FlaskForm):
    password = StringField('Password', validators=[DataRequired(),  Length(min=8, max=20), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    submit = SubmitField('Reset Password')

class AddproductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Regexp('^[ a-zA-Z0-9_\d-]+$', message='Only alphabets, numbers, dash and underscore allowed')])
    description = TextAreaField('Description', validators=[DataRequired(), Regexp('^[ a-zA-Z0-9_!@#$&*\d-]+$', message='Only alphabets, numbers, special characters(-_!@#$&*) allowed')])
    category = SelectField('Category', validators=[DataRequired()], choices=[(1, 'New Arrival'), (2, 'Most Popular'), (3, '	Limited Time'), (4, 'Chair'), (5, 'Table'), (6, 'Cabinet'), (7, 'Door'), (8, 'Bed'), (9, 'Decoration'), (10, 'Others')])
    price = FloatField('Price', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    width = IntegerField('Width', validators=[DataRequired()])
    depth = IntegerField('Depth', validators=[DataRequired()])
    image_1 = FileField('Cover Image', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_4 = FileField('Image 4', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    image_5 = FileField('Image 5', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField("Add product")

#
#
class UpdateProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Regexp('^[ a-zA-Z0-9_.,\d-]+$', message='Only alphabets, numbers, dash and underscore allowed')])
    description = TextAreaField('Description', validators=[DataRequired(), Regexp('^[ a-zA-Z0-9_!@#$&*.,\d-]+$', message='Only alphabets, numbers, special characters(-_!@#$&*.,) allowed')])
    category = SelectField('Category', validators=[DataRequired()], choices=[(1, 'New Arrival'), (2, 'Most Popular'), (3, '	Limited Time'), (4, 'Chair'), (5, 'Table'), (6, 'Cabinet'), (7, 'Door'), (8, 'Bed'), (9, 'Decoration'), (10, 'Others')])
    price = FloatField('Price', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    length = IntegerField('Length', validators=[DataRequired()])
    width = IntegerField('Width', validators=[DataRequired()])
    depth = IntegerField('Depth', validators=[DataRequired()])
    image_1 = FileField('Cover Image', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_4 = FileField('Image 4', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_5 = FileField('Image 5', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField("Update Product")

class AdminRegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    last_name = StringField('Last Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=20), Regexp('^[a-zA-Z0-9_\d-]*$', message='Only alphabets, numbers, dash and underscore allowed')])
    email  = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),  Length(min=8, max=20), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=8, max=20), Regexp('^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z]).{8,20}$', message='Password must contain 1 uppercase and lowercase letter, 1 special character [!@#$&*], at least 2 numerical and at least 8 characters.')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is taken.')


class AddToCartForm(FlaskForm):
    submit = SubmitField("Add To Cart")

class AddReviewForm(FlaskForm):
    review = TextAreaField('Review', validators=[DataRequired(), Length(min=10, max=1000), Regexp('^[ a-zA-Z0-9_!@#$&*.,\d-]*$', message='Only alphabets, numbers, special characters(-_!@#$&*) allowed')])
    rating = SelectField('Product Rating', choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default= 'choose an option' )
    submit = SubmitField('Submit')

class CheckOutForm(FlaskForm):
    full_name =  StringField('Full Name', validators=[DataRequired(), Regexp('^[ a-zA-Z]+$', message='Enter alphabets only')])
    address = TextAreaField('Address', validators=[DataRequired(), Regexp('^[ a-zA-Z0-9@#_.,\d-]+$', message='Only alphabets, numbers, special characters(@#-_) is allowed.')])
    postal_code = StringField('Postal Code', validators=[DataRequired(), validators.Length(min=6, max=6, message='PLease enter a valid input'), Regexp('^[a-zA-Z0-9]+$', message='Enter alphabets and numbers only')])
    card_number = StringField('Card Number', validators=[DataRequired(), validators.Length(min=16, max=16,  message='PLease enter a valid input'), Regexp('^[0-9]*$', message='Only numbers allowed')], render_kw={"PlaceHolder": "•••• •••• •••• ••••"})
    expiry = StringField('Year of Expiry', validators=[DataRequired(),validators.Length(min=4, max=4, message='Please enter a valid input'), Regexp('^[0-9/]*$', message='Only numbers and slash(/) allowed')], render_kw={"PlaceHolder": "YYYY"})
    cvv = StringField('CVV', validators=[DataRequired(), validators.Length(min=3, max=3, message='PLease enter a valid input'), Regexp('^[0-9]*$', message='Only numbers allowed')], render_kw={"PlaceHolder": "•••"})
    submit = SubmitField('Checkout')
