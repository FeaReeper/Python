from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'goku>superman'

@app.route("/")
def start():
    session['num'] += 1
    return render_template("counter.html", num = session['num'])

@app.route("/destroy_session")
def reset():
    session['num'] = 0
    return redirect("/")

@app.route("/counter")
def plusTwo():
    session['num'] += 1
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)