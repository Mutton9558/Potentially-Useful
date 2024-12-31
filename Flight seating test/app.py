from flask import *
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import json

load_dotenv('.env')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.getenv('SECRET')

db = SQLAlchemy(app)

class Seats(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, nullable=False, unique=True)
    seatNumber = db.Column("seatNumber", db.String(3), nullable=False, unique=True)

    def __init__(self, seatNumber):
        self.seatNumber = seatNumber

import json

@app.route('/')
def home():
    rowTag = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F"}
    taken_seats = {seat.seatNumber for seat in Seats.query.all()}

    # Define quadrants
    quadrants = {
        "top": {f"{i}-{rowTag[j]}" for i in range(0, 5) for j in range(0, 6)},
        "left": {f"{i}-{rowTag[j]}" for i in range(0, 10) for j in range(0, 3)},
        "bottom": {f"{i}-{rowTag[j]}" for i in range(5, 10) for j in range(0, 6)},
        "right": {f"{i}-{rowTag[j]}" for i in range(0, 10) for j in range(3, 6)},
    }

    # Calculate how many seats are taken in each quadrant
    quadrant_taken = {key: len(taken_seats & seats) for key, seats in quadrants.items()}

    # Convert the dictionary to a JSON string
    quadrant_taken_json = json.dumps(quadrant_taken)

    return render_template(
        "index.html",
        rowDict=rowTag,
        taken_seats=taken_seats,
        quadrant_taken_json=quadrant_taken_json,
    )



@app.route('/process_id', methods=['POST'])
def process_id():
    if request.method == "POST":
        data = request.get_json()
        button_id = data.get('id')  # Get the button ID
        print(f"Button ID received: {button_id}")
        seatTaken = Seats(seatNumber=button_id)
        db.session.add(seatTaken)
        db.session.commit()
        return redirect(url_for("home"))
    # Do something with the button ID
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)