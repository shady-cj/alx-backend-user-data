#!/usr/bin/env python3
"""
creating a new authentication system,
based on Session ID stored in database(in-memory file)
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDbAuth(SessionExpAuth):
    """
    Creating a session authentication with
    in-memory file storage.
    """

    def create_session(self, user_id: str = None) -> str:
        """
        Creating a UserSession instance and saving them
        to file
        """
        session_id = super().create_session(user_id)
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id
    
    def user_id_for_session_id(self, session_id=None):
        """
         returns the User ID by requesting UserSession in the database based on session_id
        """
        sessions = UserSession.search({"session_id": session_id})
        if len(sessions) == 0:
            return None
        session = sessions[0]
        return session.user_id
    
    def destroy_session(self, request=None):
        """
        destroys the UserSession based on the Session ID from the request cookie
        """
        super().destroy_session()
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        sessions = UserSession.search({"session_id": session_id})
        if len(sessions) == 0:
            return False
        session = sessions[0]
        session.remove()
        return True
