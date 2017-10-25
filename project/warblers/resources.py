from flask import Blueprint, request, make_response, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project.users.models import User
from project import db, bcrypt

warbler_blueprint = Blueprint('warblers', __name__)   
warblers_api = Api(warbler_blueprint)

warbler_fields = {
    'message': fields.String
}

# def db_get_messages(user_id):
#     user = User.query(user_id)
#     return user.messages

# @warblers_api.resource('/')
class WarblersAPI(Resource):
    def post(self, user_id): #create new wablereressss
        content = request.get_json()
        warble = Warbler(content['message'], user_id)
        db.session.add(warble)
        db.session.commit()
        return

    @marshal_with(warbler_fields)
    def get(self, user_id): #get all wablererss for specific user
        return User.query.get(user_id).messages.all()

class WarblerAPI(Resource):
    def get(self, warbler_id, user_id):
        warble = Warbler.query.get_or_404(warbler_id)
        resource_fields = {
            'message': fields.String
        }
        return marshal(warble, resource_fields)
        
    def delete(self, warbler_id, user_id):
        pass

warblers_api.add_resource(WarblersAPI, '/<string:user_id>')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>/<string:warbler_id>')
