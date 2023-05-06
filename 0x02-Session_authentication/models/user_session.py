#!/usr/bin/env python3
"""
Creating a User class
putting into consideration the user's
session.
"""
from .base import Base


class UserSession(Base):
    """
    Creating the UserSession session class
    to store the user_id
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Instantiating the class
        """
        super().__init__()
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
