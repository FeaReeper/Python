from flask import Flask, render_template, redirect, request
# from mysqlconnection import connectToMySQL

from flask_app import app

from flask_app.controllers import users


if __name__ == "__main__":
    app.run(debug=True)

