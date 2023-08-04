from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


from flask_app import app

from flask import render_template, request, redirect



# HOME PAGE -------------------------------------------------------------------------------------------------------------------------------------
@app.route("/dojos")
def show_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("home.html", all_dojos = dojos)



# Creates a dojo and redirects to Home Page-------------------------------------------------------------------------------------------------------
@app.route("/dojos/create/dojo", methods = ["POST"])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.new_dojo(data)
    return redirect("/dojos")



# Shows dojo page that displays all off it's ninjas
@app.route("/dojos/<int:id>")
def ninjas_in_dojo(id):
    return render_template("dojo.html", dojo = Dojo.get_one_dojo(id), ninjas = Ninja.get_all_ninjas(id))
