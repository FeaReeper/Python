from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def displayTable():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template('users.html', users=users)


# @app.route('/<int:y>')
# def specifyY(y):
#     return render_template('checkerboard.html', x=8, y=y)


# @app.route('/<int:x>/<int:y>')
# def specifyXY(x, y):
#     return render_template('checkerboard.html', x=x, y=y)

# @app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
# def specifyColor(x, y, color1, color2):
#     return render_template('checkerboard.html', x=x, y=y, color1=color1, color2=color2)



if __name__=="__main__":
    app.run(debug=True)
