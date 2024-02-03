from flask import Blueprint, jsonify, request, Response
from sqlalchemy.sql.schema import default_is_sequence
from werkzeug.security import generate_password_hash
from jello.routes import basic_auth, token_auth
from jello.entities.user import User, db

users_bp = Blueprint("users", __name__)


@users_bp.route('/users', methods=['GET'])
@basic_auth.login_required
def get_all_users():
  all_users = User.query.all()
  return jsonify(all_users)

@users_bp.route('/users', methods=['POST'])
@token_auth.login_required
def create_user():
  d = request.json
  print(d)
  u = User()
  u.username = d['username']
  u.email = d['email']
  u.password = generate_password_hash(d['password'])
  db.session.add(u)
  return Response(status=204)
  return jsonify(d), 201

@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
  u = User.query.filter(User.id == user_id).one()
  return jsonify({
    'id': 1,
    'name': 'pan'
  })














