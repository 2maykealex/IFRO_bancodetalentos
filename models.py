from app import db
# from sqlalchemy.ext.associationproxy import association_proxy


class Pessoa(db.Model):
    __tablename__ = "pessoas"
    __table_args__ = {'extend_existing': True} 
    __mapper_args__ = {'polymorphic_identity': 'pessoa'}
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome        = db.Column(db.String(100))
    apelido     = db.Column(db.String(100))
    endereco    = db.Column(db.String(50))
    num         = db.Column(db.String(10))
    complemento = db.Column(db.String(40))
    bairro      = db.Column(db.String(50))
    cidade      = db.Column(db.String(50))
    uf          = db.Column(db.String(50))

    telefone    = db.Column(db.String(15))
    
    #acesso ao sistema
    email    = db.Column(db.String(15), unique= True)
    password = db.Column(db.String(10))
    tipo     = db.Column(db.Integer)  # 1 para IFRO - 2 para VISITANTE




    #endereco = db.relationship("Endereco", uselist=False, back_populates="pessoa")
    #enderecos = db.relationship("Endereco", backref="pessoa-enderecos", lazy='dynamic')
    #telefones = db.relationship("Telefone", backref="pessoa-telefones", lazy='dynamic')
    #emails    = db.relationship("Email",    backref="pessoa-emails",    lazy='dynamic')

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

    
    # telefones = db.relationship("Telefone", backref="tel-aluno",       lazy='dynamic')
    # enderecos = db.relationship("Endereco", backref="aluno-enderecos", lazy='dynamic')
    # emails    = db.relationship("Email",    backref="aluno-emails",    lazy='dynamic')

    def __init__(self, cpf, matricula, nome, email, password, tipo):
        self.cpf = cpf
        self.matricula = matricula

        super().__init__(nome, email, password, tipo)

        # super().nome = nome
        # super().email = email
        # super().password = password

    def __repr__(self):
        return '<Aluno %r>' % self.nome


class Empresa(Pessoa):
    __tablename__ = "empresas"
    __table_args__ = {'extend_existing': True} 
    __mapper_args__ = {'polymorphic_identity': 'empresa'}

    # id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('pessoas.id'), primary_key=True)

    # id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    cnpj = db.Column(db.String(11))
    ie   = db.Column(db.Integer)

    # chaves estrangeiras
    #pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

    
    # telefones = db.relationship("Telefone", backref="tel-aluno",       lazy='dynamic')
    # enderecos = db.relationship("Endereco", backref="aluno-enderecos", lazy='dynamic')
    # emails    = db.relationship("Email",    backref="aluno-emails",    lazy='dynamic')

    def __init__(self, cnpj, ie, nome, email, password, tipo):
        self.cnpj = cnpj
        self.ie   = ie

        super().__init__(nome, email, password, tipo)

        # super().nome = nome
        # super().email = email
        # super().password = password

    def __repr__(self):
        return '<Aluno %r>' % self.nome



# class Telefone(db.Model):
#     __tablename__ = "telefones"
#     __table_args__ = {'extend_existing': True} 

#     id = db.Column(db.Integer, primary_key=True)
#     telefone = db.Column(db.String(15))

#     # chaves estrangeiras
#     pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

#     def __init__(self, telefone):
#         self.telefone = telefone

#     def __repr__(self):
#         return '<Telefone %r %r>' % (self.telefone, self.pessoa_id)

# class Email(db.Model):
#     __tablename__ = "emails"
#     __table_args__ = {'extend_existing': True} 

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(60))

#     # chaves estrangeiras
#     pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoas.id'))

#     def __init__(self, email):
#         self.email = email

#     def __repr__(self):
#         return '<Email %r>' % self.email

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child = relationship("Child", uselist=False, back_populates="parent")

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parent.id'))
#     parent = relationship("Parent", back_populates="child")

# class Endereco(db.Model):
#     __tablename__ = "enderecos"
#     #__table_args__ = {'extend_existing': True} 
     
#     id    = db.Column(db.Integer, primary_key=True)
#     endereco = db.Column(db.String(50))
#     num      = db.Column(db.String(10))
#     complemento = db.Column(db.String(40))
#     bairro      = db.Column(db.String(50))
#     tipoEndereco = db.Column(db.String(20))

#     # chaves estrangeiras
#     pessoa_id = db.Column(db.String(15), db.ForeignKey('pessoas.id'))
#     cidade_id = db.Column(db.String(15), db.ForeignKey('cidades.id'))

#     pessoa = db.relationship('Pessoa', back_populates="Endereco")

#     def __init__(self, endereco, num, complemento, bairro):
#         self.endereco = endereco
#         self.num = num
#         self.complemento = complemento
#         self.bairro = bairro

#     def __repr__(self):
#         return '<Endereco %r>' % self.endereco

# class Cidade(db.Model):
#     __tablename__ = "cidades"
#     __table_args__ = {'extend_existing': True} 

#     id   = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(50))

#     # chaves estrangeiras
#     estado_id = db.Column(db.String(15), db.ForeignKey('estados.id'))

#     cidades = db.relationship('Endereco', backref= 'Cidade')

#     def __init__(self, nome):
#         self.nome = nome

#     def __repr__(self):
#         return '<Cidade %r>' % self.nome

# class Estado(db.Model):
#     __tablename__ = "estados"
#     __table_args__ = {'extend_existing': True} 

#     id  = db.Column(db.Integer, primary_key=True)
#     nome  = db.Column(db.String(50))
#     uf  = db.Column(db.String(2))

#     estados = db.relationship('Cidade', backref= 'Estado')


#     def __init__(self, nome, uf):
#         self.nome = nome
#         self.uf = uf

#     def __repr__(self):
#         return '<Estado %r>' % self.uf






