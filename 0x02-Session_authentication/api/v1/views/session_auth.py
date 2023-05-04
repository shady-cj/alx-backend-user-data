#!/usr/bin/env python3
"""
Creating views for session auth
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False)
def login_view():
    """
    Implemented a login view
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    found_users = User.search({"email": email})
    if len(found_users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = None
    for u in found_users:
        if u.is_valid_password(password):
            user = u
    if user is None:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    resp = jsonify(user.to_json())
    resp.set_cookie(getenv("SESSION_NAME"), session_id)
    return resp


@app_views.route('/auth_session/logout', methods=["DELETE"],
                 strict_slashes=False)
def logout_view():
    """
    Handles the logout view
    """
    from api.v1.app import auth
    session_destroyed = auth.destroy_session(request)
    if not session_destroyed:
        abort(404)
    return jsonify({}), 200
