from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_restx import Api, Resource, fields

app = Flask(__name__)
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(app, version='1.0', title='API with JWT', description='REST API Using JWT Token and Swagger', 
          authorizations=authorizations)

# Configure JWT
app.config["JWT_SECRET_KEY"] = "slj234jofsjfosdijufoow4rnsgi"  # Change this secret key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 30  # Set the expiration time 30 seconds
jwt = JWTManager(app)

# Dummy user database for demonstration purposes
users = {"user1": "password1", "user2": "password2"}

# Sample data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# Define models for Swagger UI
credentials_model = api.model('Credentials', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The password')
})

item_model = api.model('Item', {
    'id': fields.Integer(required=True, description='The item ID'),
    'name': fields.String(required=True, description='The item name')
})


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return "Hello, World!"


@api.route('/login')
class Login(Resource):
    @api.expect(credentials_model)
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        # Validate user credentials
        if users.get(username) != password:
            return {"msg": "Bad username or password"}, 401

        # Create JWT token
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}


@api.route('/items')
class ItemList(Resource):
    @api.doc(security='Bearer')
    @jwt_required()
    @api.marshal_list_with(item_model)
    def get(self):
        current_user = get_jwt_identity()
        return items


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5005, debug=True)
