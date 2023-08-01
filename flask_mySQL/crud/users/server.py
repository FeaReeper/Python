from flask import Flask, render_template, redirect, request
# import the class from friend.py
from users import Users
app = Flask(__name__)

# root route for a home page
@app.route("/")
def index():
    return render_template("index.html")

# route to create a new user with a html displaying a form to input data
@app.route("/create")
def newUser():
    return render_template("create.html")

# route that is hidden, this is ran when submit is clicked on the create.html form page. Posts data to this route that sends data to class method in users.py, redirects to display
@app.route('/hidden', methods=['POST'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    # This is where the OOP is being called to create a new user and pass the data into the class method
    Users.inputUser(data)
    return redirect('/display')

# route to display one user
@app.route('/user/<int:id>')
def showOne(id):
    users = Users.getOne(id)
    return render_template("user.html", one_user = users)



@app.route('/user/<int:id>/update')
def updateUser(id):
    return render_template('edit.html', thisID = id)

# route to edit a specific user
@app.route('/users/<int:id>/update', methods=['POST'])
def edit(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    Users.update(data)
    return redirect('/display')



# route to delete a user
@app.route('/hidden/delete')
def delete():
    return redirect('/display')


# route that displays all the users
@app.route('/display')
def display():
    users = Users.get_all()
    return render_template("read_all.html", all_users = users)
            



if __name__ == "__main__":
    app.run(debug=True)

