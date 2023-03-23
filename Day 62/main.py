from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Map link', validators=[DataRequired()])
    opening = StringField('Opening time eg. 8AM', validators=[DataRequired()])
    closing = StringField('Closing time eg. 10PM', validators=[DataRequired()])
    cof_rating = SelectField('Coffee Rating', choices=["☕️", '☕️☕️', '☕️☕☕', '☕️☕☕☕', '☕️☕☕☕☕'])
    wifi_rating = SelectField('Wifi Strength Rating', choices=["✘", '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    soc_rating = SelectField('Wifi Strength Rating', choices=["🔌", '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit', )


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [form.cafe.data, form.location.data, form.opening.data, form.closing.data, form.cof_rating.data,
                form.wifi_rating.data, form.soc_rating.data]
        with open('cafe-data.csv', "a", newline='', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
            form = CafeForm(formdata=None)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
