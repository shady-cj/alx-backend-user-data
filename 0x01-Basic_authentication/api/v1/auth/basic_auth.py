#!/usr/bin/env python3
"""
Implementing a basic authentication system
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Authentication system that inherits
    from the Auth system
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the base64 basic auth token
        """
        if type(authorization_header) == str and\
           authorization_header is not None:
            if authorization_header.startswith('Basic '):
                return authorization_header.lstrip('Basic ')

        return None
