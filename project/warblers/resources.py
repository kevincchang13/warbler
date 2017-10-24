from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project import db, bcrypt

warbler_blueprint = Blueprint('warblers', __name__)   
warblers_api = Api(warbler_blueprint)

# @warblers_api.resource('/')
class Warblers(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, help='message')
        args = parser.parse_args()

warblers_api.add_resource(Warblers)