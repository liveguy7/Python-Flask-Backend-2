from jello import db
from jello.entities.country import Country
from sqlalchemy.orm import relationship


class User(db.Model):
  __tablename__ = 'backend_user'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.Text, nullable=False)
  email = db.Column(db.String(50))

  country_id = db.Column(db.Integer, db.ForeignKey(Country.id))

  country = relationship(Country.__name__)
  profile = relationship('Profile', userlist=False, back_populates='user')


class Profile(db.Model):
  __tablename__ = "profile"

  id = db.Column(db.Integer, primary_key=True)
  birth_date = db.Column(db.DateTime)
  job = db.Column(db.String(50))
  user_id = db.Column(db.Integer, db.ForeignKey(User.id))

  user = relationship(User.__name__, userlist=False, back_populates='profile')







