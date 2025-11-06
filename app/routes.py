from flask import Blueprint, request, jsonify
from .services.math_service import add, subtract

bp = Blueprint("api", __name__)