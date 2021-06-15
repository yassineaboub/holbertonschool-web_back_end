#!/usr/bin/env python3
"""Route module
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request_func() -> None:
    """ validation of all requests
    """
    if auth is not None:
        exclude_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                         '/api/v1/forbidden/']
        require_auth = auth.require_auth(path=request.path,
                                         excluded_paths=exclude_paths)
        if require_auth:
            if not auth.authorization_header(request):
                abort(401)
            if not auth.current_user(request):
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ inexistence
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def request_unauthorized(error) -> str:
    """ unauthorized requests
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def request_forbidden(error) -> str:
    """ Authentication without access
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
