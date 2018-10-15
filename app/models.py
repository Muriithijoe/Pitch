from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):

   __tablename__ = 'pitches'

   id = db.Column(db.Integer,primary_key=True)
   pitch_content = db.Column(db.String)
   pitch_category= db.Column(db.String(255))
   user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


   def save_pitch(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def clear_pitches(cls):
       Pitch.all_pitches.clear()

   @classmethod
   def get_pitches(cls,id):
       pitches = Pitch.query.filter_by('-id').all()
       return pitches

   @classmethod
   def get_category(cls, ref):

       category = Pitch.query.filter_by(pitch_category=ref).order_by('-id').all()
       return category



class Comment(db.Model):
   __tablename__ = 'comments'

   id = db.Column(db.Integer,primary_key=True)
   comment_content= db.Column(db.String())
   pitch_id = db.Column(db.Integer)
   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

   def save_comment(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_comments(cls, id):
       comments = Comment.query.filter_by(pitch_id=id).all()
       return comments

   def __repr__(self) :
       return f'User {self.name}'
