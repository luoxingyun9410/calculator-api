from flask import Blueprint, jsonify, request
from. services.math_service import add, subtract, multiply, divide

bp = Blueprint ('api',__name__)

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@bp.route("/")
def home():
    return jsonify({"Calculator": "Please use /add/ | /subtract | /divide | /multiply"})

# RULES: 
# Users have to send information in the body of their request as JSON (raw JSON in Postman for testing)

# TASKS:
# 1. Create reusable JSON function
# 2. All it at the start of all routes
# 3. Remove 'home' routes 
# 4. BONUS: Investigate flask 'middlewares' such as before_request and after_request https://www.geeksforgeeks.org/python/flask-middlewares/

def ValidateJSON():
    # This should contain the code to check that a user has submitted a JSON body in their request
    return

# ADDITION
@bp.route("/add", methods=["POST"])
def add_route():
    # TODO This should be a reusable function that always runs at the start of a route call
    if not request.is_json:
        return jsonify({"error": "Please provide a JSON body"})
    
    data = request.get_json()
    print(data)

    if 'firstNumber' not in data or 'secondNumber' not in data:
        return jsonify({"error": "Please provide firstNumber AND secondNumber in the body of your request"}), 400

    a = data["firstNumber"]
    b = data["secondNumber"]

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