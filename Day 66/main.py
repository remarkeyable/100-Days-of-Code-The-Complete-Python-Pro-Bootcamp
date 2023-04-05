from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_cafe():
    cafe_list = db.session.query(Cafe).all()
    choice = random.choice(cafe_list)
    return jsonify(id=choice.id, name=choice.name, map_url=choice.map_url, img_url=choice.img_url,
                   location=choice.location, seats=choice.seats, has_toilet=choice.has_toilet, has_wifi=choice.has_wifi,
                   has_sockets=choice.has_sockets, can_take_calls=choice.can_take_calls,
                   coffee_price=choice.coffee_price, )


@app.route('/all')
def all_cafe():
    all_cafe = db.session.query(Cafe).all()
    dict_all_cafes = {"cafe": [cafe.to_dict() for cafe in all_cafe]}

    return jsonify(dict_all_cafes)


@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(name=request.form.get("name"), map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"), location=request.form.get("loc"),
                    has_sockets=bool(request.form.get("sockets")), has_toilet=bool(request.form.get("toilet")),
                    has_wifi=bool(request.form.get("wifi")), can_take_calls=bool(request.form.get("calls")),
                    seats=request.form.get("seats"), coffee_price=request.form.get("coffee_price"), )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
