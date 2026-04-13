from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    user = User(username="admin", password="1234", is_admin=True)
    db.session.add(user)
    db.session.commit()
    print("User erstellt!")