from flask import Flask, render_template, redirect, request
# import the class from friend.py
from users import Users
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("create.html")

@app.route('/hidden', methods=['POST'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    Users.inputUser(data)
    # We need to add the form inputs to the database
    return redirect('/display')

@app.route('/display')
def display():
    users = Users.get_all()
    return render_template("read_all.html", all_users = users)
            
if __name__ == "__main__":
    app.run(debug=True)

