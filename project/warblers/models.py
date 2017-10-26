from project import db
import datetime

class Warbler(db.Model):
    __tablename__ = 'warblers'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )
    user = db.relationship(
        'User',
        lazy='dynamic',
        backref=db.backref('warbler')
    )

    def __init__(self, message, user_id) :
        self.message = message
        self.user_id = user_id
