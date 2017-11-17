import os
from flask import Flask, render_template, request, url_for, redirect, flash
import flask_login
from flask_sqlalchemy import SQLAlchemy
import models
import config

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
        return render_template('login.html')

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


@app.route('/fale_conosco')
def fale_conosco():
    return render_template('fale_conosco.html')

@app.route('/saiba_mais')
def saiba_mais():
    return render_template('saiba_mais.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        user_email = models.Pessoa.query.filter_by(email=email).first()

        if request.form['password'] == user_email.password:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return redirect(url_for('protected'))

        return 'Dados inválidos'

    return render_template('login.html') #vejam se é esse o nome do arquivo


@app.route('/protected')
@flask_login.login_required
def protected():
    return render_template('home.html') #'Logged in as: ' + flask_login.current_user.id

@app.route('/')
@app.route('/login')
def index():
    return render_template('index.html')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


if __name__ == '__main__':
    app.run(debug=True)