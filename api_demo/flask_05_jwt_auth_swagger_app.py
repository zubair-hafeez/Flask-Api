from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask_restx import Api, Resource

app = Flask(__name__)

# Configure JWT
app.config["JWT_SECRET_KEY"] = "slj234jofsjfosdijufoow4rnsgi"  # Change this secret key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 30  # Set the expiration time 30 seconds

jwt = JWTManager(app)

# Initialize API with Flask-RESTx
api = Api(
    app,
    version="1.0",
    title="Flask App using JWT",
    description="A simple API implementing JWT",
)

# Dummy user database for demonstration purposes
users = {"user1": "password1", "user2": "password2"}

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# Route for basic demonstration
@api.route("/", methods=["GET"])
class Demo(Resource):
    def get(self):
        """Endpoint for a simple hello world message."""
        return "Hello, World"

# Route for user login
@api.route("/login", methods=["POST"])
class Login(Resource):
    def post(self):
        """
        User login endpoint.
        Validates user credentials and returns a JWT token.
        """
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        # Validate user credentials
        if users.get(username) != password:
            return jsonify({"msg": "Bad username or password"}), 401

        # Create JWT token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

# Route for protected endpoint
@api.route("/items", methods=["GET"])
class Secure(Resource):
    @jwt_required()
    def get(self):
        """
        Protected endpoint.
        Requires a valid JWT token to access.
        """
        current_user = get_jwt_identity()
        return jsonify(current_user,items)

# Run the Flask application
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)

