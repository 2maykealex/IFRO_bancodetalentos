from app import db

class Pessoa(db.Model):
    id = db.Column('pessoa_id', db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

class Telefone(db.Model):
    id = db.Column('telefone_id', db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))

class Email(db.Model):
    id = db.Column('email_id', db.Integer, primary_key=True)
    email = db.Column(db.String(60))


