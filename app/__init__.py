from flask import Flask,jsonify
from .services.math_service import add, subtract, multiply, divide

def create_app():
    app = Flask(__name__)

    @app.rpute('/add/<int:a>/<int:b>')
    def add_route(a, b):
        return jsonify({"result": add(a, b)})
    
    @app.route('/subtract/<int:a>/<int:b>')
    def subtract_route(a, b):
        return jsonify({"result": subtract(a, b)})
    
    @app.route('/multiply/<int:a>/<int:b>')
    def multiply_route(a, b):
        return jsonify({"result": multiply(a, b)})
    
    @app.route('/divide/<int:a>/<int:b>')
    def divide_route(a, b):
        try:
            result = divide(a, b)
            return jsonify({"result": result})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        
    return app