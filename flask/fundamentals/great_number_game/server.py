from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "goku>superman"


@app.route("/")
def home():
    if 'num' not in session:
        session['answer'] = random.randint(1,100)
    return render_template("home.html")

@app.route("/guess", methods=["POST"])
def numberGuess():
    session['guess'] = request.form["guess"]
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
