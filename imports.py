import models
from models import *
from app import db

Vaga.query.join(models.Empresa).filter(models.Empresa.id == models.Vaga.empresa).all()


import models
from models import Pessoa
from models import Aluno
from models import Empresa
from models import Vaga
import app
from app import db
db.drop_all()

db.create_all()

# tel1 = Telefone('6932234455')
# endereco = Endereco('Rua Jacy', '2748', 'apto 01', 'Roque')

aluno = Aluno('22222222222', '12345', 'mayke', 'mayke.suporte@gmail.com','123', 1)
aluno.endereco = 'rua jacy'
aluno.num = '2748'
aluno.complemento = 'apto 1'
aluno.bairro = 'Roque'
aluno.cidade = 'Porto Velho'
aluno.uf = 'RO'
aluno.telefone = '69 9 9246-1190'


db.session.add(aluno)
db.session.commit()


vaga = models.Vaga()
vaga.data_inicio = '04/12/2014'
vaga.status      = 'ABERTA'
vaga.descricao   = 'tecnico em informatica'
vaga.remuneracao = '3000,00'
vaga.beneficios  = 'VA VT VR SAUDE'


db.session.add(vaga)
db.session.commit()

