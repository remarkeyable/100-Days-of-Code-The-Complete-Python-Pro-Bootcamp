from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, BooleanField, HiddenField
from wtforms.validators import Email, InputRequired
from wtforms.validators import DataRequired, URL, Email


class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class Update(FlaskForm):
    sockets = BooleanField('Cafe have sockets?')
    sockets_hidden = HiddenField('', default='false')
    toilets = BooleanField('Cafe have toilets?')
    toilets_hidden = HiddenField('', default='false')
    wifi = BooleanField('Cafe have Wifi?')
    wifi_hidden = HiddenField('', default='false')
    calls = BooleanField('Cafe can take calls?')
    calls_hidden = HiddenField('', default='false')
    seats = StringField('Seats on Cafe', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Update')



class Add(FlaskForm):
    name = StringField('Cafe Branch Name', validators=[DataRequired()])
    map = StringField('Map URL', validators=[DataRequired()])
    img = StringField('Image URL', validators=[DataRequired()])
    location = StringField('Cafe Location', validators=[DataRequired()])
    sockets = SelectField('Cafe have sockets?', choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()])
    toilets = SelectField('Cafe have toilets?', choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()])
    wifi = SelectField('Cafe have Wifi?', choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()])
    calls = SelectField('Cafe can take calls?', choices=[(True, 'Yes'), (False, 'No')], validators=[DataRequired()])
    seats = StringField('Seats on Cafe', validators=[DataRequired()])
    price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField('Add Cafe')
