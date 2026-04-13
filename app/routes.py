from app.models import User
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return 'Tempus Memoria is running!'

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None:
            return "User nicht gefunden!"

        if user.password != password:
            return "Falsches Passwort!"

        login_user(user)
        return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))