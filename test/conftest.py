import os

os.environ[
    "FLOW_CLIENT_CONFIG"
] = """{
      "flow_issuer": "https://example.com/v1/auth/co_random_string",
      "flow_client_id": "client_id_random_string",
      "flow_client_secret": "client_secret_random_string",
      "flow_redirect_uri": "https://example.com/client/",
      "flow_client_issuer": "https://example.com/",
      "flows": {
          "flow_name": "https://example.com/v1/auth/co_random_string/policy/policy_random_string/authorize"
      },
      "keys": [{
            "p": "9KyqbFN7CQg3zVIALZsZE-_wuwmR-wRFCSmP-84CfgGYPaknlUcr7zOenPapByABOMwNbTSVhIlw0FkQ0Rb25JfSmZij4Wuqt8SxQCryNg_Bc_CKBH2oklUBNq7ZMXDAfhfYKGPB_JBtw9kTviV7WL-5T-jJOBxqNNPHaSV2XSU",
            "kty": "RSA",
            "q": "jfxfRlIk2-Lz5orvGMxalv6mi051WowiStXPGu2XQbS9JG4yv77sNWAGL3Doc1e_UbEhy0fV8VeOfEUDR4AIuBFtOrwaZCrza2zjbLRi1J-a1M-eVut4nCCjF_gIIeMLJnFYPEvjiE1uzDqI37S5rNWXUnHicK8DgPienwAYklU",
            "d": "ZQRKqiOkwdNBpsmGRp53k7VpVHgw_AFbFJQfcVpkBk7LR3qdkSA6kKGroAL4gF7yi9TEfp4jipmSRbSbUQBXbGRwlVAjAcjj1cLXVWe4EM5iEocGGGP4fjmeCdsDRSM29rgUbtlJwhQKBt_WV7JChmUL5YgrdXkBV7xFR73knTCn9qeapbu0OAvEB4LvTNxhYJdIiT755WmIkXcSedFcErsV5XGCqX8ATAKfyaLRHQF1-LM4m8_w7Ke6nGrSVCwrnfR36LqLlog7FBOmVnubBIXBoV1qCr7l32K91UUqV4y9yYCNTDCtA8LadhL_32JEvrCXCV-0JbVTRxch8g3c0Q",
            "e": "AQAB",
            "use": "sig",
            "kid": "92N53-xL_WL4xy-9IWrUUhCAc4cnsFrQrej-_ftSa-k",
            "qi": "g1ZqX4HYpUls-4bcbSs0WvbOURZDGSTgRdcvK4u8Rr_tZvxbesNsnyLLCrJZ0Hu7aiI19xqQb4KtN0HE7iKrIr1aFW3oZcpFc5gOFXX3p3KrmGF7bvSuaM3wdCDmldX1zT9_z1FAYs28EKRuv4SXAqJLljfMODPn49WL88qtSA0",
            "dp": "SoxRYLAOzLG0TtqtMzgObASvVE2WLOUgI6qGNDKQj9Psjtz7MoB84mTX7vs4hPM7bBLABIYBCGDX_qMkfJCCqSOZBzN6uzQSz-seFm7_XXlvd-PSKYwf0HYV6JNdmbLA86pQMf4zHMDksMdzPHwvGNtRmwdSR8ZglbfxChhf-AE",
            "alg": "RS256",
            "dq": "N6K8coGdj8vOZnfqWH06wg_mko-bzG88wLYnARY4PrbjpnLHz_qv8_o8cjp72zZ28TvHUjBD1N3KJ0ejkVDKGdY6RtmOPdHWsDFqrB3C3C3uLZVtJgH-sK7ZOXsnNKASrm2bdYUHE1HEKKKHH6FhYCgRs2yMnjr11IOXJBaVikE",
            "n": "h7RO5LWURrcwIAwoqJM2_Vg-DnWq2tgZLV7-8UekG_Pa5sj-7ENVoNJie9LPpATHsWjc4ApsIlh3mPmTwJD1pod25vJnxkF8qyq_KxJmdznTtIvm6e8-e7HrGgR3XwpP2IiereFTgshh1DbKWip8K41X5Ma31Dz4S5f6hYt_HcK-5JWb0Roigz0FEIR-CtztyQGl10XoBjUT644QchpgGQY8-nOhhajc7V7ed8aZAIweQS4dc3Rj7ialhDM1DWVBVYPjk3rLsxGcu6Q1yTav_4U0gZ-NHwd2Hv-Cm4pQff8V-7JjkSniJhUZxrjtOnEotGR77oM9kFgRv2BarOQHSQ"
        }],
      "flow_request_validity": {
          "days": 1,
          "seconds": 0
      },
      "keycloak_client_id": "test_client_id",
      "keycloak_client_secret": "test_client_secret",
      "keycloak_metadata_url": "https://example.com/keycloak/realms/flow/.well-known/openid-configuration",
      "session_secret": "session_secret"
}"""
