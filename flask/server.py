from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo/')

def hello_dojo():
    return 'Dojo'

@app.route('/hi/<string:name>/')

def hi_name(name):
    return f'Hi {name}'

@app.route('/hi/string:<name>/<int:num>/')

def many_hi(name, num):
    return f'Hi {name * num}'



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

