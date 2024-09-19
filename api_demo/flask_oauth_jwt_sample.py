## pip install authlib

from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
# app.secret_key = 'slj234jofsjfosdijufoow4rnsgi'  # Change this to a random secret key
app.config["JWT_SECRET_KEY"] = "slj234jofsjfosdijufoow4rnsgi"

jwt = JWTManager(app)

# OAuth Configuration
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id="google_client_id",  ##Get it from Environment Variables
    client_secret="google_client_secret",  ##Get it from Environment Variables
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    client_kwargs={"scope": "openid profile email"},
)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/login")
def login():
    redirect_uri = url_for("authorize", _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route("/authorize")
def authorize():
    token = google.authorize_access_token()
    resp = google.get("userinfo", token=token)
    user_info = resp.json()
    # Create a JWT token after successful OAuth
    access_token = create_access_token(identity=user_info["email"])
    return jsonify(access_token=access_token, user_info=user_info)


if __name__ == "__main__":
    app.run(ssl_context="adhoc")  # Important: OAuth2 requires HTTPS
