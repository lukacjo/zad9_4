from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, TextAreaField, BooleanField,IntegerField, FormField
from wtforms.validators import DataRequired, Email
    
class MovieForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    title = StringField('Tytuł', validators=[DataRequired()])
    opinion = TextAreaField('Opinia o filmie', validators=[])
    watched = BooleanField('Czy obejrzany?')