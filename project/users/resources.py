from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.users.models import User
from project import db, bcrypt

user_blueprint = Blueprint('users', __name__)
users_api = Api(user_blueprint)

# @users_api.resource('/')
class Users(Resource):
    def get(self):
        # call database using user_id
        # send JSON response with user object
        return make_response(jsonify({ "test": "one" }))
    def post(self):
        # parse JSON body
        # call database to create user
        # send JSON response of created user
        pass

class User(Resource):
    def get(self, user_id):
        # call database using user_id
        # send JSON response with user object
        return make_response(jsonify({ "test": "one" }))
    def delete(self, user_id):
        pass



users_api.add_resource(Users)
users_api.add_resource(User, '/<string:user_id>')
# users_api.add_resource(Tweets, '/<string:user_id>/tweets')

