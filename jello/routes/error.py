from os import error
from flask import Blueprint
from flask.json import jsonify


error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(Exception)
def handle_not_found(err):
  return jsonify({
    "message": 'jello not found'
  }), 404

@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
  return jsonify({
    'message': 'jello error'
  }), 504



