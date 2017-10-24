from project import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    username = db.Column(db.Text, unique=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    messages = db.relationship(
        'User',
        lazy='dynamic',
        backref=db.backref('user')
    )

    def __init__(self, email, username, name, password):
        self.email = email
        self.username = username
        self.name = name
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user:
            authenticated_user=bcrypt.check_password_hash(user.password, password)
            if authenticated_user:
                return user
        return False
