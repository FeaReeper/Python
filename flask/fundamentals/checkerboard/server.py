from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerBoard():
    return render_template('checkerboard.html', x=8, y=8)


@app.route('/<int:y>')
def specifyY(y):
    return render_template('checkerboard.html', x=8, y=y)


@app.route('/<int:x>/<int:y>')
def specifyXY(x, y):
    return render_template('checkerboard.html', x=x, y=y)


if __name__=="__main__":
    app.run(debug=True)
