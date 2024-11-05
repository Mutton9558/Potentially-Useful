from flask import *
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv('.env')
app = Flask(__name__)
app.secret_key = os.getenv('KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(255))
    username = db.Column("username", db.String(255))
    password = db.Column("password", db.String(255))

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password

@app.route('/')
def home():
    return redirect(url_for("register"))

@app.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        nameInput = request.form["name"]
        emailInput = request.form["email"]
        usernameInput = request.form["username"]
        passwordInput = request.form["password"]

        if users.query.filter_by(email = emailInput).first() or users.query.filter_by(username = usernameInput).first():
            flash("Email or Username already exists!")
        else:
            new_user = users(name=nameInput, email=emailInput, username=usernameInput, password=passwordInput)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        userInput = request.form["login-username"]
        passInput = request.form["login-password"]

        if users.query.filter_by(username = userInput).first():
            found_user = users.query.filter_by(username = userInput).first()
            if passInput == found_user.password:
                return redirect(url_for("home"))
            else:
                flash("Invalid Password!")
        else:
            flash("Username does not exist!")
    return render_template("login.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)