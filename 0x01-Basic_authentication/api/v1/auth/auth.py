#!/usr/bin/env python3
"""
Implementing an authentication system
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
        Defining the main authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Handlers that defines if auth is required or not.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        auth header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        """
        return None
