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

@bp.route("/subtract/<int:a>/<int:b>")
def subtract_route(a, b):
    return jsonify({"result": subtract(a,b)})

@bp.route("/multiply/<int:a>/<int:b>")
def multiply_route(a, b):
    return jsonify({"result": multiply(a,b)})

@bp.route("/divide/<int:a>/<int:b>")
def divide_route(a, b):
    try:
        result = divide(a,b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400