from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random   
import os

os.chdir('/workspaces/100-days-of-code/Day-66/')

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=True)
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
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def rand():
    rand_cafe = random.choice(db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all())
    return jsonify(
        name = rand_cafe.name,
        map_url = rand_cafe.map_url,
        img_url = rand_cafe.img_url,
        location = rand_cafe.location,
        seats = rand_cafe.seats,
        has_toilet = rand_cafe.has_toilet,
        has_wifi = rand_cafe.has_wifi,
        has_sockets = rand_cafe.has_sockets,
        can_take_calls = rand_cafe.can_take_calls,
        coffee_price = rand_cafe.coffee_price
        )


@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=['GET', 'POST'])
def search_cafe():
    loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location==loc)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return {
            "error" : {
                "Not Found" : "Sorry, we dont ahve a cafe at that location."
            }
        }

## HTTP POST - Create Record

@app.route("/add", methods=['POST','GET'])
def add():
    # if request.method == 'POST':
    print(request.args.get("name"))
    adding_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("loc"),
        has_sockets=request.args.get("sockets") == 'true',
        has_toilet=request.args.get("toilet") == 'true',
        has_wifi=request.args.get("wifi") == 'true',
        can_take_calls=request.args.get("calls") == 'true',
        seats=request.args.get("seats"),
        coffee_price=request.args.get("coffee_price"))
    
    db.session.add(adding_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
    # else:
    #     return jsonify(response={"Failed": "error."})

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods = ['PATCH'])
def update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    print(cafe)  
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the cafe."}), 200
    else:
        return {
            "error" : {
                "Not Found" : "Cafe not found."
            }
        }, 200

## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods = ['DELETE'])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        
        cafe = db.get_or_404(Cafe, cafe_id)
        print(cafe)  
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return {
                "error" : {
                    "Not Found" : "Sorry, a cafe with that id was not found in the database."
                }
            }, 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    
    
if __name__ == '__main__':
    app.run(debug=True)


