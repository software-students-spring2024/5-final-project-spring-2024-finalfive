from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('start.html')

@app.route("/profile")
def profile():
    
    return render_template("profile.html")
    
if __name__ == "__main__":
    app.run(debug=True)
