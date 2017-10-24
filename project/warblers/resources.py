from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project import db, bcrypt

warbler_blueprint = Blueprint('warblers', __name__)   
warblers_api = Api(warbler_blueprint)

# @warblers_api.resource('/')
class Warblers(Resource):
    def get(self): #get all wablererss
        pass

class Warbler(Resource):
    def post(self, user_id): #create new wablereressss
        pass

    def get(self, warbler_id, user_id):
        pass

    def delete(self, warbler_id, user_id):
        pass

warblers_api.add_resource(Warblers)
warblers_api.add_resource(Warbler, '/<string:user_id>/<string:warbler_id>')
warblers_api.add_resource(Warbler, '/<string:user_id>')
