# Put your app in here.
from flask import Flask
from flask import request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/') 
def index():
    """Show homepage"""
    return """ <html>
            <body>
            <h1>I am the landing page</h1>
            </body>
        </html>
    """

@app.route("/add")
def calc_add():
    """Add a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = add(a,b)
    return str(res)

@app.route("/sub")
def calc_sub():
    """Subtract b from a"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = sub(a,b)
    return str(res)

@app.route("/mult")
def calc_mult():
    """Multiply a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = mult(a,b)
    return str(res)

@app.route("/div")
def calc_div():
    """Divide a by b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = div(a,b)
    return str(res)

@app.route("/math/<operation>")
def all_in_one(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    math = {"add": add(a,b), "sub": sub(a,b), "mult": mult(a,b), "div": div(a,b)}

    res = str(math[operation])
    return res 