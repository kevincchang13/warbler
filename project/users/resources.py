from flask import Blueprint, make_response, jsonify, request
from project import app
import jwt
import datetime
from flask_restful import Api, Resource, fields, marshal
from project.users.models import User
from project import db, bcrypt
from flask_jwt import JWT, jwt_required, current_identity

import os

user_blueprint = Blueprint('users', __name__)
users_api = Api(user_blueprint)

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
    def get(self, user_id): # get single user
        # call database using user_id
        # send JSON response with user object

        return make_response(jsonify({ "test": "one" }))
        pass
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


users_api.add_resource(UsersAPI, '')
users_api.add_resource(UserAPI, '/<string:user_id>')
users_api.add_resource(Auth, '/auth')

