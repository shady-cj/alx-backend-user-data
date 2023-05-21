#!/usr/bin/env python3
"""
Contains utility authentication functions and classes
"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
     takes in a password string arguments
     and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        The method registers a user into self._db
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {email} already exists".format(email=email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
        return user
