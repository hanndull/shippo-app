from random import choice
from flask import Flask, render_template, request
from shipping import create_shipment

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def starting_test():
    """Display homepage. & create Test shipment"""
    
    create_shipment()
    
    return "Hi! This is the homepage."


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")