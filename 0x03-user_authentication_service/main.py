#!/usr/bin/env python3
"""
End-to-end integration test.
Using assert to validate the response’s expected
"""
import requests
URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """ test user registration """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/users', data=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'register_user'")


def log_in_wrong_password(email: str, password: str) -> None:
    """ test user login with wrong password"""
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    assert response.status_code == 401, "Test fail"
    print("Test pass: 'log_in_wrong_password'")


def profile_unlogged() -> None:
    """ test profile view while not logged in"""
    data = {"session_id": ""}
    response = requests.get(f'{URL}/profile', data=data)
    assert response.status_code == 403, "Test fail"
    print("Test pass: 'profile_unlogged'")


def log_in(email: str, password: str) -> str:
    """ test the login endpoint"""
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'log_in'")
    session_id = response.cookies.get("session_id")
    return session_id


def profile_logged(session_id: str) -> None:
    """ test profile view while logged in"""
    data = {"session_id": session_id}
    response = requests.get(f'{URL}/profile', cookies=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'profile_logged'")


def log_out(session_id: str) -> None:
    """ test log out view"""
    data = {"session_id": session_id}
    response = requests.delete(f'{URL}/sessions', cookies=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'log_out'")


def reset_password_token(email: str) -> str:
    """ test reset password token view"""
    data = {"email": email}
    response = requests.post(f'{URL}/reset_password', data=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'reset_password_token'")
    reset_token = response.json().get("reset_token")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ test password update """
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(f'{URL}/reset_password', data=data)
    assert response.status_code == 200, "Test fail"
    print("Test pass: 'update_password'")


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
