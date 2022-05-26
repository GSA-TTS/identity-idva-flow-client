import logging

import fastapi
import starlette_prometheus
from authlib.integrations import starlette_client as oauth_client
from starlette import requests as server
from starlette import responses
from starlette.middleware import sessions

from flow_client import settings, sig_gen

logging.basicConfig(level=logging.INFO)

app = fastapi.FastAPI()

app.add_middleware(sessions.SessionMiddleware, secret_key=settings.SESSION_SECRET)

app.add_middleware(starlette_prometheus.PrometheusMiddleware)
app.add_route("/metrics/", starlette_prometheus.metrics)

oauth = oauth_client.OAuth()
oauth.register(
    name="keycloak",
    client_id=settings.KEYCLOAK_CLIENT_ID,
    client_secret=settings.KEYCLOAK_CLIENT_SECRET,
    server_metadata_url=settings.KEYCLOAK_METADATA_URL,
    client_kwargs={"scope": "openid profile"},
)


@app.get("/")
async def homepage(request: server.Request):

    user = request.session.get("user")
    if not user:
        return responses.HTMLResponse('<a href="/login">login</a>')

    html = ""
    for flow in settings.FLOWS:
        html += f'<div><a href="/flow/{flow}">flow: {flow}</a></div>'
    html += '<div><a href="/logout">logout</a></div>'
    return responses.HTMLResponse(html)


@app.get("/login")
async def login(request: server.Request):
    redirect_uri = request.url_for("auth")
    return await oauth.keycloak.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: server.Request):
    try:
        token = await oauth.keycloak.authorize_access_token(request)
    except oauth_client.OAuthError as error:
        return responses.HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return responses.RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: server.Request):
    request.session.pop("user", None)
    return responses.RedirectResponse(url="/")


@app.get("/flow/{flow_name}")
async def flow(flow_name, request: server.Request):

    user = request.session.get("user")
    if not user:
        return responses.HTMLResponse('<a href="/login">login</a>')

    if flow_name not in settings.FLOWS:
        return responses.HTMLResponse("no such flow", status_code=404)

    url = settings.FLOWS[flow_name]
    request = sig_gen.gen_sig_url(url, settings.VALID_FOR)
    logging.info(
        "Url generated for user %s (%s)\nUrl: %s",
        user.get("sub", "no subject"),
        user.get("preferred_username", ""),
        request.url,
    )
    return responses.RedirectResponse(url=request.url, status_code=302)


@app.get("/jwks.json")
async def flow():
    public_key_fields = ["kty", "e", "use", "kid", "alg", "n"]
    public_key = {
        key: value
        for (key, value) in settings.KEYS[0].items()
        if key in public_key_fields
    }
    return {"keys": [public_key]}
