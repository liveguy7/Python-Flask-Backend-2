from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import check_password_hash, generate_password_hash
import jwt

allowed_users = {
    'admin': generate_password_hash('admin'),
    'user': generate_password_hash('user')
}

allowed_tokens = {
    'token-sergio': 'sergio',
    'token-bob': 'bob'
}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

@basic_auth.verify_password
def verify_password(username, password):
  if username not in allowed_users:
    return None

  if check_password_hash(allowed_users[username],password):
    return username

@token_auth.verify_token
def verify_token(token):
  try:
    decoded_jwt = jwt.decode(
      token, 
      "mysecret", 
      algorithms['HS256'])
  except Exception as e:
    return None
  if decode_jwt['name'] in allowed_users:
    return decoded_jwt['name']
  return None




























