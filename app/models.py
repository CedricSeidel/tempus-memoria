from app import db
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column("password", db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    is_admin = db.Column(db.Boolean, default=False)
    entries = db.relationship('TimeEntry', backref='user', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    entries = db.relationship('TimeEntry', backref='category', lazy=True)

class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
