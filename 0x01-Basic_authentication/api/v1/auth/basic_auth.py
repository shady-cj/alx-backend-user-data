#!/usr/bin/env python3
"""
Implementing a basic authentication system
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


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

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Extracts and returns the decoded user credentials
        """
        if type(decoded_base64_authorization_header) == str and\
           decoded_base64_authorization_header is not None:
            if ":" in decoded_base64_authorization_header:
                token = decoded_base64_authorization_header
                email, password = token.split(':')
                return email, password
        return None, None

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str
                                     ) -> TypeVar('User'):
        """
         returns the User instance based on his email and password.
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        results = User.search({"email": user_email})
        if len(results) == 0:
            return None
        for user in results:
            if user.is_valid_password(user_pwd):
                return user
        return None
