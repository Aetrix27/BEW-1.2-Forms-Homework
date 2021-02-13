from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, ItemCategory

class GroceryStoreForm(FlaskForm):

    title = StringField('Title:', validators=[DataRequired(), Length(min=1, max=70)])
    address = TextAreaField('Address:', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):

    name = StringField('Name:', validators=[DataRequired(), Length(min=1, max=40)])
    price = FloatField('Price:', validators=[DataRequired()])
    category = SelectField("Category:", choices = ItemCategory.choices())
    photo_url = StringField('Photo URL:', validators=[DataRequired(), URL()])
    store = QuerySelectField('Store:', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')