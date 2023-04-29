#!/usr/bin/env python3
"""
This module Implements a
hash_password function that expects one
string argument name password and returns
a salted, hashed password, which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    hashes the password and returns the
    hashed `randomly generated salted` password.
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check and validate if hashed_password is equal to password
    returns True or False based on the outcome
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
