from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form to add a new pet to our database"""
    name = StringField('Pet name', validators=[InputRequired()])
    species = SelectField('Species', choices=[
                          ("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    photo_url = StringField('Photo URL address',
                            validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField("This pet is available")
