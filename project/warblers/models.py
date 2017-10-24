from project import db

class Warbler(db.Model):
    __tablename__ = 'warblers'

    id = db.Column(db.Integer, primay_key=True)
    message = db.Column(db.Text)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    def __init__(self, message, user_id){
        self.message = message
        self.user_id = user_id
    }