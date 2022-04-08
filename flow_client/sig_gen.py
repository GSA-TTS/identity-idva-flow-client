import secrets
import time
from datetime import timedelta

from jose import jwt, jwk, constants
from requests import Request

from flow_client import settings


def gen_sig_url(url: str, valid_time: timedelta):

    state = secrets.token_urlsafe(24)
    nonce = secrets.token_urlsafe(16)
    epoch_time = int(time.time()) + valid_time.total_seconds()

    jwt_data = {
        "iss": settings.FLOW_CLIENT_ISSUER,
        "aud": settings.FLOW_ISSUER,
        "exp": epoch_time,
    }

    key = jwk.construct(settings.KEYS[0], constants.ALGORITHMS.RS256)

    encoded_jwt = jwt.encode(jwt_data, key, algorithm="RS256")

    query = {
        "response_type": "code",
        "client_id": settings.FLOW_CLIENT_ID,
        "scope": "openid profile",
        "state": state,
        "redirect_uri": settings.FLOW_REDIRECT_URI,
        "nonce": nonce,
        "request": encoded_jwt,
    }

    return Request("GET", url, params=query).prepare()
