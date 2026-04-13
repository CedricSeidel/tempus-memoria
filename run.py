from flask import Flask
from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True, port=5001)
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)
