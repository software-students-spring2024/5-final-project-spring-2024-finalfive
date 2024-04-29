from flask import Flask, request, render_template, redirect, url_for, flash, session
from hashlib import sha256
#import mongomock, requests
from pymongo import MongoClient
from stats_api import *

app = Flask(__name__)

# could use testing env for mongomock, but for now just use local mongodb
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
    users.insert_one({"name": name, "username": username, "password": password, "friends": [], "queries": []})
    
    return render_template("login.html")

@app.route("/home/<username>")
def display_home(username):
    return render_template("start.html", username = username)

@app.route("/profile/<username>", methods=['POST', 'GET'])
def display_profile(username):
    user = users.find_one({"username": username})
    user_friends = user["friends"]
    user_queries = user["queries"]
    #print(user_queries)
    if not user_friends and not user_queries:
          return render_template('profile.html', username = username, no_friends = True, no_queries = True, name = users.find_one({"username": username})["name"])
    if not user_friends:
        return render_template('profile.html', username = username, no_friends = True, queries = user_queries, name = users.find_one({"username": username})["name"])
    if not user_queries:
        return render_template('profile.html', username = username, friends = user_friends, no_queries = True, name = users.find_one({"username": username})["name"])
    return render_template("profile.html", friends=user_friends, username = username, queries = user_queries, name = users.find_one({"username": username})["name"])

@app.route("/addfriends/<username>")
def display_addfriends(username):
    return render_template("addfriends.html", username = username)

@app.route("/addfriends/<username>", methods=["POST"])
def addfriends(username):
    friend = request.form["friend"]
    if users.find_one({"username": friend}) is None:
        return render_template("addfriends.html", username = username, error = True)
    query = {"username": username, "friends": {"$in": [friend]}}
    if users.find_one(query) is not None:
        return render_template("addfriends.html", username = username, exist = True)
    users.update_one({"username": username}, {"$push": {"friends": friend}})
    return render_template("addfriends.html", username = username, success = True)

@app.route("/query/<username>/", methods=["GET"])
def display_query(username):
    sport = request.args.get('sport')
    return render_template("query.html", username=username, sport=sport)

@app.route("/query/<username>/", methods=["POST"])
def query(username):
    query_text = request.form["query"]
    sport = request.form["sport"]
    result = search_statmuse(query_text, sport)
    return render_template("query.html", username=username, sport=sport, result=result, query=query_text)

@app.route('/save_to_profile/<username>', methods=['POST'])
def save_to_profile(username):
    sport = request.form.get('sport')
    query = request.form.get('query')
    result = request.form.get('result')
    user_query = [sport, query, result]
    #print(user_query)
    users.update_one({"username": username}, {"$push": {"queries": user_query}})
    return redirect(url_for('display_home', username=username))

@app.route("/<original_user>/friends/<username>")
def display_friend(username, original_user):
    print(original_user)
    friend_queries = users.find_one({"username": username})["queries"]
    return render_template("friends.html", username = username, queries = friend_queries, og = original_user)

if __name__ == "__main__":   
    app.run(debug=True)
