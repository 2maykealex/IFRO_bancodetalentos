import models
from app import db
from models import Aluno
from models import Pessoa
from models import Endereco
from models import Cidade
from models import Estado
from models import Telefone
from models import Email

import models
from models import *
import app
from app import *

db.drop_all()

db.create_all()


tel1 = Telefone('6932234455')
tel2 = Telefone('6995821422')


aluno = Aluno('22222222222', '12345', 'mayke', 'mayke.suporte@gmail.com','123', 1)
aluno.telefones.append(tel1)
aluno.telefones.append(tel2)

db.session.add(aluno)
db.session.commit()

# or
m.characters.extend([c,c2])


# or
db.session.add_all([c,c2])
# commit
db.session.commit()