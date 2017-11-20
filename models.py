from app import db

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(10))
    tipo = db.Column(db.Integer)   # 1 para IFRO - 2 para VISITANTE

    def __init__(self, nome, email, password, tipo):
        self.nome = nome
        self.email = email
        self.password = password
        self.tipo = tipo

    def __repr__(self):
        return '<Pessoa %r>' % self.nome

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))
    
    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60))

    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))

class Endereco(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(50))
    num      = db.Column(db.String(10))
    complemento = db.Column(db.String(40))
    bairro      = db.Column(db.String(50))
    
    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))
    cidade_id = db.Column(db.String(15), db.ForeignKey('cidade.id'))

    def __init__(self, nome, uf):
        self.nome = endereco
        self.num = num
        self.complemento = complemento
        self.bairro = bairro        

    def __repr__(self):
        return '<Endereco %r>' % self.endereco
    
class Cidade(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    # chaves estrangeiras
    estado_id = db.Column(db.String(15), db.ForeignKey('estado.id'))
    
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '<Cidade %r>' % self.nome

class Estado(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nome  = db.Column(db.String(50))
    uf  = db.Column(db.String(2))

    def __init__(self, nome, uf):
        self.nome = nome
        self.uf = uf

    def __repr__(self):
        return '<Estado %r>' % self.uf



    



