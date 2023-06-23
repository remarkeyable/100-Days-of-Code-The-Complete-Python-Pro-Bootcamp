from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, BooleanField, HiddenField
from wtforms.validators import Email, InputRequired
from wtforms.validators import DataRequired, URL, Email


class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class Update(FlaskForm):
    sockets = BooleanField('Café has sockets?')
    sockets_hidden = HiddenField('', default='false')
    toilets = BooleanField('Café has toilets?')
    toilets_hidden = HiddenField('', default='false')
    wifi = BooleanField('Café has Wi-Fi?')
    wifi_hidden = HiddenField('', default='false')
    calls = BooleanField('Café can take calls?')
    calls_hidden = HiddenField('', default='false')
    seats = StringField('Seats at Café', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Update')


class Add(FlaskForm):
    sockets = BooleanField('Cafè has sockets?')
    sockets_hidden = HiddenField('', default='false')
    toilets = BooleanField('Cafè has toilets?')
    toilets_hidden = HiddenField('', default='false')
    wifi = BooleanField('Cafè has WiFi?')
    wifi_hidden = HiddenField('', default='false')
    calls = BooleanField('Cafè can take calls?')
    calls_hidden = HiddenField('', default='false')
    name = StringField('Cafè Branch Name', validators=[DataRequired()])
    map = StringField('Map URL', validators=[DataRequired()])
    img = StringField('Image URL', validators=[DataRequired()])
    location = StringField('Cafè Location', validators=[DataRequired()])
    seats = StringField('Seats on Cafè', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Add Cafè')
