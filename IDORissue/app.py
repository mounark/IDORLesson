
from flask import Flask, render_template, request, redirect, session, url_for
import json
from functools import wraps

#Initialize the Flask application
app = Flask(__name__)
#Using the simple key below is for demonstration purposes only. In a prodcution env. I would make sure to use a random one with massive amounts of data for encryption.
app.secret_key = "supersecretkey"

#Load user data from users.json into a dictionary
with open("users.json", "r") as f:
    users = json.load(f)

#Define a decorator for authentication.
def login_required(f):
    @wraps(f)
    #*args and **kwargs are used for arbitratry number of arguments and argument defintions respectively
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

#Default route displayed is overview page.
@app.route("/")
def overview():
    return render_template("overview.html")

#Define login route where user logs in as Alice
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "Alice Parker" and password == "pasthe$123":
            session["user"] = "1"
            return redirect(url_for("profile", user_id=1))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

#Define instructions route to show the steps needed to see IDOR and resolve it
@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

#Define the logout route to end the user session
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

#Define route to show the different profiles and corresponding patient data
@app.route("/profile/<int:user_id>")
@login_required
def profile(user_id):
    user = users.get(str(user_id))
    if not user:
        return "Profile not found", 404
    return render_template("profile.html", user=user, users=users, user_id=user_id)

#Run the Flask in debug mode incase we have any issues we will get logs
if __name__ == "__main__":
    app.run(debug=True)
