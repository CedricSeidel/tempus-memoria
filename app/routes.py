from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Tempus Memoria is running!'