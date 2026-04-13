# Projektdokumentation
## Tempus Memoria — Webbasiertes Zeiterfassungssystem

---

| | |
|---|---|
| **Projektname** | Tempus Memoria |
| **Projektzeitraum** | April 2026 |
| **Technologie** | Python, Flask, SQLite, SQLAlchemy, Flask-Login |
| **Plattform** | Lokal (macOS) |
| **Entwickler** | Cedric Seidel |

---

## Inhaltsverzeichnis

1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Anforderungsanalyse](#2-anforderungsanalyse)
3. [Technologie-Stack](#3-technologie-stack)
4. [Systemarchitektur](#4-systemarchitektur)
5. [Datenbankmodell](#5-datenbankmodell)
6. [Implementierung](#6-implementierung)
7. [Aufgetretene Probleme & Lösungen](#7-aufgetretene-probleme--lösungen)
8. [Gelernte Konzepte](#8-gelernte-konzepte)
9. [Aktueller Stand & Ausblick](#9-aktueller-stand--ausblick)

---

## 1. Projektbeschreibung

Tempus Memoria ist ein lokal betriebenes Zeiterfassungssystem, das es ermöglicht, personenbezogene und themengebundene Zeiteinheiten zu erfassen, zu verwalten und auszuwerten. Das System wird als Web-Applikation mit Python und dem Flask-Framework umgesetzt.

---

## 2. Anforderungsanalyse

### Funktionale Anforderungen

| ID | Anforderung | Beschreibung | Status |
|----|-------------|--------------|--------|
| F1 | Zeiteinheiten erfassen | Start/Ende auf Kommando | ⬜ Offen |
| F2 | Benutzer-Login | Anmelden und Abmelden | ✅ Umgesetzt |
| F3 | Benutzerverwaltung | CRUD für User & Admin | 🔄 In Arbeit |
| F4 | Kategorien | CRUD + Freitext | ⬜ Offen |
| F5 | Auswertung | Chronik nach Tag/Woche/Monat/Jahr | ⬜ Offen |

### Benutzerrollen

```
┌─────────────────────────────────┐
│             Admin               │
│  • Alle Benutzerrechte          │
│  • Benutzer anlegen/löschen     │
│  • Kategorien verwalten         │
│  • Alle Zeiteinträge einsehen   │
└────────────────┬────────────────┘
                 │ erbt von
┌────────────────▼────────────────┐
│          Normaler User          │
│  • Einloggen / Ausloggen        │
│  • Eigene Zeit erfassen         │
│  • Eigene Chronik einsehen      │
└─────────────────────────────────┘
```

---

## 3. Technologie-Stack

| Schicht | Technologie | Version | Zweck |
|---------|-------------|---------|-------|
| Sprache | Python | 3.9.6 | Programmiersprache |
| Web-Framework | Flask | aktuell | Routen, HTTP, Templates |
| Datenbank | SQLite | — | Lokale Datei-Datenbank |
| ORM | Flask-SQLAlchemy | aktuell | Python ↔ Datenbank |
| Authentifizierung | Flask-Login | aktuell | Session-Verwaltung |
| Templates | Jinja2 | — | Dynamisches HTML |
| IDE | PyCharm | — | Entwicklungsumgebung |
| Betriebssystem | macOS | — | Entwicklungsplattform |

---

## 4. Systemarchitektur

### Projektstruktur

```
tempus-memoria/
│
├── run.py                  ← Einstiegspunkt, App starten
├── seed.py                 ← Testdaten in DB einfügen
├── requirements.txt        ← Installierte Pakete
├── .venv/                  ← Virtuelle Umgebung (nicht in Git)
│
└── app/
    ├── __init__.py         ← Application Factory, db & login_manager
    ├── models.py           ← Datenbankmodelle (Tabellen)
    ├── routes.py           ← URL-Routen & Logik
    │
    └── templates/
        ├── base.html       ← Grundlayout (Vererbung)
        └── login.html      ← Login-Formular
```

### Application Factory Pattern

Das Projekt verwendet das sogenannte **Application Factory Pattern**. Dabei wird die Flask-App nicht direkt beim Import erstellt, sondern in einer Funktion `create_app()`. Das ermöglicht:

- Saubere Trennung von Konfiguration und Logik
- Bessere Testbarkeit
- Mehrere App-Instanzen möglich (z.B. Test vs. Produktion)

```
run.py
  └── create_app()          ← erstellt die App
        ├── db.init_app()   ← Datenbank registrieren
        ├── models          ← Tabellen laden
        ├── Blueprint       ← Routen registrieren
        └── login_manager   ← Auth registrieren
```

### Request-Lebenszyklus

```
Browser             Flask               Datenbank
  │                   │                      │
  │── GET /login ────►│                      │
  │                   │── render login.html  │
  │◄── HTML ──────────│                      │
  │                   │                      │
  │── POST /login ───►│                      │
  │   (username,      │── User.query ───────►│
  │    password)      │◄── User-Objekt ──────│
  │                   │                      │
  │                   │── login_user()       │
  │◄── redirect / ────│                      │
  │                   │                      │
```

---

## 5. Datenbankmodell

### Entity-Relationship-Diagramm (ERD)

```
┌─────────────────┐         ┌──────────────────────┐
│      User       │         │      TimeEntry       │
├─────────────────┤         ├──────────────────────┤
│ id (PK)         │◄────────│ id (PK)              │
│ username        │  1 : n  │ user_id (FK)         │
│ password        │         │ category_id (FK)     │
│ is_admin        │         │ start_time           │
└─────────────────┘         │ end_time (nullable)  │
                            │ description          │
                            └──────────┬───────────┘
                                       │ n : 1
                                       ▼
                            ┌──────────────────────┐
                            │       Category       │
                            ├──────────────────────┤
                            │ id (PK)              │
                            │ name                 │
                            └──────────────────────┘
```

### Tabellenübersicht

**User**

| Spalte | Typ | Beschreibung |
|--------|-----|--------------|
| id | Integer (PK) | Eindeutiger Schlüssel |
| username | String(100) | Benutzername |
| password | String(200) | Passwort (später: Hash) |
| is_admin | Boolean | Admin-Rolle, Standard: False |

**Category**

| Spalte | Typ | Beschreibung |
|--------|-----|--------------|
| id | Integer (PK) | Eindeutiger Schlüssel |
| name | String(100) | Kategoriename |

**TimeEntry**

| Spalte | Typ | Beschreibung |
|--------|-----|--------------|
| id | Integer (PK) | Eindeutiger Schlüssel |
| start_time | DateTime | Startzeit |
| end_time | DateTime (nullable) | Endzeit, kann leer sein |
| description | String(300) | Freitext, nullable |
| user_id | Integer (FK) | Verweis auf User |
| category_id | Integer (FK) | Verweis auf Category |

---

## 6. Implementierung

### Phase 1 — Fundament ✅

**Ziel:** Flask-App zum Laufen bringen mit sauberer Struktur.

Umgesetzte Schritte:
- Projektordner und Dateistruktur angelegt
- Virtuelle Umgebung (`.venv`) erstellt und aktiviert
- Flask, Flask-SQLAlchemy, Flask-Login installiert
- Erste Route `/` mit Rückgabe eines Textes
- Application Factory Pattern (`create_app()`) eingeführt
- Blueprint für Routen eingerichtet

**Wichtige Dateien:**

`run.py`
```python
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

`app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempusmemoria.db'
    db.init_app(app)
    from app import models
    from app.routes import main
    app.register_blueprint(main)
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)
    return app
```

---

### Phase 2 — Datenbankmodelle ✅

**Ziel:** Tabellen in Python definieren, SQLAlchemy erstellt das SQL automatisch.

`app/models.py`
```python
from app import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    entries = db.relationship('TimeEntry', backref='user', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    entries = db.relationship('TimeEntry', backref='category', lazy=True)

class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
```

---

### Phase 3 — Authentifizierung ✅

**Ziel:** Benutzer können sich einloggen und ausloggen. Geschützte Seiten sind nur für eingeloggte User zugänglich.

`app/routes.py`
```python
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
```

### Routen-Übersicht (aktuell)

| Method | URL | Beschreibung | Geschützt |
|--------|-----|--------------|-----------|
| GET | `/` | Startseite | ✅ login_required |
| GET | `/login` | Login-Formular anzeigen | ❌ |
| POST | `/login` | Login verarbeiten | ❌ |
| GET | `/logout` | Ausloggen | ✅ login_required |

---

## 7. Aufgetretene Probleme & Lösungen

### Problem 1 — `python` nicht gefunden

**Fehler:**
```
zsh: command not found: python
```

**Ursache:** Auf macOS heißt der Befehl `python3` statt `python`.

**Lösung:** Alle Befehle mit `python3` statt `python` ausführen.

---

### Problem 2 — venv Aktivierung schlägt fehl

**Fehler:**
```
source: no such file or directory: venv/bin/activate
```

**Ursache 1:** Die venv hieß `.venv` (mit Punkt) statt `venv`.

**Lösung:** `source .venv/bin/activate`

**Ursache 2:** Nach dem Verschieben des Projektordners hatte die venv den alten Pfad gespeichert.

**Lösung:** venv löschen und neu erstellen:
```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-sqlalchemy flask-login
```

---

### Problem 3 — Doppelter Ordner durch falsches `mkdir`

**Ursache:** Der Befehl `mkdir -p tempus-memoria/app/templates` wurde ausgeführt während man bereits im Ordner `tempus-memoria` war — dadurch entstand ein doppelt verschachtelter Ordner.

**Lösung:** Projektordner manuell bereinigt.

---

### Problem 4 — `RuntimeError: The current Flask app is not registered`

**Fehler:**
```
RuntimeError: The current Flask app is not registered with this 'SQLAlchemy' instance.
```

**Ursache:** In der Flask Shell wurde versucht auf die Datenbank zuzugreifen ohne einen aktiven App-Kontext. Außerdem hatte `run.py` noch alten Code aus Phase 1 (die ursprüngliche "Hallo Welt" App) der Konflikte erzeugte.

**Lösung:**
- Alten Code aus `run.py` entfernt
- Testdaten über ein separates `seed.py` Script eingefügt statt über die Shell

---

### Problem 5 — Zwei `elif POST` Blöcke

**Fehler:** Login-Logik wurde nicht ausgeführt obwohl der Code korrekt war.

**Ursache:** Beim Erweitern der Login-Route wurden versehentlich zwei `elif request.method == 'POST'` Blöcke geschrieben. Python führt immer nur den ersten aus.

**Lösung:** Den ersten (alten) `POST`-Block entfernt.

---

### Problem 6 — `lazy='True'` statt `lazy=True`

**Fehler:** Kein direkter Fehler, aber falscher Datentyp.

**Ursache:** `'True'` ist ein String, `True` ist ein Boolean. SQLAlchemy erwartet einen Boolean.

**Lösung:** Anführungszeichen entfernt.

---

## 8. Gelernte Konzepte

### Virtuelle Umgebung (venv)

Eine isolierte Python-Umgebung pro Projekt. Verhindert Konflikte zwischen verschiedenen Projekten die unterschiedliche Paketversionen brauchen.

```
Ohne venv:           Mit venv:
─────────────        ─────────────────────────
System-Python        Projekt A (.venv) → Flask 2.0
  └── Flask 3.0      Projekt B (.venv) → Flask 3.0
      (Konflikt!)    (kein Konflikt)
```

### Python Packages

Ein Ordner mit einer `__init__.py` Datei ist ein Python-Package. Dadurch kann man Code aus diesem Ordner importieren:

```python
from app import create_app   # app/ ist ein Package
from app.routes import main  # routes.py ist ein Modul darin
```

### Decorator (`@`)

Ein Decorator verpackt eine Funktion mit zusätzlichem Verhalten. In Flask werden Decorators genutzt um Routen zu definieren und Seiten zu schützen:

```python
@main.route('/login')     # URL mit Funktion verknüpfen
@login_required           # Zugriff nur für eingeloggte User
def login():
    ...
```

### ORM (Object Relational Mapper)

SQLAlchemy übersetzt Python-Klassen in SQL-Tabellen. Kein manuelles SQL nötig:

```python
# Statt: SELECT * FROM user WHERE username = 'admin'
user = User.query.filter_by(username='admin').first()
```

### Blueprint

Blueprints teilen Routen in separate Dateien auf. Ohne Blueprint würden alle Routen in einer einzigen Datei landen — bei größeren Projekten unübersichtlich.

### Jinja2 Template-Vererbung

`base.html` definiert das Grundlayout einmal. Alle anderen Seiten erben davon und füllen nur die definierten Blöcke aus:

```
base.html          login.html
─────────────      ──────────────────────
<nav>...</nav>     {% extends 'base.html' %}
{% block           {% block content %}
  content %}   ←     <form>...</form>
{% endblock %}     {% endblock %}
```

### App-Kontext (app_context)

Flask braucht einen aktiven App-Kontext um auf die Datenbank zugreifen zu können. Außerhalb einer Route muss dieser manuell erstellt werden:

```python
with app.app_context():
    db.create_all()
```

---

## 9. Aktueller Stand & Ausblick

### Aktueller Stand

```
✅ Phase 1 — Fundament (Flask, Struktur, Blueprint)
✅ Phase 2 — Datenbankmodelle (User, Category, TimeEntry)
✅ Phase 3 — Authentifizierung (Login, Logout, login_required)
⬜ Phase 4 — Zeiterfassung (Start/Stop, Kategorien CRUD)
⬜ Phase 5 — Auswertung (Chronik, Summen)
```

### Nächste Schritte

- Passwort-Hashing mit `werkzeug.security` (Sicherheit)
- Dashboard-Seite mit echtem HTML
- Timer-Funktionalität (Start/Stop)
- Kategorien verwalten (CRUD)
- Auswertungsansicht

### Offene Sicherheitslücken (bekannt)

| Lücke | Beschreibung | Geplante Lösung |
|-------|-------------|-----------------|
| Plaintext-Passwort | Passwörter werden unverschlüsselt gespeichert | Passwort-Hashing mit werkzeug |
| Kein CSRF-Schutz | Formulare sind anfällig für Cross-Site-Request-Forgery | Flask-WTF einbinden |

---

*Dokumentation erstellt am 13.04.2026 — wird laufend aktualisiert.*