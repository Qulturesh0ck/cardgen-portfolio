import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()

###UPDATED TO REFLECT PROPER CARD STRUCTURE###

class Card(db.Model):
    __tablename__ = 'cards'
    __table_args__ = {'extend_existing': True}
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.String(250), nullable=True)
    bp = db.Column(db.String(4), nullable=True)
    hp = db.Column(db.String(4), nullable = True)
    
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self,name: str, image: str, description: str, bp: str, hp: str,  user_id: int):
        self.user_id = user_id
        self.name = name
        self.image = image
        self.description = description
        self.bp = bp
        self.hp = hp
    def serialize(self):
        return {
            'card_id': self.card_id,
            'name': self.name,
            'image':self.image,
            'description' : self.description,
            'bp': self.bp,
            'hp' :self.hp, 
            'user_id': self.user_id 
        }
    

class GeneratedCard(db.Model):
    __tablename__ = 'generated_cards'
    __table_args__ = {'extend_existing': True}
    gen_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    imagepath = db.Column(db.String, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.card_id'), nullable=False)
    
    def __init__(self, imagepath:str, card_id: int,  user_id: int):
        self.imagepath = imagepath
        self.user_id = user_id
        self.card_id = card_id
    def serialize(self):
        return {
            'imagepath' : self.imagepath,
            'card_id': self.card_id,
            'user_id': self.user_id,
            'gen_id' : self.gen_id

        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    cards = db.relationship('Card', backref='user',cascade="all,delete", foreign_keys=[Card.user_id])

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
        }
    
