from . import db,login_manager
from flask_login import current_user,UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime



class Quotes:
    '''
    Quotes  class to define quotes Objects
    '''
    def __init__(self,id,author,quote,permalink):
        self.id=id
        self.author=author
        self.quote=quote
        self.permalink=permalink 
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User (UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email = db.Column(db.String(255), unique = True,nullable = False)
    hashed_password = db.Column(db.String(255),nullable = False)
    post = db.relationship('Post', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    
    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.hashed_password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "User: %s" %str(self.username)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment', backref='post', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_post(id):
        post = post.query.filter_by(id=id).first()

        return post

    def __repr__(self):
        return f'Post {self.title}'

class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    subscriber = db.relationship('Subscriber', backref='comment', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def get_comment(id):
        comment = Comment.query.all(id=id)
        return comment


    def __repr__(self):
        return f'Comment {self.comment}'

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'),nullable=False)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'