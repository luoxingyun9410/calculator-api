from flask import Blueprint, jsonify
from. services.math_service import add, subtract, multiply, divide

bp = Blueprint ('api',__name__)

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@bp.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return jsonify({"result": add(a,b)})

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