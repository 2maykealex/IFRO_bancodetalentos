from app import db

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(10))

    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Pessoa %r>' % self.nome

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60))


