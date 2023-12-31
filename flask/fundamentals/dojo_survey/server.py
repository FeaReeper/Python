from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "goku>superman"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/function', methods=['POST'])
def function():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("display.html")



if __name__ == "__main__":
    app.run(debug=True)
