from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
#
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False, nullable=False)
    
    #@property
    #def password(self):
    #    raise AttributeError('`password` is not a readable attribute')
    #
    #@password.setter
    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method='sha256'
            )
        
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<user %r>' % self.username
    
    @staticmethod
    def generate_fake(count=100, **kwargs):
        """Generate a number of fake users for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed
        from faker import Faker

        fake = Faker()

        seed()
        for i in range(count):
            u = User(
                username=fake.username(),
                email=fake.email(),
                password='password',
                confirmed=True,
                **kwargs)
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
