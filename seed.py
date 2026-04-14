from app import create_app, db
from app.models import User, Category

app = create_app()

with app.app_context():
    User.query.delete()
    Category.query.delete()
    db.session.commit()

    user = User(username="admin", is_admin=True)
    user.set_password("Admin@12345!")
    db.session.add(user)
    db.session.commit()
    print("User erstellt!")

    categories = ['E-Mails beantworten', 'Meeting', 'Pause', 'Entwicklung', 'Dokumentation']
    for name in categories:
        category = Category(name=name)
        db.session.add(category)
    db.session.commit()
    print("Kategorien erstellt!")