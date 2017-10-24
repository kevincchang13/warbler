from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project import db, bcrypt

warbler_blueprint = Blueprint('warblers', __name__)   
warblers_api = Api(warbler_blueprint)

# @warblers_api.resource('/')
class WarblersAPI(Resource):
    def get(self): #get all wablererss
        pass

class WarblerAPI(Resource):
    def post(self, user_id): #create new wablereressss
        content = request.get_json()
        warble = Warbler(content['message'], user_id)
        db.session.add(warble)
        db.session.commit()
        

    def get(self, warbler_id, user_id):
        pass

    def delete(self, warbler_id, user_id):
        pass

warblers_api.add_resource(WarblersAPI, '')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>/<string:warbler_id>')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>')
