from jello import db
from jello.entities.user import User
from sqlalchemy.orm import relationship

users_to_groups_association = db.Table (
  'users_to_groups_associattion',
  db.Colunn('user_id', db.Integer, db.ForeignKey(User.id), primary_key=True)
  db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True)
  
)

class Group(db.Model):
  __tablename__ = 'group'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)

  users = relationship(User.__name__, secondary=users_to_groups_association, backref='groups')

  











