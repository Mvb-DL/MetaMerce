from ..models import *
from flask_login import current_user


class UserController:

  def get_user(self):
    user = User.query.filter(User.id==current_user.id)
    return user

  def create_user(self, email, first_name, last_name, user_name, password_one):
    new_user = User(email=email, first_name=first_name, last_name=last_name, user_name=user_name, password=password_one)
    db.session.add(new_user)
    db.session.commit()
    return new_user

  def delete_user(self):
    delete_user = User.query.filter_by(id=current_user.id).one()
    db.session.delete(delete_user)
    db.session.commit()
