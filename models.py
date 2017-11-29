from app import db
# from sqlalchemy.ext.associationproxy import association_proxy


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    __table_args__ = {'extend_existing': True} 
    __mapper_args__ = {'polymorphic_identity': 'pessoa'}
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(100))

    # enderecos = db.relationship("Endereco", backref="pessoa", lazy='dynamic')
    telefones = db.relationship("Telefone", backref="pessoa-telefones", lazy='dynamic')
    emails    = db.relationship("Email", backref="pessoa-emails", lazy='dynamic')
    user      = db.relationship("Usuario", backref="pessoa-usuario", uselist=False)

    # telefones = association_proxy('user_newsletters', 'newsletter')

    def __init__(self, nome, email, password, tipo):
        self.nome = nome
        self.email = email
        self.password = password
        self.tipo = tipo

    def __repr__(self):
        return '<Pessoa %r %r %r>' % (self.nome, self.email, self.tipo)

    def getTelefones(self):
        for telefone in Pessoa.telefones:
            print(self.nome, ' - ', telefone)

class Usuario(db.Model):
    __tablename__ = "usuarios"    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(15), unique= True)
    password = db.Column(db.String(10))
    tipo = db.Column(db.Integer)  # 1 para IFRO - 2 para VISITANTE

    # chaves estrangeiras
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    #relacionamento one2one
    #pessoa = db.relationship("Pessoa", backref="usuario-pessoa")

    def __init__(self, user, password):
        self.user = user
        self.password = password

class Aluno(Pessoa):
    __tablename__ = "alunos"
    __table_args__ = {'extend_existing': True} 
    __mapper_args__ = {'polymorphic_identity': 'aluno'}

    # id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('pessoas.id'), primary_key=True)

    # id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    cpf = db.Column(db.String(11))
    matricula = db.Column(db.Integer)

    # chaves estrangeiras
    #pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    #rel
    telefones = db.relationship("Telefone", backref="tel-aluno", lazy='dynamic')

    def __init__(self, cpf, matricula, nome, email, password, tipo):
        self.cpf = cpf
        self.matricula = matricula

        super().__init__(nome, email, password, tipo)

        # super().nome = nome
        # super().email = email
        # super().password = password

    def __repr__(self):
        return '<Aluno %r>' % self.nome

class Telefone(db.Model):
    __tablename__ = "telefones"
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(15))

    # chaves estrangeiras
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    def __init__(self, telefone):
        self.telefone = telefone

    def __repr__(self):
        return '<Telefone %r %r>' % (self.telefone, self.pessoa_id)

class Email(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60))

    # chaves estrangeiras
    pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoas.id'))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Email %r>' % self.email


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






