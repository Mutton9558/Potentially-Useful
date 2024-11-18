from flask import *
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv('.env')
app = Flask(__name__)
app.secret_key = os.getenv('KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.permanent_session_lifetime = timedelta(days=1)

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

class games(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    gameName = db.Column("name", db.String(100))
    gameDesc = db.Column('description', db.String(10000))
    img = db.Column("image", db.Text, nullable=True)
    mimetype = db.Column(db.Text, nullable=True)

    def __init__(self, gameName, gameDesc, img=None, mimetype=None):
        self.gameName = gameName
        self.gameDesc = gameDesc
        self.img = img
        self.mimetype = mimetype

@app.route('/', methods = ["POST", "GET"])
def home():
    if "user" in session and session["user"] != "":
        if session["user"] != "Mutton9558":
            return redirect(url_for("gamesShow"))
        if request.method == "POST":
            game_name = request.form["game-name"]
            game_desc = request.form["game-desc"]
            game_img = request.files["game-img"]
            if game_img:
                mt = game_img.mimetype
                game = games(gameName = game_name, gameDesc = game_desc, img = game_img.read(), mimetype = mt)
            else:
                game = games(gameName = game_name, gameDesc = game_desc)
            db.session.add(game)
            db.session.commit()   
            return redirect(url_for("home"))
        return render_template("index.html")
    else:
        return redirect(url_for("register"))

@app.route("/gamesShow")
def gamesShow():
    gameList = games.query.order_by(games.gameName.asc()).all()
    if "user" in session and session["user"] != "":
        return render_template("games.html", game_list = gameList)
    else:
        return redirect(url_for("register"))
    
@app.route('/game_image/<int:id>')
def game_image(id):
    game = games.query.get(id)
    if game and game.img:
        return Response(game.img, mimetype=game.mimetype)
    else:
        abort(404)  # Return 404 if the image or game doesn't exist

@app.route("/register", methods = ["POST", "GET"])
def register():
    if "user" in session and session["user"] != "":
        return redirect(url_for("home"))
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
        session.permanent = True
        userInput = request.form["login-username"]
        passInput = request.form["login-password"]

        if users.query.filter_by(username = userInput).first():
            found_user = users.query.filter_by(username = userInput).first()
            if passInput == found_user.password:
                session["user"] = userInput
                if session["user"] == "Mutton9558":
                    return redirect(url_for("home"))
                else:
                    return redirect(url_for("gamesShow"))
            else:
                flash("Invalid Password!")
        else:
            flash("Username does not exist!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session and session["user"] != "": # checks if session not null
        usr = session["user"]
        flash("User Logged Out Successfully!")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)