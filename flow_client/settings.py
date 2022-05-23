from datetime import timedelta
import logging
import os
import json
import sys

log = logging.getLogger(__name__)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG set is set to True if env var is "True"
DEBUG = os.getenv("DEBUG", "False") == "True"

FLOW_CLIENT_CONFIG = os.getenv("FLOW_CLIENT_CONFIG")

try:
    oidc_config = json.loads(FLOW_CLIENT_CONFIG)
except (json.JSONDecodeError, TypeError) as err:
    log.error("Unable to load oidc_config from FLOW_CLIENT_CONFIG")
    log.debug("Error: %s", str(err))
    sys.exit("A flow client config is necessary for the application to run")

FLOW_ISSUER = oidc_config["flow_issuer"]
FLOW_CLIENT_ID = oidc_config["flow_client_id"]
FLOW_CLIENT_SECRET = oidc_config["flow_client_secret"]
FLOW_REDIRECT_URI = oidc_config["flow_redirect_uri"]
FLOW_CLIENT_ISSUER = oidc_config["flow_client_issuer"]
FLOWS = oidc_config["flows"]
KEYS = oidc_config["keys"]

VALID_FOR = timedelta(
    days=oidc_config["flow_request_validity"]["days"],
    seconds=oidc_config["flow_request_validity"]["seconds"],
)

KEYCLOAK_CLIENT_ID = oidc_config["keycloak_client_id"]
KEYCLOAK_CLIENT_SECRET = oidc_config["keycloak_client_secret"]
KEYCLOAK_METADATA_URL = oidc_config["keycloak_metadata_url"]

SESSION_SECRET = oidc_config["session_secret"]
