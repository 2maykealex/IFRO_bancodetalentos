
from flask import Flask, render_template, request, url_for, redirect
import flask_login

app = Flask(__name__)
app.secret_key = 'super secret string' #Change this!


login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'teste@teste.com': {'password': '123'}}

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if request.form['password'] == users[email]['password']:
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