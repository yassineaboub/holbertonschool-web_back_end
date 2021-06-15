#!/usr/bin/env python3
"""Session Auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Dictionary representation of the User authenticated
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user_not_found_error = {"error": "no user found for this email"}
    try:
        users = User.search({'email': email})
    except KeyError:
        return jsonify(user_not_found_error), 404

    if len(users) == 0:
        return jsonify(user_not_found_error), 404

    for user in users:
        if user.is_valid_password(password):
            # Create session
            from api.v1.app import auth

            session_id = auth.create_session(user_id=user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """Logout User authenticated
    """

    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
