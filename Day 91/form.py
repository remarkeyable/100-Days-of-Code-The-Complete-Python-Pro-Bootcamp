from flask_wtf.file import FileField
from flask_wtf import FlaskForm
from wtforms import SubmitField


class UploadImage(FlaskForm):
    image = FileField()
    submit = SubmitField('Get Colors')
