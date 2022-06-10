import datetime
import secrets
import time

import requests
from jose import constants, jwk, jwt

from flow_client import settings

NONCE_BYTES = 16
STATE_BYTES = 24

public_key_fields = ["kty", "e", "use", "kid", "alg", "n"]


def public_key(jwk):
    """get public key from jwk"""
    return {key: value for (key, value) in jwk.items() if key in public_key_fields}


def gen_sig_url(url: str, valid_time: datetime.timedelta):

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
        "state": secrets.token_urlsafe(STATE_BYTES),
        "redirect_uri": settings.FLOW_REDIRECT_URI,
        "nonce": secrets.token_urlsafe(NONCE_BYTES),
        "request": encoded_jwt,
    }

    return requests.Request("GET", url, params=query).prepare()
