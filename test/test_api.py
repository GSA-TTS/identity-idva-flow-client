from fastapi import testclient

from flow_client import oidc


def test_jwks(client: testclient.TestClient) -> None:
    """test jwks endpoint"""

    response = client.get("/jwks.json")
    assert response.status_code == 200
    content = response.json()
    for jwk in content["keys"]:
        for k in jwk.keys():
            assert k in oidc.public_key_fields
    print(content)
