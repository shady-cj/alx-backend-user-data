#!/usr/bin/env python3
"""
Implementing an authentication system
"""
from flask import request
from typing import List, TypeVar
import re
from os import getenv


class Auth:
    """
        Defining the main authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Handlers that defines if auth is required or not.
        """
        if path is None or \
           excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path.rstrip('/')
        for p in excluded_paths:
            p = p.rstrip('/')
            if "*" in p:
                ind = p.find('*')
                list_p = list(p)
                list_p.insert(ind, ".")
                p = "".join(list_p)
            if re.search(r'^{}$'.format(p), path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        auth header
        """
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request:
        """
        if request is None:
            return request
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
