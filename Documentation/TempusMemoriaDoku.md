# Tempus Memoria — Projektdokumentation
## Zeiterfassungssystem mit Python & Flask

---

## Inhaltsverzeichnis

1. [Projektübersicht](#1-projektübersicht)
2. [Technologie-Stack](#2-technologie-stack)
3. [Projektstruktur](#3-projektstruktur)
4. [Datenbankmodell (ERD)](#4-datenbankmodell-erd)
5. [Phasenplan](#5-phasenplan)
6. [Routen-Übersicht](#6-routen-übersicht)
7. [Benutzerrollen](#7-benutzerrollen)
8. [Wichtige Konzepte](#8-wichtige-konzepte)
9. [Fortschritt](#9-fortschritt)

---

## 1. Projektübersicht

**Tempus Memoria** ist ein lokales Zeiterfassungssystem, das es ermöglicht, personenbezogene und themengebundene Zeiteinheiten zu erfassen.

### Anforderungen (aus dem Projekt-Briefing)

| # | Anforderung | Beschreibung |
|---|-------------|--------------|
| 1 | Zeiteinheiten loggen | Start/Ende auf Kommando |
| 2 | Login-System | Benutzer können sich anmelden |
| 3 | Benutzerverwaltung | CRUD für User & Admin |
| 4 | Kategorien | CRUD für vorgefertigte Kategorien + Freitext |
| 5 | Auswertung | Chronik & Summen nach Tag / Woche / Monat / Jahr |

---

## 2. Technologie-Stack

| Schicht | Technologie | Zweck |
|---------|-------------|-------|
| Sprache | Python 3 | Programmiersprache |
| Web-Framework | Flask | Routen, HTTP, Templates |
| Datenbank | SQLite | Lokale Datei-Datenbank |
| ORM | SQLAlchemy | Python ↔ Datenbank |
| Auth | Flask-Login | Login / Session-Verwaltung |
| Templates | Jinja2 | HTML dynamisch rendern |
| Frontend | HTML + CSS | Benutzeroberfläche |

---

## 3. Projektstruktur

```
tempus-memoria/
│
├── run.py                  ← App starten
├── requirements.txt        ← Pakete (pip)
├── .venv/                  ← Virtuelle Umgebung (nicht in Git)
│
└── app/
    ├── __init__.py         ← App-Factory, db initialisieren
    ├── models.py           ← Datenbankmodelle (Tabellen)
    ├── routes.py           ← URL-Routen & Logik
    │
    └── templates/          ← HTML-Dateien
        ├── base.html       ← Grundlayout (wird vererbt)
        ├── login.html
        ├── dashboard.html
        ├── timer.html
        └── history.html
```

---

## 4. Datenbankmodell (ERD)

```
┌─────────────────┐         ┌──────────────────┐
│      User       │         │    TimeEntry     │
├─────────────────┤         ├──────────────────┤
│ id (PK)         │◄────────│ id (PK)          │
│ username        │  1   n  │ user_id (FK)     │
│ password_hash   │         │ category_id (FK) │
│ is_admin        │         │ start_time       │
└─────────────────┘         │ end_time         │
                            │ description      │
                            └──────────────────┘
                                     │ n
                                     │
                                     ▼ 1
                            ┌──────────────────┐
                            │    Category      │
                            ├──────────────────┤
                            │ id (PK)          │
                            │ name             │
                            │ color            │
                            └──────────────────┘
```

### Beziehungen

| Von | Zu | Typ | Bedeutung |
|-----|----|-----|-----------|
| User | TimeEntry | 1 : n | Ein User hat viele Zeiteinträge |
| Category | TimeEntry | 1 : n | Eine Kategorie hat viele Zeiteinträge |

---

## 5. Phasenplan

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5
Fundament   Datenbank   Auth        Zeiterfassung  Auswertung
   ✅           🔄          ⬜           ⬜              ⬜
```

### Phase 1 — Fundament ✅

- [x] Projektordner anlegen
- [x] Virtuelle Umgebung (venv) einrichten
- [x] Flask, SQLAlchemy, Flask-Login installieren
- [x] `run.py` mit erster Route
- [x] Application Factory Pattern (`create_app`)
- [x] Blueprint einrichten

### Phase 2 — Datenbank 🔄 *(aktuell)*

- [ ] Modelle definieren: `User`, `Category`, `TimeEntry`
- [ ] Datenbank initialisieren (`db.create_all()`)
- [ ] Erste Testdaten einfügen

### Phase 3 — Authentifizierung ⬜

- [ ] Passwort-Hashing (werkzeug)
- [ ] Login-Formular (HTML)
- [ ] Flask-Login einrichten
- [ ] `@login_required` Decorator
- [ ] Admin-Rolle absichern

### Phase 4 — Zeiterfassung ⬜

- [ ] Start/Stop-Logik (Timer)
- [ ] Kategorie CRUD (erstellen, anzeigen, bearbeiten, löschen)
- [ ] Benutzer CRUD (Admin-Bereich)
- [ ] Freitext-Einträge

### Phase 5 — Auswertung ⬜

- [ ] Chronik-Ansicht pro Person
- [ ] Summen nach Tag / Woche / Monat / Jahr
- [ ] Filterung nach Kategorie

---

## 6. Routen-Übersicht

*(wird schrittweise befüllt)*

| Method | URL | Beschreibung | Auth |
|--------|-----|--------------|------|
| GET | `/` | Startseite / Dashboard | ✅ Login |
| GET/POST | `/login` | Login-Formular | ❌ |
| GET | `/logout` | Abmelden | ✅ Login |
| GET | `/timer` | Zeiterfassung starten/stoppen | ✅ Login |
| GET | `/history` | Chronik anzeigen | ✅ Login |
| GET | `/admin/users` | Benutzerverwaltung | ✅ Admin |
| GET/POST | `/admin/categories` | Kategorien verwalten | ✅ Admin |

---

## 7. Benutzerrollen

```
                    ┌─────────────────────────┐
                    │         Admin           │
                    │  • Alle User-Rechte     │
                    │  • User anlegen/löschen │
                    │  • Kategorien verwalten │
                    │  • Alle Zeiten einsehen │
                    └───────────┬─────────────┘
                                │ erbt von
                    ┌───────────▼─────────────┐
                    │       Normaler User     │
                    │  • Einloggen            │
                    │  • Eigene Zeit erfassen │
                    │  • Eigene Chronik sehen │
                    └─────────────────────────┘
```

---

## 8. Wichtige Konzepte

### Was ist eine virtuelle Umgebung?

Eine isolierte Python-Umgebung pro Projekt. Pakete werden nur lokal installiert und stören keine anderen Projekte.

```bash
python3 -m venv .venv        # einmal erstellen
source .venv/bin/activate    # jedes Mal aktivieren (Mac/Linux)
```

### Was ist ein Blueprint?

Ein Blueprint ist ein Baustein in Flask um Routen aufzuteilen. Statt alle Routen in eine Datei zu packen, können sie in Module aufgeteilt werden.

```python
# routes.py
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hallo!'
```

### Was ist ein ORM?

ORM = Object Relational Mapper. SQLAlchemy übersetzt Python-Klassen in Datenbanktabellen. Du schreibst kein SQL, sondern Python.

```python
# Statt SQL: SELECT * FROM user WHERE id = 1
user = User.query.get(1)
```

### Was ist Application Factory?

`create_app()` ist eine Funktion die die Flask-App erstellt. Das ermöglicht mehrere Instanzen (z.B. Test vs. Produktion).

---

## 9. Fortschritt

| Datum | Was gemacht |
|-------|-------------|
| 13.04.2026 | Projektstruktur, venv, Flask, Blueprint, Application Factory |

---

*Dieses Dokument wird laufend aktualisiert.*