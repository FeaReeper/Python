from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'goku>superman'

@app.route("/")
def home():
    return render_template("index.html", num = session['num'])

@app.route("/mycoolsite")
def coolSite():
    if 'num' not in session:
        session['num'] = 1
    else:
        session['num'] += 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)