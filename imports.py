import models
from models import Pessoa
from models import Aluno
from models import Telefone
import app
from app import db
db.drop_all()

db.create_all()

tel1 = Telefone('6932234455')
tel2 = Telefone('6995821422')
aluno = Aluno('22222222222', '12345', 'mayke', 'mayke.suporte@gmail.com','123', 1)
aluno.telefones.append(tel1)
aluno.telefones.append(tel2)

db.session.add(aluno)
db.session.commit()
