#!/usr/bin/env python3
"""
Implementing session expiry
"""
from .session_auth import SessionAuth
from datetime import datetime
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    Implements expiration for the current
    session Authentication system.
    """

    def __init__(self):
        """
        Setting the session duration from the
        environment variable SESSION_DURATION
        """
        try:
            self.session_duration = int(getenv("SESSION_DURATION", 0))
        except:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """
        Overloading the create session and adding a new
        attribute created_at to store when the session was
        created.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.__class__.user_id_by_session_id[session_id] = session_dict
        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        """
        Return the user_id based on the
        expiration time
        """
        if session_id is None:
            return session_id
        session_info = self.user_id_by_session_id.get(session_id)
        if session_info is None:
            return None
        if self.session_duration <= 0:
            return session_info.get("user_id")
        created_at = session_info.get("created_at")
        if created_at is None:
            return None
        now = datetime.datetime.now()
        total_secs = created_at.timestamp() + self.session_duration
        if now.timestamp() > total_secs:
            return None
        return session_info.get("user_id")
