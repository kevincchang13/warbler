from flask import Blueprint, request, make_response, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project.users.models import User
from project import db, bcrypt

warbler_blueprint = Blueprint('warblers', __name__)
warblers_api = Api(warbler_blueprint)

warbler_fields = {
    'message': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'username': fields.String
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

    # @marshal_with(warbler_fields)
    # def get(self, user_id): #get all wablererss for specific user
    #     return User.query.get_or_404(user_id).messages.all()

class WarblerAPI(Resource):
    @marshal_with(warbler_fields)
    def get(self, warbler_id, user_id):
        return Warbler.query.get(warbler_id)

    def delete(self, warbler_id, user_id):
        pass

class WarblersAll(Resource):
    @marshal_with(warbler_fields)
    def get(self):
       return Warbler.query.all.limit(100)

warblers_api.add_resource(WarblersAPI, '/<string:user_id>')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>/<string:warbler_id>')
warblers_api.add_resource(WarblersAll, '/')
