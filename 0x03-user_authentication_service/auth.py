#!/usr/bin/env python3
"""
Contains utility authentication functions
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
     takes in a password string arguments
     and returns bytes
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
