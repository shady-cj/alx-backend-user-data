#!/usr/bin/env python3
"""
Creating a class to handle session authentication.
"""
from .auth import Auth
import uuid


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
