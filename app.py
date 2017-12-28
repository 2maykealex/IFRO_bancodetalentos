import os
from flask import Flask, render_template, request, url_for, redirect, flash
import flask_login
from flask_sqlalchemy import SQLAlchemy
import models
import config

from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret string' #Change this!

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECURITY_REGISTERABLE'] = True

db = SQLAlchemy(app) #db é uma instância de SQLAlchemy

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'teste@teste.com': {'password': '123'}}

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    email_user = models.Pessoa.query.filter_by(email=email).first()
    if email_user is None:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return #'Não existe o e-mail {} cadastrado no banco'.format(email)

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    #user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/criar_tabelas')
def criar_tabelas():
    db.create_all()
    flash('criado com sucesso')

    return redirect(url_for('index'))

@app.route('/remover_tabelas')
def remover_tabelas():
    db.drop_all()
    flash('removido com sucesso')
    return redirect(url_for('index'))

@app.route('/post_user', methods=['POST'])
def post_user():
    user = models.User(request.form['username'], request.form['email'])
    models.db.session.add(user)
    models.db.session.commit()
    flash('Usuario criado com sucesso')
    return redirect(url_for('index'))

@app.route('/post_aluno', methods=['POST']) #salvar um aluno no banco
def post_aluno():
    aluno = models.Aluno(request.form['cpf'] ,  request.form['matricula'].upper(), request.form['nome'].upper(), request.form['email'], request.form['senha'], 2)
    aluno.endereco = request.form['endereco']
    aluno.num      = request.form['num']
    aluno.complemento = request.form['complemento']
    aluno.bairro   = request.form['bairro']
    aluno.cidade   = request.form['cidade']
    aluno.uf   = request.form['uf']
    aluno.data_cadastro = datetime.now()
    
    models.db.session.add(aluno)
    models.db.session.commit()
    flash('Aluno registrado com sucesso!')
    return redirect(url_for('listarAlunos'))

@app.route('/post_empresa', methods=['POST']) #salvar um aluno no banco
def post_empresa():
    empresa = models.Empresa(request.form['fantasia'].upper(), request.form['cnpj'], request.form['ie'], request.form['nome'].upper(), request.form['email'].upper(), request.form['senha'].upper(), 2)
    empresa.endereco = request.form['endereco'].upper()
    empresa.num      = request.form['num'].upper()
    empresa.complemento = request.form['complemento'].upper()
    empresa.bairro   = request.form['bairro'].upper()
    empresa.cidade   = request.form['cidade'].upper()
    empresa.uf   = request.form['uf'].upper()
    empresa.data_cadastro = datetime.now()

    models.db.session.add(empresa)
    models.db.session.commit()
    flash('Empresa registrada com sucesso!')
    return redirect(url_for('listarEmpresas'))

@app.route('/post_vaga', methods=['POST']) #salvar um aluno no banco
def post_vaga():
    vaga = models.Vaga()
    vaga.data_inicio = datetime.now()
    vaga.status      = 'ABERTA'.upper()
    vaga.descricao   = request.form['descricao'].upper()
    vaga.remuneracao = request.form['remuneracao'].upper()
    vaga.beneficios  = request.form['beneficios'].upper()
    vaga.empresa     = request.form['empresa'].upper()

    models.db.session.add(vaga)
    models.db.session.commit()
    flash('Vaga registrada com sucesso!')
    return redirect(url_for('listarVagas'))

@app.route('/listarAlunos')    
def listarAlunos():
    alunos = models.Aluno.query.all()
    return render_template('listarAlunos.html', alunos=alunos)

@app.route('/viewAluno/<idAluno>/')   
def viewAluno(idAluno):
    aluno = models.Aluno.query.filter_by(id=idAluno).first()
    return render_template('viewAluno.html', aluno=aluno)

@app.route('/listarEmpresas')   
def listarEmpresas():
    empresas = models.Empresa.query.all()
    return render_template('listarEmpresas.html', empresas=empresas)

