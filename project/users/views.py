from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.users.models import User
from project import db, bcrypt

users_api = Api(Blueprint('Users_api', __name__))

@users_api.resource('/')
    class UserAPI(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='username')
            parser.add_argument('password', type=str, help='password')
            args = parser.parse_args()
            
