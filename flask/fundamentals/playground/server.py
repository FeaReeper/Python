from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def welcome():
    return render_template('welcome.html', num=4, color='blue')


@app.route('/play/<int:num>')
def many_boxes(num):
    return render_template('welcome.html', num=num, color='blue')


@app.route('/play/<int:num>/<string:color>')
def color_change(num, color):
    return render_template('welcome.html', num=num, color=color)


if __name__=="__main__":
    app.run(debug=True)
