from flask import Flask, render_template, redirect, request
# import the class from friend.py
from users import Users
app = Flask(__name__)

# HOME PAGE -------------------------------------------------------------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")





# DISPLAYS ALL USERS PAGE ------------------------------------------------------------------------------------------------------------------------------
@app.route('/users')
def display():
    users = Users.get_all()
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
    Users.inputUser(data)
    return redirect('/users')




# DISPLAY ONE SPECIFIC USER PAGE -------------------------------------------------------------------------------------------------------------------
@app.route('/users/<int:id>')
def showOne(id):
    return render_template("user.html", user = Users.getOne(id))




# UPDATE SPECIFIC USER PAGE -------------------------------------------------------------------------------------------------------------------------
@app.route('/users/<int:id>/update')
def updateUser(id):
    return render_template('edit.html', user = Users.getOne(id))

# HIDDEN ROUTE TO UPDATE SPECIFIC USER REDIRECTS TO DISPLAY ALL USERS PAGE
@app.route('/users/<int:id>/update', methods=['POST'])
def edit(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    Users.update(data)
    return redirect('/users')





# HIDDEN ROUTE TO DELETE A SPECIFIC USER REDIRECT TO DISPLAY ALL USERS PAGE ----------------------------------------------------------------------------
@app.route('/users/<int:id>/delete')
def delete(id):
    Users.delete(id)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)

