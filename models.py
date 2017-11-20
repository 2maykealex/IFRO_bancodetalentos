from app import db
from sqlalchemy.orm import relationship

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

class Aluno(Pessoa):
    #id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    matricula = db.Column(db.Integer, primary_key=True)

    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))

    alunos = relationship('Pessoa', backref= 'Aluno')

    def __init__(self, cpf, matricula, nome, email, password, tipo):        
        self.cpf = cpf
        self.matricula = matricula

        super().__init__(nome, email, password, tipo)

        # super().nome = nome
        # super().email = email
        # super().password = password

    def __repr__(self):
        return '<Aluno %r>' % self.matricula

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))
    
    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))

    telefones = relationship('Pessoa', backref= 'Telefone')

    def __init__(self, email):
        self.telefone = telefone

    def __repr__(self):
        return '<Telefone %r>' % self.telefone

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60))

    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))

    emails = relationship('Pessoa', backref= 'Email')

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Email %r>' % self.email


class Endereco(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(50))
    num      = db.Column(db.String(10))
    complemento = db.Column(db.String(40))
    bairro      = db.Column(db.String(50))
    
    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))
    cidade_id = db.Column(db.String(15), db.ForeignKey('cidade.id'))

    enderecos = relationship('Pessoa', backref= 'Endereco')


    def __init__(self, nome, uf):
        self.endereco = endereco
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
    
    cidades = relationship('Endereco', backref= 'Cidade')

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '<Cidade %r>' % self.nome

class Estado(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nome  = db.Column(db.String(50))
    uf  = db.Column(db.String(2))

    estados = relationship('Cidade', backref= 'Estado')


    def __init__(self, nome, uf):
        self.nome = nome
        self.uf = uf

    def __repr__(self):
        return '<Estado %r>' % self.uf



    



