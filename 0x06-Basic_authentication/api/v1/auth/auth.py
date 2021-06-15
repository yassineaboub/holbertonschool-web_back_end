#!/usr/bin/env python3
"""module for API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """all authentication system that will be implemented
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if path require authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        slash_tolerant = True

        for excluded_path in excluded_paths:
            path_safe_slash = path
            excluded_path_safe_slash = excluded_path

            if slash_tolerant:
                if path_safe_slash[-1] != '/':
                    path_safe_slash += '/'
                if excluded_path_safe_slash[-1] != '/':
                    excluded_path_safe_slash += '/'

            if excluded_path_safe_slash[-2] == '*':
                if excluded_path_safe_slash[:-2] in path_safe_slash:
                    return False

            if path_safe_slash == excluded_path_safe_slash:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Getting authorization
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        """
        return None
