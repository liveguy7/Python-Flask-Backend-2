from flask import Blueprint, redirect, request
from werkzeug.security import check_password_hash
from jello.routes import allowed_users
import jwt


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'] )
def login():
  d = request.json
  if "username" not in d or 'password' not in d:
    raise Exception('unable to authenticate')

  if not check_password_hash(
    allowed_users[d['username']],
    d['password']
  ):
    raise Exception('invalid password')

  encoded_jwt = jwt.encode({
    "sub": 1, 
    "name": 'pan'
  })







