from flask import Blueprint, make_response, jsonify, request
from flask_restful import Api, Resource
from project.users.models import User
from project import db

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



users_api.add_resource(UsersAPI, '')
users_api.add_resource(UserAPI, '/<string:user_id>')

