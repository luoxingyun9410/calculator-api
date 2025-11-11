from flask import Blueprint, request, jsonify
from .services.math_service import add, subtract, multiply, divide

bp = Blueprint("api", __name__)

def _parse_numbers():
    if request.is_json:
        data = request.get.json() or {}
        a, b =data.get("a"), data.get("b")
    else:
        a = request.args.get("a", type =float)
        b = request.args.get("b", type =float)
    if a is None or b is None:
        return None, None, jsonify({"error":"Both 'a' and 'b' parameters are required."}), 400
    return float(a), float(b), None, None

@bp.route("/add", methods=["GET","POST"])
def add_route():
    a, b, err, code = _parse_numbers()
    if err:
        return err, code
    return jsonify({"result": add(a,b)})

@bp.route("/subtract", methods=["GET","POST"])
def subtract_route():
    a, b, err, code = _parse_numbers()
    if err:
        return err, code
    return jsonify({"result": subtract(a,b)})

@bp.route("/multiply", methods=["GET","POST"])
def multiply_route():
    a, b, err, code = _parse_numbers()
    if err:
        return err, code
    return jsonify({"result": multiply(a,b)})

@bp.route("/divide", methods=["GET","POST"])
def divide_route():
    a, b, err, code = _parse_numbers()
    if err:
        return err,code
    try:
        jsonify({"result": divide(a,b)})
    except ZeroDivisionError as e:
        return {"error": str(e)}, 400