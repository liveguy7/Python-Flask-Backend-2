from flask import Flask, render_template, jsonify, request, Response
from jello.routes.health import health_bp
from jello.routes.users import users_bp
from jello.routes.error import error_bp
from jello.routes.auth import auth_bp
from jello.extensions import db


def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jello.sqlite'

  db.app = app
  db.init_app(app)
 

  app.register_blueprint(health_bp)
  app.register_blueprint(users_bp)
  app.register_blueprint(error_bp)
  app.register_blueprint(auth_bp)

  
  return app



















