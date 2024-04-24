from flask import Flask, request, render_template, redirect, url_for, flash, session
from hashlib import sha256
import mongomock, requests
from pymongo import MongoClient
from api import *

app = Flask(__name__)


app.config["MONGO_URI"] = MongoClient("mongodb://localhost:27017")
connection = app.config["MONGO_URI"]
db = connection["stats"]
users = db.users

try:
    connection.admin.command("ping")  
    print(" *", "Connected to MongoDB!")  
except Exception as e:
    print(" * MongoDB connection error:", e)

# @login_manager.user_loader
# def user_loader(email):
#     data = users.find_one({"email": email})
#     print(data)
#     #if data:
#         #return data
#     return render_template("login.html", error="User not found")


@app.route("/")
def display_login():
    return render_template("login.html", error = False)

# The route for the log-in page
@app.route("/", methods=["POST"])
def login():
    username = request.form['username']
    password = sha256(request.form["password"].encode()).hexdigest()
    data = users.find_one({"username": username})
    #print(f"Data: {data}")
    if data is None:
        return render_template("login.html", error = True)
    if data["password"] == password:
        return redirect(url_for("display_home", username = username))
    return render_template("login.html", error = True)

@app.route("/register")
def display_register():
    return render_template("register.html")

#the route for registering
@app.route("/register", methods=["POST"])
def register():
    name = request.form['name']
    username = request.form['username']
    password = sha256(request.form["password"].encode()).hexdigest()

    if users.find_one({"username": username}):
        return render_template("register.html", error = True)
    users.insert_one({"name": name, "username": username, "password": password, "friends": []})
    
    return render_template("login.html")

@app.route("/home/<username>")
def display_home(username):
    return render_template("start.html", username = username)

@app.route("/query/<sport>/<username>")
def display_query(sport, username):
    # if sport == "fc":
    #     return render_template("query.html", sport = "Football")
    return render_template("query.html", sport = sport, username = username)

@app.route("/profile/<username>")
def display_profile(username):
    return render_template("profile.html", username = username)

@app.route("/profile/<username>", methods=['POST'])
def profile(username):
    username = request.form["username"]
    return render_template("profile.html", username=username)


@app.route("/query/<sport>", methods=["POST"])
def query(sport):
    sport = request.form["sport"]
    return render_template("query.html", sport = sport)

if __name__ == "__main__":
    app.run(debug=True)
