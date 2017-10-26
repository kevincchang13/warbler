from flask import Blueprint, make_response, jsonify, request
import jwt
import datetime
from flask_restful import Api, Resource, fields, marshal_with
from project.users.models import User
from project import db, bcrypt

import os

user_blueprint = Blueprint('users', __name__)
users_api = Api(user_blueprint)

warbler_fields = {
    'message': fields.String
}

user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'name': fields.String,
    'messages': fields.List(fields.Nested(warbler_fields))
}

# def token_required(fn):
#     @wraps(fn)
#     def decorated(*args, **kwargs):
#         token = None

#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']

#         if not token:
#             return jsonify({'message': 'Token is missing'}), 401

#         try:
#             data = jwt.decode(token, os.environ.get('SECRET_KEY'))
#             current_user = User.query.filter_by(user_id=data['user_id']).first()
#         except:
#             return jsonify({'message': 'Token is ainvalid'}), 401

#         return fn(current_user, *args, **kwargs)

#     return decorated

# @users_api.resource('/')
class UsersAPI(Resource):
    @marshal_with(user_fields)
    def get(self): #get all users
        pass

    # @token_required
    def post(self): #create new user
        content = request.get_json()
        from IPython import embed; embed()
        user = User(content['email'], content['username'], content['name'], content['password'])
        db.session.add(user)
        db.session.commit()
        return {}

class UserAPI(Resource):
    # @token_required
    def get(self, user_id): # get single user
        return User.query.get_or_404(user_id)
    # @token_required
    def delete(self, user_id): #delete user
        pass

class Auth(Resource):
    def post(self):
        content = request.get_json()
        user = User.query.filter_by(username=content['username']).first()
        if user:
            authenticated_user=bcrypt.check_password_hash(user.password, content['password'])
            if authenticated_user:
                # https://www.youtube.com/watch?v=J5bIPtEbS0Q
                token = jwt.encode({'user' : user.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ.get('SECRET_KEY'))
                return jsonify({'token' : token.decode('UTF-8')})
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required'})

class Follow(Resource):
    def post(self, user_id):
        pass

    def delete(self,user_id):
        pass

users_api.add_resource(UsersAPI, '')
users_api.add_resource(UserAPI, '/<string:user_id>')
users_api.add_resource(Auth, '/auth')
users_api.add_resource(Follow, '/<string:user_id>/follow')
