from app.models import User
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
import re

main = Blueprint('main', __name__)

def validate_password(password):
    if len(password) < 12:
        return "Passwort muss mindestens 12 Zeichen lang sein."
    if not re.search(r'[A-Z]', password):
        return "Passwort muss mindestens einen Großbuchstaben enthalten."
    if not re.search(r'[0-9]', password):
        return "Passwort muss mindestens eine Zahl enthalten."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Passwort muss mindestens ein Sonderzeichen enthalten."
    return None

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
        if not user.check_password(password):
            return "Falsches Passwort!"
        login_user(user)
        return redirect(url_for('main.index'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))