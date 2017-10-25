from flask import Flask,render_template, request, url_for, redirect
import flask_login


app = Flask(__name__)
app.secret_key = 'super secret string' #Change this!

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'teste@teste.com': {'password': '123'}}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if request.form['password'] == users[email]['password']:
            user = User()
            user.id = email
            flask_login.login_user(user)
            return redirect(url_for('protected'))

        return 'Bad login'

    return render_template('login.html') #vejam se é esse o nome do arquivo


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/')
def index():
    return '<a href="/login"> Login</a>' #vejam se é essa a rota do seu arquivo de login.html

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


if __name__ == '__main__':
    app.run(debug=True)