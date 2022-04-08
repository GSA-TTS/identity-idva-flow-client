import logging

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette_prometheus import PrometheusMiddleware, metrics

from flow_client import settings, sig_gen

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET)

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)

logging.getLogger().setLevel(logging.INFO)

oauth = OAuth()
oauth.register(
    name="keycloak",
    client_id=settings.KEYCLOAK_CLIENT_ID,
    client_secret=settings.KEYCLOAK_CLIENT_SECRET,
    server_metadata_url=settings.KEYCLOAK_METADATA_URL,
    client_kwargs={"scope": "openid profile"},
)


@app.get("/")
async def homepage(request: Request):

    user = request.session.get("user")
    if not user:
        return HTMLResponse('<a href="/login">login</a>')

    html = ""
    for flow in settings.FLOWS:
        html += f'<div><a href="/flow/{flow}">flow: {flow}</a></div>'
    html += '<div><a href="/logout">logout</a></div>'
    return HTMLResponse(html)


@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth")
    return await oauth.keycloak.authorize_redirect(request, redirect_uri)


@app.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.keycloak.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f"<h1>{error.error}</h1>")
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/")


@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")


@app.get("/flow/{flow_name}")
async def flow(flow_name, request: Request):

    user = request.session.get("user")
    if not user:
        return HTMLResponse('<a href="/login">login</a>')

    if flow_name not in settings.FLOWS:
        return HTMLResponse("no such flow", status_code=404)

    url = settings.FLOWS[flow_name]
    request = sig_gen.gen_sig_url(url, settings.VALID_FOR)
    return RedirectResponse(url=request.url, status_code=302)


@app.get("/jwks.json")
async def flow():
    public_key = {
        k: v
        for (k, v) in settings.KEYS[0].items()
        if k in ["kty", "e", "use", "kid", "alg", "n"]
    }
    return {"keys": [public_key]}
