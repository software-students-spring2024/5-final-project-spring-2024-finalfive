from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login
import functools

# Initialize the App
app = Flask(__name__)
app.secret_key = 'super secret key'

# Mock user profile data - will be deleted once MongoDB database is active
user_profile = {
    "email": "john.doe@example.com",
    "password": "doeboy",
}

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return secure_function
# Initialize the login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

# Loads user from current session
@login_manager.user_loader
def user_loader(email):
    #results = user_collection.find_one({'email' : email})
    results = user_profile['email']
    if not results:
        return

    user = User()
    user.id = email
    return user

# Loads user from flask request
@login_manager.request_loader
def request_loader(request):
    email = request.form.get("email")
    #results = user_collection.find_one({'email' : email})
    results = user_profile['email']
    if not results:
        return

    user = User()
    user.id = email
    return user

# The route for the log-in page
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        action = request.form['action']
        
        # Attempts to find a DB entry from the Mongo Database
        results = user_profile['email']

        # Checks to see if user is already is in the databse
        if action == 'signin' and results and user_profile['password'] == "doeboy":
            #check_password_hash(user_profile['password'], password):
            user = User()
            user.id = email
            flask_login.login_user(user)
            session["email"] = email
            # Redirect to the home page upon successful login
            return redirect(url_for("home"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

#the route for registering
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        existing_user = user_profile['email']
        # Adds a Database entry if the user isn't already registered
        if existing_user is None:
            #hash_pass = generate_password_hash(password)
            #user_collection.insert_one({'email' : email, 'password' : hash_pass, 'name' : name})
            flash('Registration successful!', 'success')
            return redirect(url_for('home')) 
        return 'That email already exists!'
    return render_template('register.html')

# the route for the home page
@app.route("/home")
@login_required
def home():
    return render_template('start.html')

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", profile=user_profile)

@app.route("/deletion")
def delete_profile():
    # Implementation to delete  profile from db
    #
    #     
    #

    return render_template("profile.html")
    
if __name__ == "__main__":
    app.run(debug=True)
