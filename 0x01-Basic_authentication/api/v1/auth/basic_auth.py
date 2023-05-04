#!/usr/bin/env python3
"""
Implementing a basic authentication system
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
                                           self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        extracts and returns the decoded auth token
        """
        if type(base64_authorization_header) == str and\
           base64_authorization_header is not None:
            token = base64_authorization_header
            try:
                decoded_token = base64.b64decode(token)
                return decoded_token.decode('utf-8')
            except Exception as e:
                return None
        return None
