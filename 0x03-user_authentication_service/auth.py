#!/usr/bin/env python3
"""
Contains utility authentication functions and classes
"""

import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from typing import Optional


def _hash_password(password: str) -> bytes:
    """
     takes in a password string arguments
     and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """
    The function should return a string representation of a new UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        It should expect email and password required arguments and
        return a boolean based on whether the credentials are valid
        or not
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Creates a session id for an email
        """
        try:
            user = self._db.find_user_by(email=email)
            uid = _generate_uuid()
            self._db.update_user(user.id, session_id=uid)
            return uid
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str = None) -> Optional(User):
        """
        retrieves user from session_id
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
