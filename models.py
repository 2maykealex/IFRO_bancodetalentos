from app import db
#from sqlalchemy.ext.associationproxy import association_proxy


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(10))
    tipo = db.Column(db.Integer)   # 1 para IFRO - 2 para VISITANTE

    telefones = db.relationship("Telefone", backref="pessoa", lazy='dynamic')
    #enderecos = db.relationship("Endereco", backref="Pessoa", lazy='dynamic')

    #telefones = association_proxy('user_newsletters', 'newsletter')

    def __init__(self, nome, email, password, tipo):
        self.nome = nome
        self.email = email
        self.password = password
        self.tipo = tipo

    def __repr__(self):
        return '<Pessoa %r>' % self.nome

class Telefone(db.Model):
    __tablename__ = "telefones"
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))
    
    # chaves estrangeiras
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    #telefones = relationship('Pessoa', backref= 'Telefone')

    #pessoa = db.relationship('Pessoa', enable_typechecks=False)

    def __init__(self, telefone):
        self.telefone = telefone

    def __repr__(self):
        return '<Telefone %r>' % self.telefone

# class Email(db.Model):
#     __tablename__ = "emails"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(60))
#
#     # chaves estrangeiras
#     pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoas.id'))
#
#     emails = relationship('Pessoa', backref= 'Email')
#
#     def __init__(self, email):
#         self.email = email
#
#     def __repr__(self):
#         return '<Email %r>' % self.email
#

# class Endereco(db.Model):
#     __tablename__ = "enderecos"
#     #id    = db.Column(db.Integer, primary_key=True)
#     endereco = db.Column(db.String(50))
#     num      = db.Column(db.String(10))
#     complemento = db.Column(db.String(40))
#     bairro      = db.Column(db.String(50))
#     tipoEndereco = db.Column(db.String(20))
#
#     # chaves estrangeiras
#     pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoa.id'))
#     cidade_id = db.Column(db.String(15), db.ForeignKey('cidade.id'))
#
#     enderecos = relationship('Pessoa')
#
#     def __init__(self, endereco, num, complemento, bairro):
#         self.endereco = endereco
#         self.num = num
#         self.complemento = complemento
#         self.bairro = bairro
#
#     def __repr__(self):
#         return '<Endereco %r>' % self.endereco

class Aluno(Pessoa):
    __tablename__ = "alunos"
    #id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    cpf = db.Column(db.String(11))
    matricula = db.Column(db.Integer, primary_key=True)

    # chaves estrangeiras
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    alunos = db.relationship('Pessoa')

    def __init__(self, cpf, matricula, nome, email, password, tipo):
        self.cpf = cpf
        self.matricula = matricula

        super().__init__(nome, email, password, tipo)

        # super().nome = nome
        # super().email = email
        # super().password = password

    def __repr__(self):
        return '<Aluno %r>' % self.nome


# class Cidade(db.Model):
#     __tablename__ = "cidades"
#     id   = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(50))
#
#     # chaves estrangeiras
#     estado_id = db.Column(db.String(15), db.ForeignKey('estado.id'))
#
#     cidades = relationship('Endereco', backref= 'Cidade')
#
#     def __init__(self, nome):
#         self.nome = nome
#
#     def __repr__(self):
#         return '<Cidade %r>' % self.nome
#
# class Estado(db.Model):
#     __tablename__ = "estados"
#     id  = db.Column(db.Integer, primary_key=True)
#     nome  = db.Column(db.String(50))
#     uf  = db.Column(db.String(2))
#
#     estados = relationship('Cidade', backref= 'Estado')
#
#
#     def __init__(self, nome, uf):
#         self.nome = nome
#         self.uf = uf
#
#     def __repr__(self):
#         return '<Estado %r>' % self.uf



    



