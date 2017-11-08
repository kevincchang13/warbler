from flask import Blueprint, make_response, jsonify, request
import jwt
from functools import wraps
from flask_restful import Api, Resource, reqparse, marshal_with, fields
from project.warblers.models import Warbler
from project.users.models import User
from project import db, bcrypt
from sqlalchemy import desc

import os

# for marshal_with
warbler_blueprint = Blueprint('warblers', __name__)
warblers_api = Api(warbler_blueprint)

user_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'profile_img' : fields.String
}

warbler_fields = {
    'id': fields.Integer,
    'message': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'user': fields.List(fields.Nested(user_fields)),
    'img_url' : fields.String
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403
        try:
            data = jwt.decode(token.split(" ")[1], os.environ.get('SECRET_KEY'))
        except:
            return jsonify({'message' : 'Token is invalid'}), 403
        return f(*args, **kwargs)

    return decorated


# def db_get_messages(user_id):
#     user = User.query(user_id)
#     return user.messages

# @warblers_api.resource('/')
class WarblersAPI(Resource):
    # @token_required
    def post(self, user_id): #create new wablereressss
        print('WarblersAPI')
        content = request.get_json()
        warble = Warbler(content['message'], content['img_url'], user_id)
        db.session.add(warble)
        db.session.commit()
        return jsonify({'message' : 'need message id'})

    @marshal_with(warbler_fields)
    def get(self, user_id):
        warblers = Warbler.query.filter_by(user_id=user_id).order_by(desc('created_at')).limit(100).all()
        return warblers

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
        return warblers

warblers_api.add_resource(WarblersAPI, '/<string:user_id>')
warblers_api.add_resource(WarblerAPI, '/<string:user_id>/<string:warbler_id>')
warblers_api.add_resource(WarblersAll, '/')

