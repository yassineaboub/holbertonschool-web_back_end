#!/usr/bin/env python3
""" encrypt pass """
import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypt pass """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ encrypt pass """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
