from flask_app.models.user import User

# import the class from friend.py

from flask_app import app

from flask import render_template, request, redirect


# HOME PAGE -------------------------------------------------------------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")





# DISPLAYS ALL USERS PAGE ------------------------------------------------------------------------------------------------------------------------------
@app.route('/users')
def display():
    users = User.get_all()
    return render_template("read_all.html", all_users = users)





# CREATE A NEW USER PAGE -------------------------------------------------------------------------------------------------------------------------
@app.route("/create")
def newUser():
    return render_template("create.html")

# HIDDEN ROUTE THAT CREATES USER AND REDIRECTS TO DISPLAY ALL PAGE
@app.route('/hidden', methods=['POST'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    # This is where the OOP is being called to create a new user and pass the data into the class method
    User.inputUser(data)
    return redirect('/users')




# DISPLAY ONE SPECIFIC USER PAGE -------------------------------------------------------------------------------------------------------------------
@app.route('/users/<int:id>')
def showOne(id):
    return render_template("user.html", user = User.getOne(id))




# UPDATE SPECIFIC USER PAGE -------------------------------------------------------------------------------------------------------------------------
@app.route('/users/<int:id>/update')
def updateUser(id):
    return render_template('edit.html', user = User.getOne(id))

# HIDDEN ROUTE TO UPDATE SPECIFIC USER REDIRECTS TO DISPLAY ALL USERS PAGE
@app.route('/users/<int:id>/update', methods=['POST'])
def edit(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    User.update(data)
    return redirect('/users')





# HIDDEN ROUTE TO DELETE A SPECIFIC USER REDIRECT TO DISPLAY ALL USERS PAGE ----------------------------------------------------------------------------
@app.route('/users/<int:id>/delete')
def delete(id):
    User.delete(id)
    return redirect('/users')
