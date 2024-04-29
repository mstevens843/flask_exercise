from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """return a + b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def subtract():
    """return a - b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def multiply():
    """return a * b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route('/div')
def divide():
    """return a / b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


operators = {
        "add" : add,
        "sub" : sub,
        "mult" : mult,
        "div" : div,
        }

@app.route("/math/<operator>")
def all_oper(operator):
    """Perform all operation on a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a, b)

    return str(result)


