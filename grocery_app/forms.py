from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL, ValidationError
from grocery_app.models import GroceryStore, ItemCategory
from .models import User

class GroceryStoreForm(FlaskForm):

    title = StringField('Title:', validators=[DataRequired(), Length(min=1, max=70)])
    address = TextAreaField('Address:', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):

    name = StringField('Name:', validators=[DataRequired(), Length(min=1, max=40)])
    price = FloatField('Price:', validators=[DataRequired()])
    category = SelectField("Category:", choices = ItemCategory.choices())
    photo_url = StringField('Photo URL:', validators=[DataRequired(), URL()])
    store = QuerySelectField('Store:', query_factory=lambda: GroceryStore.query, allow_blank=False, get_label='title')
    
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')