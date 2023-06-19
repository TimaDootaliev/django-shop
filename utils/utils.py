from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
from dataclasses import dataclass


def now():
    return datetime.now().strftime("-%d-%m-%Y-%H-%M-%S")


def get_tokens_for_user(user):
    @dataclass
    class Token:
        refresh: str
        access: str

    refresh = RefreshToken.for_user(user)

    return Token(refresh, refresh.access_token)
