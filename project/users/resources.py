from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource, fields, marshal_with
from project.users.models import User
from project import db, bcrypt
from flask_jwt import JWT, jwt_required, current_identity

user_blueprint = Blueprint('users', __name__)
users_api = Api(user_blueprint)

warbler_fields = {
    'message': fields.String
}

user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'messages': fields.List(fields.Nested(warbler_fields))
}

# @users_api.resource('/')
class UsersAPI(Resource):
    def get(self): #get all users
        # call database using user_id
        # send JSON response with user object
        pass

    def post(self): #create new user
        content = request.get_json()
        user = User(content['email'], content['username'], content['name'], content['password'])
        db.session.add(user)
        db.session.commit()
        # parse JSON body
        # call database to create user
        # send JSON response of created user

class UserAPI(Resource):
    @marshal_with(user_fields)
    def get(self, user_id): # get single user
        return User.query.get_or_404(user_id)


    def delete(self, user_id): #delete user
        pass

class Auth(Resource):
    def post(self):
        content = request.get_json()
        user = User.query.filter_by(username=content['username']).first()
        if user:
            authenticated_user=bcrypt.check_password_hash(user.password, content['password'])
            if authenticated_user:
                resource_fields = {
                    'id': fields.Integer,
                    'email': fields.String,
                    'username': fields.String
                }
                return marshal(user, resource_fields)
        return False



users_api.add_resource(UsersAPI, '')
users_api.add_resource(UserAPI, '/<string:user_id>')
users_api.add_resource(Auth, '/auth')

