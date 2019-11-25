
from . import db
class User(db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    
    pitches =  db.relationship('Pitch', backref = 'user', lazy = "dynamic")

    def __repr__(self):
        return f'User{self.username}'
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
class Pitch(db.Model):
    __tablename__ ='pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(800))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls,catergory):
        pitches  = Pitch.query.filter_by(id=id).first()
        return pitches

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id = id).all()
        return pitches
         
    





