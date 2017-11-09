from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column('pessoa_id', db.Integer, primary_key=True)
    nome = db.Column(db.String(100))


class Telefone(db.Model):
    id = db.column('telefone_id', db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))

class Email(db.Model):
    id = db.column('email_id', db.Integer, primary_key=True)
    email = db.Column(db.String(60)


