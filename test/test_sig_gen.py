from datetime import timedelta
from urllib.parse import parse_qs, urlparse

from flow_client import settings, sig_gen
from jose import constants, jwk, jwt


def test_gen_sig_url() -> None:
    """test get"""
    ipd_url = "https://example.com"
    valid_for = timedelta(days=1, seconds=0)
    request = sig_gen.gen_sig_url(ipd_url, valid_for)
    url = urlparse(request.url)
    query = parse_qs(url.query)
    request_jwt = query["request"][0]
    key = jwk.construct(settings.KEYS[0], constants.ALGORITHMS.RS256)
    validation_options = {
        "require_aud": True,
        "require_exp": True,
        "require_iss": True,
    }
    jwt.decode(
        request_jwt, key, audience=settings.FLOW_ISSUER, options=validation_options
    )
