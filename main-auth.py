from flask import Flask, render_template, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)



login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin):
    pass

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Saptak'}
    posts = [
        {
            'author': {'username': 'Sappy'},
            'body': 'send me outside'
        }
    ]
    user = User.query.filter_by(username='Saptak').first()
    login_user(user)
    return 'You are now logged in!'


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logmein', methods=['POST'])
def logmein():
    username = request.form['username']

    user = User.query.filter_byt(username=username).first()

    if not user:
        return '<h1>User not found!<h1>'
    login_user(user)

    return '<h1>You are logged in!'




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are logged out!'

@app.route('/home')
@login_required
def home():
    return 'The current user is' + current_user.username


if __name__ == '__main__':
    app.run(debug=True)

