from app.models import User
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
import re
from datetime import datetime
from flask_login import current_user
from app.models import User, TimeEntry
from app import db
from sqlalchemy import true
from app.models import User, TimeEntry, Category

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
def home():
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def index():
    return render_template('dashboard.html')

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

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/timer', methods=['GET', 'POST'])
@login_required
def timer():
    if request.method == 'GET':
        running = TimeEntry.query.filter_by(user_id=current_user.id, end_time=None).first()
        categories = Category.query.all()
        return render_template('timer.html', running=running, categories=categories)

    elif request.method == 'POST':
        action = request.form['action']

        if action == 'start':
            category_id = request.form.get('category_id') or None
            entry = TimeEntry(
                user_id=current_user.id,
                start_time=datetime.now(),
                end_time=None,
                category_id=category_id
            )
            db.session.add(entry)
            db.session.commit()

        elif action == 'stop':
            entry = TimeEntry.query.filter_by(
                user_id=current_user.id,
                end_time=None
            ).first()
            if entry:
                entry.end_time = datetime.now()
                db.session.commit()

        return redirect(url_for('main.timer'))