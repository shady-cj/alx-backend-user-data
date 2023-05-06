#!/usr/bin/env python3
"""
Creating a class to handle session authentication.
"""
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    Extending Auth and implementing a session auth system.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.__class__.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
         returns a User ID based on a Session ID:
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value:
        """
        if request is None:
            return None
        get_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(get_cookie)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
         deletes the user session / logout:
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        self.__class__.user_id_by_session_id.pop(session_id)
        return True
