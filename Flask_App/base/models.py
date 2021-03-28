from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from Flask_App import db, login_manager
from Flask_App.base.utils import hash_pass


class User(db.Model, UserMixin):
    __tablename__ = 'USER'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_TC = Column(String(11), unique=True, nullable=False)
    firstname = Column(String(50), default="Noname")
    lastname = Column(String(50), default="No Lastname")
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