@app.route('/viewEmpresa/<idEmp>/')
def viewEmpresa(idEmp):
    empresa = models.Empresa.query.filter_by(id=idEmp).first()
    
    vagasEmpresa = models.Vaga.query.select_from(models.Empresa).add_columns(models.Vaga.id, models.Empresa.id, models.Empresa.nome, models.Vaga.data_inicio, models.Vaga.status, models.Vaga.descricao, models.Vaga.remuneracao, models.Vaga.beneficios
).filter(models.Empresa.id == models.Vaga.empresa).filter(models.Vaga.empresa == empresa.id).order_by(models.Vaga.data_inicio).all()
    
    return  render_template('viewEmpresa.html', empresa=empresa, vagas=vagasEmpresa)

@app.route('/listarVagas')    #Abrir Formulário de cadastro de aluno
def listarVagas():
    vagas  = models.Vaga.query.select_from(models.Empresa).add_columns(models.Empresa.nome, models.Vaga.data_inicio, models.Vaga.status, models.Vaga.descricao, models.Vaga.remuneracao, models.Vaga.beneficios
).filter(models.Empresa.id == models.Vaga.empresa).order_by(models.Vaga.data_inicio).all()

    return render_template('listarVagas.html', vagas=vagas)

@app.route('/cadAluno')    #Abrir Formulário de cadastro de aluno
def cadAluno():
    return render_template('cadAluno.html')

@app.route('/cadEmpresa')
def cadEmpresa():
    return render_template('cadEmpresa.html')

@app.route('/cadVaga')
def cadVaga():
    empresas = models.Empresa.query.all()
    return render_template('cadVaga.html', empresas=empresas)

@app.route('/editarAluno/<idAluno>/')    #Abrir Formulário de cadastro de aluno
def editarAluno(idAluno):
    aluno = models.Aluno.query.filter_by(id=idAluno).first()
    return render_template('editarAluno.html', aluno=aluno)

@app.route('/updateAluno/<idAluno>', methods=['POST']) #salvar um aluno no banco
def updateAluno(idAluno):

    aluno = models.Aluno.query.filter_by(id=idAluno).first()
    cpfAluno = "{}{}{}{}".format(request.form['cpf'][0:3], request.form['cpf'][4:7], request.form['cpf'][8:11], request.form['cpf'][12:14] )    
    aluno.cpf          = cpfAluno
    aluno.matricula    = request.form['matricula'].upper()
    aluno.nome         = request.form['nome'].upper()
    aluno.telefone     = request.form['telefone']
    aluno.email        = request.form['email']    
    aluno.tipo         = 2
    aluno.endereco     = request.form['endereco']
    aluno.num          = request.form['num']
    aluno.complemento  = request.form['complemento']
    aluno.bairro       = request.form['bairro']
    aluno.cidade       = request.form['cidade']
    aluno.uf           = request.form['uf']
    
    models.db.session.commit()
    flash('Aluno atualizado com sucesso!')

    # url = "/editarAluno/{}".format(idAluno)
    return redirect(url_for('editarAluno', idAluno=idAluno, atualizado = True) )


@app.route('/fale_conosco')
def fale_conosco():
    return render_template('fale_conosco.html')

@app.route('/saiba_mais')
def saiba_mais():
    return render_template('saiba_mais.html')

@flask_login.login_required
@app.route('/home_visitante')
def home_visitante():
    return render_template('home_visit.html')

@flask_login.login_required
@app.route('/home_ifro')
def home_ifro():
    return render_template('home_ifro.html')


    

@app.route('/login', methods=['GET', 'POST'])         #fazer login
def login():
    if request.method == 'POST':
        email = request.form['email']

        user_email = models.Pessoa.query.filter_by(email=email).first()

        if request.form['password'] == user_email.password:
            user = User()
            user.id = email
            flask_login.login_user(user)

            if user_email.tipo == 1:  #acesso IFRO
                return redirect(url_for('home_ifro'))
            elif user_email.tipo == 2:  #acesso VISITANTE
                return redirect(url_for('home_visitante'))

        return 'Dados inválidos'

    return render_template('login.html') #vejam se é esse o nome do arquivo

@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('/home_ifro.html') #'Logged in as: ' + flask_login.current_user.id

@app.route('/')
def index():
    return render_template('home_ifro.html')  #mudar depois para    index.html

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


if __name__ == '__main__':
    app.run(debug=True)