import models
from models import Pessoa
from models import Aluno
from models import Telefone
from models import Endereco
from models import Cidade
from models import Estado


import models
from models import Pessoa
from models import Aluno
import app
from app import db
db.drop_all()

db.create_all()

# tel1 = Telefone('6932234455')
# endereco = Endereco('Rua Jacy', '2748', 'apto 01', 'Roque')

aluno = Aluno('22222222222', '12345', 'mayke', 'mayke.suporte@gmail.com','123', 1)
aluno.apelido = ''
aluno.endereco = 'rua jacy'
aluno.num = '2748'
aluno.complemento = 'apto 1'
aluno.bairro = 'Roque'
aluno.cidade = 'Porto Velho'
aluno.uf = 'RO'
aluno.telefone = '69 9 9246-1190'






# aluno.telefones.append(tel1)
# aluno.enderecos.append(endereco)


db.session.add(aluno)
db.session.commit()
