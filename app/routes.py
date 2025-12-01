from flask import Blueprint, jsonify
from. services.math_service import add, subtract, multiply, divide

bp = Blueprint ('api',__name__)

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@bp.route("/")
def home():
    return jsonify({"Calculator": "Please use /add/ | /subtract | /divide | /multiply"})

# ADDITION
@bp.route("/add")
def add_home():
    return jsonify({"Addition": "Please provide two numbers like /add/1/2"})

@bp.route("/add/<a>/<b>")
def add_route(a, b):
    try:
        aValue = float(a)
        bValue = float(b)

        result = add(aValue,bValue)
        if result.is_integer():
            result = int(result)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Please provide either a float or integer"}), 400
    
@bp.route("/subtract")
def subtract_home():
    return jsonify({"Addition": "Please provide two numbers like /add/1/2"})

@bp.route("/subtract/<a>/<b>")
def subtract_route(a, b):
    try:
        aValue = float(a)
        bValue = float(b)

        result = subtract(aValue,bValue)
        if result.is_integer():
            result = int(result)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Please provide either a float or integer"}), 400

@bp.route("/multiply")
def multiply_home():
    return jsonify({"Multiplication": "Please provide two numbers like /multiply/1/2"})

@bp.route("/multiply/<a>/<b>")
def multiply_route(a, b):
    try:
        aValue = float(a)
        bValue = float(b)

        result = multiply(aValue,bValue)
        if result.is_integer():
            result = int(result)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route("/divide")
def divide_home():
    return jsonify({"Division": "Please provide two numbers like /divide/1/2"})

@bp.route("/divide/<a>/<b>")
def divide_route(a, b):
    try:
        aValue = float(a)
        bValue = float(b)

        result = divide(aValue,bValue)
        if result.is_integer():
            result = int(result)
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400