from flask_app.models.user import User


from flask_app import app

from flask import render_template, request, redirect, session

from flask import Bcyrpt
bcyrpt = Bcyrpt(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/create', methods=['POST'])
def create_user():

    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not User.validate_user(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # ****************Dont I need to put the bcrypt here, after the validator so the password doesnt go through the validator encrypted???????????
    pw_hash = bcyrpt.generate_password_hash(request.form['password'])
    # else no errors:
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
        }

    User.save(data)
    return redirect("/")

@app.route("/login/", methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = {
        "email" : request.form["email"]
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")