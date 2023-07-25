from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "goku>superman"

@app.route('/')
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
