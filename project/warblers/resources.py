from flask import Blueprint, request, make_response, jsonify
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project.users.models import User
from project import db, bcrypt
from sqlalchemy import desc

warbler_blueprint = Blueprint('warblers', __name__)
warblers_api = Api(warbler_blueprint)

user_fields = {
    # 'id': fields.Integer,
    # 'email': fields.String,
    'username': fields.String
}

warbler_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    # 'user': fields.List(fields.Nested(user_fields))
    'username': fields.String(attribute='user.username')
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
        warblers = Warbler.query.order_by(desc('created_at')).limit(100).all()
        # warblers = [{"message": w.message, "created_at": w.created_at, "username": w.user.username} for w in warbs]
        return warblers

warblers_api.add_resource(WarblersAPI, '/<string:user_id>')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>/<string:warbler_id>')
warblers_api.add_resource(WarblersAll, '')
