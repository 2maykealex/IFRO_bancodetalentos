import models
from app import db
from models import Aluno
from models import Pessoa
from models import Endereco
from models import Cidade
from models import Estado
from models import Telefone
from models import Email

db.drop_all()

db.create_all()

aluno = Aluno('22222222222', '12345', 'mayke', 'mayke.suporte@gmail.com','123', 1)
db.session.add(aluno)
db.session.commit()

Pessoa.

