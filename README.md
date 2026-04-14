# Projektdokumentation
## Tempus Memoria — Webbasiertes Zeiterfassungssystem

---

## Deckblatt

| Feld | Inhalt |
|------|--------|
| **Projektname** | Tempus Memoria |
| **Projektart** | Innerbetriebliches Entwicklungsprojekt |
| **Ausbildungsberuf** | Fachinformatiker Anwendungsentwicklung |
| **Ausbildungsbetrieb** | Muster GmbH, Musterstraße 1, 12345 Musterstadt |
| **Auszubildender** | Max Mustermann |
| **Ausbildungsjahrgang** | 2024 – 2026 |
| **Projektstart** | 13.04.2026 |
| **Projektende** | 30.06.2026 |
| **Gesamtaufwand** | 80 Stunden |
| **Betreuer** | Erika Musterfrau |
| **Abgabedatum** | 30.06.2026 |

---

## Inhaltsverzeichnis

1. [Projektbeschreibung](#1-projektbeschreibung)
2. [Projektplanung](#2-projektplanung)
3. [Analysephase](#3-analysephase)
4. [Entwurfsphase](#4-entwurfsphase)
5. [Implementierungsphase](#5-implementierungsphase)
6. [Testphase](#6-testphase)
7. [Einführung & Abnahme](#7-einführung--abnahme)
8. [Aufgetretene Probleme & Lösungen](#8-aufgetretene-probleme--lösungen)
9. [Fazit & Reflexion](#9-fazit--reflexion)
10. [Anhang](#10-anhang)

---

## 1. Projektbeschreibung

### 1.1 Ausgangssituation

Die Muster GmbH ist ein mittelständisches Unternehmen mit 25 Mitarbeitern in der IT-Dienstleistungsbranche. Aktuell erfolgt die Erfassung von Arbeitszeiten und Tätigkeiten der Mitarbeiter ausschließlich über handschriftliche Stundenzettel sowie unstrukturierte Excel-Tabellen. Dieses Vorgehen führt regelmäßig zu folgenden Problemen:

- Stundenzettel gehen verloren oder sind unleserlich
- Keine einheitliche Kategorisierung von Tätigkeiten
- Auswertungen sind zeitaufwändig und fehleranfällig
- Kein zentraler Überblick für Vorgesetzte und Administration
- Nachträgliche Korrekturen sind schwer nachvollziehbar

Die Geschäftsführung hat daher den Bedarf geäußert, ein digitales, einfach bedienbares System zur Zeiterfassung einzuführen, das lokal im Unternehmen betrieben wird und keine Abhängigkeit von externen Cloud-Diensten erzeugt.

### 1.2 Projektziel

Ziel des Projekts ist die Entwicklung eines lokal betriebenen, webbasierten Zeiterfassungssystems mit dem Namen **Tempus Memoria** (lateinisch: „Erinnerung an die Zeit"). Das System ermöglicht Mitarbeitern, ihre Arbeitszeiten digital und gegliedert nach vordefinierten Tätigkeitskategorien zu erfassen. Administratoren können Benutzer und Kategorien verwalten sowie alle erfassten Zeiten einsehen und auswerten.

Das System ist als Web-Applikation konzipiert, die im lokalen Netzwerk des Unternehmens betrieben wird und über jeden Standard-Browser erreichbar ist.

### 1.3 Projektabgrenzung

Folgende Punkte sind ausdrücklich **nicht** Bestandteil dieses Projekts:

- Cloud-Hosting oder externer Serverbetrieb
- Mobile App (iOS / Android)
- Echtzeit-Synchronisation zwischen mehreren Geräten
- Export in externe Lohnbuchhaltungssysteme
- Automatische Urlaubsplanung oder Schichtplanung
- E-Mail-Benachrichtigungen

### 1.4 Projektumfeld

| Kriterium | Beschreibung |
|-----------|-------------|
| Auftraggeber | Muster GmbH (intern) |
| Zielgruppe | 20 Mitarbeiter, 5 Administratoren |
| Betriebsumgebung | Lokaler Server, Zugriff via Browser |
| Entwicklungsumgebung | macOS, PyCharm, Python 3.9 |
| Versionskontrolle | Git / GitHub |

---

## 2. Projektplanung

### 2.1 Projektphasen & Zeitplanung

| Nr. | Phase | Inhalt | Geplante Zeit |
|-----|-------|--------|---------------|
| 1 | Projektbeschreibung & Planung | Zieldefinition, Zeitplanung, Ressourcenplanung, Wirtschaftlichkeit | 10 Stunden |
| 2 | Analysephase | IST-Analyse, Anforderungsaufnahme, Benutzerfälle | 10 Stunden |
| 3 | Entwurfsphase | Architektur, Datenbankmodell, UML-Diagramme, UI-Entwürfe | 12 Stunden |
| 4 | Implementierung Fundament | Projektstruktur, Flask, Blueprint, Templates | 8 Stunden |
| 5 | Implementierung Datenbank | Modelle, SQLAlchemy, Migrationen | 5 Stunden |
| 6 | Implementierung Authentifizierung | Login, Logout, Rollen, Passwort-Hashing | 5 Stunden |
| 7 | Implementierung Zeiterfassung | Timer, Kategorien CRUD, Benutzer CRUD | 8 Stunden |
| 8 | Implementierung Auswertung | Chronik, Summen, Filter nach Zeitraum | 6 Stunden |
| 9 | Testphase | Manuelle Tests, Fehlerbehebung, Testprotokoll | 8 Stunden |
| 10 | Einführung & Abnahme | Deployment lokal, Übergabe, Abnahmeprotokoll | 4 Stunden |
| 11 | Dokumentation | Projektdokumentation fertigstellen | 4 Stunden |
| | **Gesamt** | | **80 Stunden** |

### 2.2 Projektphasen im Überblick (Gantt-Diagramm)

```
Phase                        KW15  KW16  KW17  KW18  KW19  KW20  KW21  KW22
─────────────────────────────────────────────────────────────────────────────
1. Planung                   ████
2. Analyse                   ████  ██
3. Entwurf                         ████  ████
4. Impl. Fundament                       ████  ██
5. Impl. Datenbank                             ██    ██
6. Impl. Auth                                  ██    ██
7. Impl. Zeiterfassung                               ████  ██
8. Impl. Auswertung                                        ████
9. Testphase                                               ██    ████
10. Einführung & Abnahme                                         ██    ██
11. Dokumentation            ░░░░  ░░░░  ░░░░  ░░░░  ░░░░  ░░░░  ░░░░  ████
─────────────────────────────────────────────────────────────────────────────
████ = aktive Bearbeitung    ░░░░ = laufende Dokumentation
```

### 2.3 Ressourcenplanung

#### Personelle Ressourcen

| Person | Rolle | Aufwand |
|--------|-------|---------|
| Max Mustermann | Entwickler, Dokumentation | 80 Stunden |
| Erika Musterfrau | Betreuer, Abnahme | 4 Stunden |
| Mitarbeiter A–C | Testnutzer | je 1 Stunde |

#### Technische Ressourcen

| Ressource | Beschreibung | Kosten |
|-----------|-------------|--------|
| MacBook Pro | Entwicklung & Test | vorhanden |
| PyCharm Community | IDE | kostenlos |
| Python 3.9 | Laufzeitumgebung | kostenlos |
| Flask & Erweiterungen | Web-Framework | kostenlos |
| SQLite | Datenbank | kostenlos |
| Git / GitHub | Versionskontrolle | kostenlos |
| Chrome / Safari | Testbrowser | vorhanden |

### 2.4 Wirtschaftlichkeitsanalyse

#### 2.4.1 Make-or-Buy Entscheidung

Vor Beginn der Eigenentwicklung wurde geprüft, ob eine bestehende Softwarelösung die Anforderungen erfüllen kann.

| Kriterium | Fremdsoftware (z.B. Clockify Pro) | Fremdsoftware (z.B. Timr) | Eigenentwicklung |
|-----------|-----------------------------------|--------------------------|-----------------|
| Monatliche Kosten | 8 € / User | 11 € / User | Einmalig |
| Datenschutz | Daten auf ext. Server | Daten auf ext. Server | Daten lokal |
| DSGVO-Konformität | Eingeschränkt | Eingeschränkt | Vollständig |
| Anpassbarkeit | Gering | Gering | Vollständig |
| Internetabhängigkeit | Ja | Ja | Nein |
| Offline-Betrieb | Nein | Nein | Ja |
| Einarbeitungsaufwand | Mittel | Mittel | Gering (eigenes System) |
| Lerneffekt Azubi | Keiner | Keiner | Hoch |

**Entscheidung: Eigenentwicklung**

Begründung:
- Datenschutzanforderungen des Unternehmens erfordern lokale Datenhaltung
- Keine laufenden Lizenzkosten
- Vollständige Anpassbarkeit an interne Prozesse
- Projekt dient gleichzeitig als Ausbildungsnachweis

#### 2.4.2 Kostenvergleich

**Fremdsoftware (Clockify Pro, 25 User):**

| Position | Berechnung | Kosten/Jahr |
|----------|------------|-------------|
| Lizenzkosten | 25 User × 8 €/Monat × 12 Monate | 2.400,00 € |
| Einrichtung & Schulung | 5h × 80 €/h (IT-Mitarbeiter) | 400,00 € |
| **Gesamt Jahr 1** | | **2.800,00 €** |
| **Folgekosten p.a.** | | **2.400,00 €** |

**Eigenentwicklung:**

| Position | Berechnung | Kosten |
|----------|------------|--------|
| Entwicklungszeit Azubi | 80h × 15 €/h | 1.200,00 € |
| Betreuungszeit | 4h × 80 €/h | 320,00 € |
| Software & Lizenzen | Open Source | 0,00 € |
| Hardware | vorhanden | 0,00 € |
| **Gesamtkosten einmalig** | | **1.520,00 €** |
| **Laufende Kosten p.a.** | Wartung ca. 5h/Jahr | **400,00 €** |

#### 2.4.3 Amortisationsrechnung

```
Einsparung gegenüber Clockify Pro im ersten Jahr:
  2.800 € (Fremdlösung) – 1.520 € (Eigenentwicklung) = 1.280 € Ersparnis

Ab Jahr 2:
  2.400 € (Fremdlösung p.a.) – 400 € (Wartung p.a.) = 2.000 € Ersparnis/Jahr

Amortisation: sofort ab Jahr 1 (Eigenentwicklung ist günstiger)
```

Die Eigenentwicklung amortisiert sich bereits im ersten Betriebsjahr und erzeugt ab Jahr 2 eine jährliche Ersparnis von ca. 2.000 €.

#### 2.4.4 Nutzwertanalyse

| Kriterium | Gewichtung | Clockify | Timr | Eigenentwicklung |
|-----------|------------|----------|------|-----------------|
| Datenschutz / DSGVO | 30% | 2 | 2 | 5 |
| Kosten | 25% | 3 | 2 | 5 |
| Anpassbarkeit | 20% | 2 | 2 | 5 |
| Offline-Betrieb | 15% | 1 | 1 | 5 |
| Einführungsaufwand | 10% | 4 | 3 | 4 |
| **Nutzwert (gewichtet)** | 100% | **2,35** | **2,00** | **4,90** |

*Bewertungsskala: 1 = sehr schlecht, 5 = sehr gut*

**Ergebnis:** Die Eigenentwicklung erzielt mit 4,90 den höchsten Nutzwert und wird daher umgesetzt.

---

## 3. Analysephase

### 3.1 IST-Analyse

#### Aktueller Prozess der Zeiterfassung

```
Mitarbeiter          Stift & Papier         Vorgesetzter
     │                      │                     │
     │── Tätigkeit ────────►│                     │
     │   aufschreiben       │                     │
     │                      │                     │
     │── Wochenzettel ───────────────────────────►│
     │   abgeben            │                     │
     │                      │         manuelle    │
     │                      │         Auswertung  │
     │                      │         in Excel    │
```

#### Schwachstellen des IST-Zustands

| ID | Schwachstelle | Auswirkung | Priorität |
|----|---------------|------------|-----------|
| S01 | Stundenzettel können verloren gehen | Datenverlust, Nacharbeit | Hoch |
| S02 | Keine Kategorisierung von Tätigkeiten | Keine Projektauswertung möglich | Hoch |
| S03 | Manuelle Excel-Auswertung | Zeitaufwand ca. 3h/Woche | Hoch |
| S04 | Unleserliche Handschrift | Fehler bei der Übertragung | Mittel |
| S05 | Keine Echtzeit-Übersicht | Vorgesetzter sieht Zeiten erst wöchentlich | Mittel |
| S06 | Kein Audit-Trail | Änderungen nicht nachvollziehbar | Niedrig |

### 3.2 SOLL-Analyse

Das neue System soll folgende Verbesserungen bringen:

| Schwachstelle | SOLL-Zustand |
|---------------|-------------|
| S01 | Digitale Speicherung, kein Datenverlust |
| S02 | Vordefinierte Kategorien + Freitext |
| S03 | Automatische Auswertung per Klick |
| S04 | Digitale Eingabe, keine Handschrift |
| S05 | Echtzeit-Übersicht für Admins |
| S06 | Unveränderliche Zeitstempel |

### 3.3 Funktionale Anforderungen

| ID | Anforderung | Beschreibung | Priorität | Quelle |
|----|-------------|--------------|-----------|--------|
| F01 | Benutzer-Login | Anmelden mit Benutzername & Passwort | Muss | Auftraggeber |
| F02 | Benutzer-Logout | Sitzung sicher beenden | Muss | Auftraggeber |
| F03 | Zeiterfassung starten | Startzeitpunkt mit einem Klick setzen | Muss | Auftraggeber |
| F04 | Zeiterfassung stoppen | Endzeitpunkt setzen, Eintrag speichern | Muss | Auftraggeber |
| F05 | Kategorie zuweisen | Zeiteintrag einer Kategorie zuordnen | Muss | Auftraggeber |
| F06 | Freitext | Optionale Beschreibung zum Zeiteintrag | Soll | Auftraggeber |
| F07 | Benutzerverwaltung | CRUD für Benutzerkonten (Admin) | Muss | Auftraggeber |
| F08 | Kategorieverwaltung | CRUD für Kategorien (Admin) | Muss | Auftraggeber |
| F09 | Chronikansicht | Eigene Zeiteinträge chronologisch einsehen | Muss | Auftraggeber |
| F10 | Summenansicht | Auswertung nach Tag / Woche / Monat / Jahr | Muss | Auftraggeber |
| F11 | Admin-Übersicht | Alle Zeiteinträge aller User einsehen | Soll | Auftraggeber |
| F12 | Passwort ändern | Eigenes Passwort ändern | Kann | Entwickler |

### 3.4 Nicht-funktionale Anforderungen

| ID | Anforderung | Beschreibung | Messbarkeit |
|----|-------------|--------------|-------------|
| NF01 | Sicherheit | Passwörter werden gehasht gespeichert (bcrypt/werkzeug) | Kein Klartext in DB |
| NF02 | Benutzerfreundlichkeit | Bedienung ohne Schulung möglich | Testnutzer kommen ohne Anleitung aus |
| NF03 | Lokalbetrieb | Keine Internetverbindung erforderlich | Funktioniert ohne Internet |
| NF04 | Verfügbarkeit | System startet zuverlässig | Kein Absturz im Testbetrieb |
| NF05 | Wartbarkeit | Saubere Code-Struktur, kommentiert | Code-Review durch Betreuer |
| NF06 | Erweiterbarkeit | Modularer Aufbau | Neue Features ohne Umbau möglich |
| NF07 | Kompatibilität | Läuft in aktuellen Browsern | Getestet in Chrome, Safari, Firefox |
| NF08 | Datenschutz | Nur eigene Daten sichtbar (außer Admin) | Kein Zugriff auf fremde Daten |

### 3.5 Benutzerrollen & Rechte

```
┌──────────────────────────────────────────────┐
│                   Admin                      │
│                                              │
│  Eigene Zeiteinträge erfassen & einsehen     │
│  Alle Zeiteinträge aller User einsehen       │
│  Benutzer anlegen / bearbeiten / löschen     │
│  Kategorien anlegen / bearbeiten / löschen   │
│  Auswertungen für alle User generieren       │
└─────────────────────┬────────────────────────┘
                      │ erbt alle Rechte von
┌─────────────────────▼────────────────────────┐
│               Normaler User                  │
│                                              │
│  Einloggen / Ausloggen                       │
│  Eigene Zeit starten / stoppen               │
│  Eigene Zeiteinträge einsehen & bearbeiten   │
│  Eigene Chronik & Auswertung einsehen        │
└──────────────────────────────────────────────┘
```

### 3.6 Use-Case-Diagramm

```
                 ┌──────────────────────────────────────────────┐
                 │              Tempus Memoria                  │
                 │                                              │
  ┌──────┐       │  (UC01) Einloggen                            │
  │      │───────┼─►(UC02) Ausloggen                            │
  │      │       │  (UC03) Zeit starten                         │
  │ User │───────┼─►(UC04) Zeit stoppen                         │
  │      │       │  (UC05) Zeiteintrag bearbeiten               │
  │      │───────┼─►(UC06) Eigene Chronik einsehen              │
  └──────┘       │  (UC07) Eigene Auswertung einsehen           │
                 │                                              │
  ┌──────┐       │  (UC08) Alle Zeiteinträge einsehen           │
  │      │───────┼─►(UC09) Benutzer verwalten (CRUD)            │
  │Admin │───────┼─►(UC10) Kategorien verwalten (CRUD)          │
  │      │       │  (UC11) Auswertung für alle User             │
  │      │       │  (+ alle User-Aktionen UC01–UC07)            │
  └──────┘       │                                              │
                 └──────────────────────────────────────────────┘
```

---

## 4. Entwurfsphase

### 4.1 Architekturentscheidung

#### Gewählte Architektur: MVC mit Flask

Das System folgt dem **MVC-Muster** (Model-View-Controller). Diese Architektur trennt Datenhaltung, Darstellung und Steuerungslogik klar voneinander und erleichtert Wartung und Erweiterung.

| Schicht | Komponente | Datei | Verantwortlichkeit |
|---------|-----------|-------|-------------------|
| Model | SQLAlchemy-Modelle | `models.py` | Datenbankstruktur & Beziehungen |
| View | Jinja2-Templates | `templates/*.html` | HTML-Darstellung |
| Controller | Flask-Routen | `routes.py` | Anfragen verarbeiten, Logik steuern |

```
┌─────────────┐   HTTP-Request    ┌──────────────────┐
│             │ ─────────────────►│   Controller     │
│   Browser   │                   │   (routes.py)    │
│  (Client)   │ ◄─────────────────│                  │
│             │   HTTP-Response   └────────┬─────────┘
└─────────────┘                            │
                                   ┌───────┴──────┐
                                   │              │
                             ┌─────▼────┐   ┌─────▼─────┐
                             │   Model  │   │   View    │
                             │ (models  │   │(templates │
                             │   .py)   │   │  /*.html) │
                             └─────┬────┘   └───────────┘
                                   │
                           ┌───────▼─────┐
                           │  Datenbank  │
                           │  (SQLite)   │
                           └─────────────┘
```

### 4.2 Technologie-Entscheidungen

| Entscheidung | Gewählt | Alternative | Begründung |
|-------------|---------|-------------|------------|
| Sprache | Python | PHP, Node.js | Ausbildungsschwerpunkt, gut lesbar |
| Framework | Flask | Django, FastAPI | Leichtgewichtig, gut für Lernzwecke |
| Datenbank | SQLite | MySQL, PostgreSQL | Keine Installation nötig, lokal als Datei |
| ORM | SQLAlchemy | Direktes SQL | Sicherer, pythonisch, keine SQL-Injection |
| Auth | Flask-Login | Eigene Implementierung | Bewährt, sicher, einfach |
| Templates | Jinja2 | React, Vue | Serverseitiges Rendering, einfacher |

### 4.3 Projektstruktur

```
tempus-memoria/
│
├── run.py                     ← Einstiegspunkt, App starten
├── seed.py                    ← Testdaten einfügen (Entwicklung)
├── requirements.txt           ← Installierte Pakete (pip freeze)
├── .gitignore                 ← Git-Ausschlüsse (.venv, *.db)
├── .venv/                     ← Virtuelle Umgebung (nicht in Git)
│
└── app/
    ├── __init__.py            ← Application Factory
    ├── models.py              ← Datenbankmodelle
    ├── routes.py              ← Routen & Controller
    │
    └── templates/
        ├── base.html          ← Grundlayout (Navigation, Footer)
        ├── login.html         ← Login-Formular
        ├── dashboard.html     ← Startseite nach Login
        ├── timer.html         ← Zeiterfassung Start/Stop
        ├── history.html       ← Chronikansicht
        ├── summary.html       ← Auswertungsansicht
        └── admin/
            ├── users.html     ← Benutzerverwaltung
            └── categories.html ← Kategorieverwaltung
```

### 4.4 Datenbankmodell (ERD)

```
┌────────────────────┐           ┌──────────────────────────────┐
│        User        │           │          TimeEntry           │
├────────────────────┤           ├──────────────────────────────┤
│ PK  id             │◄──────────│ PK  id                       │
│     username       │  1 : n    │ FK  user_id       NOT NULL   │
│     password_hash  │           │ FK  category_id   NULLABLE   │
│     is_admin       │           │     start_time    NOT NULL   │
└────────────────────┘           │     end_time      NULLABLE   │
                                 │     description   NULLABLE   │
                                 └──────────────┬───────────────┘
                                                │ n : 1
                                 ┌──────────────▼───────────────┐
                                 │           Category           │
                                 ├──────────────────────────────┤
                                 │ PK  id                       │
                                 │     name          NOT NULL   │
                                 └──────────────────────────────┘
```

#### Tabellenspezifikation

**Tabelle: user**

| Spalte | Datentyp | Constraints | Beschreibung |
|--------|----------|-------------|--------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Eindeutiger Schlüssel |
| username | VARCHAR(100) | NOT NULL, UNIQUE | Benutzername |
| password_hash | VARCHAR(200) | NOT NULL | Gehashtes Passwort |
| is_admin | BOOLEAN | NOT NULL, DEFAULT FALSE | Admin-Rolle |

**Tabelle: category**

| Spalte | Datentyp | Constraints | Beschreibung |
|--------|----------|-------------|--------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Eindeutiger Schlüssel |
| name | VARCHAR(100) | NOT NULL, UNIQUE | Kategoriename |

**Tabelle: time_entry**

| Spalte | Datentyp | Constraints | Beschreibung |
|--------|----------|-------------|--------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Eindeutiger Schlüssel |
| user_id | INTEGER | FOREIGN KEY (user.id), NOT NULL | Zugehöriger User |
| category_id | INTEGER | FOREIGN KEY (category.id), NULLABLE | Zugehörige Kategorie |
| start_time | DATETIME | NOT NULL | Startzeit |
| end_time | DATETIME | NULLABLE | Endzeit (leer = läuft noch) |
| description | VARCHAR(300) | NULLABLE | Freitext-Beschreibung |

### 4.5 UML — Klassendiagramm

```
┌─────────────────────────────────┐
│             User                │
├─────────────────────────────────┤
│ - id: Integer                   │
│ - username: String              │
│ - password_hash: String         │
│ - is_admin: Boolean             │
├─────────────────────────────────┤
│ + check_password(pw): Boolean   │
│ + get_id(): String              │
└──────────────┬──────────────────┘
               │ 1
               │
               │ n
┌──────────────▼──────────────────┐
│           TimeEntry             │
├─────────────────────────────────┤
│ - id: Integer                   │
│ - user_id: Integer (FK)         │
│ - category_id: Integer (FK)     │
│ - start_time: DateTime          │
│ - end_time: DateTime            │
│ - description: String           │
├─────────────────────────────────┤
│ + duration(): timedelta         │
│ + is_running(): Boolean         │
└──────────────┬──────────────────┘
               │ n
               │
               │ 1
┌──────────────▼──────────────────┐
│           Category              │
├─────────────────────────────────┤
│ - id: Integer                   │
│ - name: String                  │
├─────────────────────────────────┤
│ + __repr__(): String            │
└─────────────────────────────────┘
```

### 4.6 UML — Aktivitätsdiagramm: Login-Prozess

```
             [Start]
                │
                ▼
       ┌─────────────────┐
       │  Login-Seite    │
       │  aufrufen (GET) │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │  Formular       │
       │  ausfüllen &    │
       │  absenden (POST)│
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │  Benutzername   │
       │  in DB suchen   │
       └────────┬────────┘
                │
        ┌───────┴────────┐
        │                │
   [gefunden]      [nicht gefunden]
        │                │
        ▼                ▼
┌──────────────┐  ┌─────────────────┐
│  Passwort-   │  │  Fehlermeldung: │
│  hash prüfen │  │  "User nicht    │
└──────┬───────┘  │  gefunden"      │
       │          └────────┬────────┘
  ┌────┴────┐              │
  │         │              ▼
[korrekt] [falsch]   [Login-Seite]
  │         │
  ▼         ▼
login_  Fehlermeldung:
user()  "Falsches
  │     Passwort"
  ▼
Dashboard
  │
[Ende]
```

### 4.7 UML — Sequenzdiagramm: Zeiterfassung starten

```
Browser        routes.py      models.py       SQLite
   │               │               │              │
   │─GET /timer───►│               │              │
   │               │─laufenden     │              │
   │               │ Eintrag laden►│              │
   │               │               │─SELECT──────►│
   │               │               │◄─Eintrag─────│
   │◄─timer.html───│               │              │
   │               │               │              │
   │─POST /timer───►               │              │
   │  (start)      │               │              │
   │               │─TimeEntry()──►│              │
   │               │  erstellen    │              │
   │               │               │─INSERT──────►│
   │               │               │◄─OK──────────│
   │◄─redirect /───│               │              │
   │  timer        │               │              │
```

### 4.8 Routen-Planung (vollständig)

| Method | URL | Funktion | Rolle | Beschreibung |
|--------|-----|----------|-------|--------------|
| GET | `/` | `index` | User | Dashboard / Weiterleitung |
| GET/POST | `/login` | `login` | Alle | Login-Formular |
| GET | `/logout` | `logout` | User | Session beenden |
| GET/POST | `/timer` | `timer` | User | Zeit starten / stoppen |
| GET | `/history` | `history` | User | Eigene Chronik |
| GET | `/history/summary` | `summary` | User | Eigene Auswertung |
| GET | `/admin/users` | `admin_users` | Admin | Benutzerliste |
| GET/POST | `/admin/users/new` | `admin_user_new` | Admin | User anlegen |
| GET/POST | `/admin/users/<id>/edit` | `admin_user_edit` | Admin | User bearbeiten |
| POST | `/admin/users/<id>/delete` | `admin_user_delete` | Admin | User löschen |
| GET | `/admin/categories` | `admin_categories` | Admin | Kategorieliste |
| GET/POST | `/admin/categories/new` | `admin_category_new` | Admin | Kategorie anlegen |
| GET/POST | `/admin/categories/<id>/edit` | `admin_category_edit` | Admin | Kategorie bearbeiten |
| POST | `/admin/categories/<id>/delete` | `admin_category_delete` | Admin | Kategorie löschen |

### 4.9 UI-Entwurf (Wireframes)

**Login-Seite:**
```
┌──────────────────────────────────────┐
│           Tempus Memoria             │
│                                      │
│         ┌──────────────────┐         │
│  User:  │                  │         │
│         └──────────────────┘         │
│         ┌──────────────────┐         │
│  Pass:  │                  │         │
│         └──────────────────┘         │
│                                      │
│            [ Einloggen ]             │
└──────────────────────────────────────┘
```

**Dashboard (nach Login):**
```
┌──────────────────────────────────────┐
│ Tempus Memoria    [Admin] [Logout]   │
├──────────────────────────────────────┤
│ Willkommen, Max Mustermann           │
│                                      │
│  ┌──────────────┐ ┌───────────────┐  │
│  │  Timer       │ │  Chronik      │  │
│  │  starten ►   │ │  einsehen ►   │  │
│  └──────────────┘ └───────────────┘  │
│                                      │
│  Letzte Einträge:                    │
│  ─────────────────────────────────   │
│  09:00–10:30  E-Mails   1,5h         │
│  10:30–12:00  Meeting   1,5h         │
└──────────────────────────────────────┘
```

---

## 5. Implementierungsphase

### 5.1 Phase 1 — Fundament ✅

**Ziel:** Lauffähige Flask-App mit sauberer Struktur.

**Umgesetzte Schritte:**
- Projektordner und Dateistruktur angelegt
- Virtuelle Umgebung (`.venv`) erstellt und aktiviert
- Pakete installiert: Flask, Flask-SQLAlchemy, Flask-Login
- Erste Route `/` mit Textausgabe implementiert
- Application Factory Pattern (`create_app()`) eingeführt
- Blueprint für Routen eingerichtet und registriert
- Jinja2 Template-Vererbung mit `base.html` eingerichtet

**`run.py`**
```python
from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
```

**`app/__init__.py`**
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

### 5.2 Phase 2 — Datenbankmodelle ✅

**Ziel:** Tabellen als Python-Klassen definieren, SQLAlchemy übersetzt automatisch in SQL.

**`app/models.py`**
```python
from app import db
from app import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password_hash = db.Column("password", db.String(200))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
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

### 5.3 Phase 3 — Authentifizierung ✅

**Ziel:** Login, Logout und Seitenschutz mit `@login_required`.

**`app/routes.py`**
```python
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
```

**Bekannte Sicherheitslücke (geplante Lösung in Phase 4):**
Passwörter werden aktuell im Klartext gespeichert. In Phase 4 wird `werkzeug.security` für Passwort-Hashing implementiert.

---

### 5.4 Phase 4 — Zeiterfassung  (geplant)
**Ziel:** Passwörter Hashen damit Passwörter nicht in Klartext dargestellt werden. 

Implementiert mit:

```python
from werkzeug.security import generate_password_hash, check_password_hash
...

password_hash = db.Column("password", db.String(200))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha256")
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        ...
```



**Weitere Geplante Inhalte:**
- Dashboard als HTML-Template
- Start/Stop Timer-Logik mit Datenbankanbindung
- Kategorien CRUD (Admin-Bereich)
- Benutzer CRUD (Admin-Bereich)

---

### 5.5 Phase 5 — Auswertung (geplant)

**Geplante Inhalte:**
- Chronikansicht pro Benutzer
- Automatische Summenberechnung nach Tag / Woche / Monat / Jahr
- Filterung nach Kategorie und Zeitraum
- Admin-Ansicht über alle Benutzer

---

## 6. Testphase

### 6.1 Teststrategie

Es werden manuelle Funktions- und Negativtests (Black-Box-Tests) durchgeführt. Jede implementierte Funktion wird anhand der Anforderungen aus Kapitel 3.3 geprüft. Fehlgeschlagene Tests werden dokumentiert, behoben und erneut getestet.

### 6.2 Testprotokoll — Phase 3: Authentifizierung

| ID | Testfall | Vorbedingung | Eingabe | Erwartetes Ergebnis | Tatsächliches Ergebnis | Status |
|----|----------|-------------|---------|---------------------|----------------------|--------|
| T01 | Login korrekt | User "admin" in DB | admin / 1234 | Weiterleitung zu `/` | Weiterleitung zu `/` | ✅ |
| T02 | Login falsches Passwort | User "admin" in DB | admin / 9999 | Fehlermeldung "Falsches Passwort" | Fehlermeldung angezeigt | ✅ |
| T03 | Login unbekannter User | — | xyz / 1234 | Fehlermeldung "User nicht gefunden" | Fehlermeldung angezeigt | ✅ |
| T04 | Zugriff `/` ohne Login | Nicht eingeloggt | GET / | Weiterleitung zu `/login` | Weiterleitung zu `/login` | ✅ |
| T05 | Logout | Eingeloggt als admin | GET /logout | Weiterleitung zu `/login` | Weiterleitung zu `/login` | ✅ |
| T06 | Logout ohne Login | Nicht eingeloggt | GET /logout | Weiterleitung zu `/login` | Weiterleitung zu `/login` | ✅ |

### 6.3 Geplante Testfälle (offene Phasen)

| ID | Testfall | Anforderung |
|----|----------|-------------|
| T07 | Timer starten | F03 |
| T08 | Timer stoppen & Eintrag speichern | F04 |
| T09 | Zeiteintrag mit Kategorie speichern | F05 |
| T10 | Chronik zeigt korrekte Einträge | F09 |
| T11 | Auswertung summiert korrekt | F10 |
| T12 | Admin kann User anlegen | F07 |
| T13 | Admin kann User löschen | F07 |
| T14 | Admin kann Kategorie anlegen | F08 |
| T15 | Normaler User hat keinen Admin-Zugriff | NF08 |
| T16 | User sieht keine fremden Einträge | NF08 |

---

## 7. Einführung & Abnahme

### 7.1 Deployment (lokal)

Das System wird auf dem Rechner des Administrators installiert und im lokalen Netzwerk betrieben. Die Einrichtung erfolgt mit folgenden Schritten:

```bash
# 1. Repository klonen
git clone https://github.com/muster/tempus-memoria.git
cd tempus-memoria

# 2. Virtuelle Umgebung erstellen
python3 -m venv .venv
source .venv/bin/activate

# 3. Pakete installieren
pip install -r requirements.txt

# 4. App starten
python3 run.py
```

Das System ist dann erreichbar unter `http://localhost:5001`.

### 7.2 Abnahmekriterien

| ID | Kriterium | Erfüllt |
|----|-----------|---------|
| A01 | Alle Testfälle T01–T06 bestanden | ✅ |
| A02 | Login und Logout funktionieren | ✅ |
| A03 | Geschützte Seiten nur nach Login erreichbar | ✅ |
| A04 | Passwörter werden nicht im Klartext gespeichert | ⬜ (Phase 4) |
| A05 | Zeiterfassung Start/Stop funktioniert | ⬜ (Phase 4) |
| A06 | Auswertung nach Zeitraum funktioniert | ⬜ (Phase 5) |

---

## 8. Aufgetretene Probleme & Lösungen

### Problem 1 — `python` nicht gefunden

| | |
|---|---|
| **Fehlermeldung** | `zsh: command not found: python` |
| **Ursache** | Auf macOS heißt der Befehl `python3` statt `python` |
| **Lösung** | Alle Befehle mit `python3` ausführen |
| **Lerneffekt** | macOS-spezifische Python-Benennung beachten |

---

### Problem 2 — venv Aktivierung schlägt fehl

| | |
|---|---|
| **Fehlermeldung** | `source: no such file or directory: venv/bin/activate` |
| **Ursache 1** | Die venv heißt `.venv` (versteckter Ordner mit Punkt am Anfang) |
| **Lösung 1** | `source .venv/bin/activate` verwenden |
| **Ursache 2** | Projektordner wurde verschoben — venv enthält absoluten Pfad |
| **Lösung 2** | venv löschen und neu erstellen |
| **Lerneffekt** | venv speichert absolute Pfade und muss nach Verschieben neu erstellt werden |

---

### Problem 3 — Doppelt verschachtelter Projektordner

| | |
|---|---|
| **Ursache** | `mkdir -p tempus-memoria/app/templates` wurde ausgeführt während man bereits im `tempus-memoria`-Ordner war |
| **Lösung** | Projektordner manuell bereinigt |
| **Lerneffekt** | Vor `mkdir` immer mit `pwd` prüfen wo man sich gerade befindet |

---

### Problem 4 — RuntimeError: Flask App nicht registriert

| | |
|---|---|
| **Fehlermeldung** | `RuntimeError: The current Flask app is not registered with this SQLAlchemy instance` |
| **Ursache** | `run.py` enthielt noch alten „Hallo Welt"-Code aus Phase 1, der eine zweite Flask-App ohne `db.init_app()` erstellte und Konflikte verursachte |
| **Lösung** | Alten Code aus `run.py` entfernt; Testdaten über separates `seed.py` Script eingefügt |
| **Lerneffekt** | Jede SQLAlchemy-Instanz muss explizit mit `db.init_app(app)` mit einer Flask-App verknüpft werden |

---

### Problem 5 — Zwei `elif POST` Blöcke

| | |
|---|---|
| **Symptom** | Neue Login-Logik wurde nicht ausgeführt obwohl Code korrekt war |
| **Ursache** | Beim Erweitern der Route wurden versehentlich zwei `elif request.method == 'POST'` Blöcke geschrieben. Python führt immer nur den ersten zutreffenden Block aus. |
| **Lösung** | Ersten (alten) `POST`-Block entfernt |
| **Lerneffekt** | Bei `if/elif`-Ketten wird immer nur der erste zutreffende Block ausgeführt — doppelte Bedingungen werden ignoriert |

---

## 9. Fazit & Reflexion

### 9.1 Soll-Ist-Vergleich Zeitplanung

| Phase | Geplant | Tatsächlich | Abweichung | Begründung |
|-------|---------|-------------|------------|------------|
| Planung & Analyse | 20h | 20h | ±0h | Plangemäß |
| Entwurf | 12h | 12h | ±0h | Plangemäß |
| Impl. Fundament | 8h | 8h | ±0h | Plangemäß |
| Impl. Datenbank | 5h | 5h | ±0h | Plangemäß |
| Impl. Auth | 5h | 6h | +1h | Debugging App-Kontext |
| Impl. Zeiterfassung | 8h | 0h | offen | Noch nicht begonnen |
| Impl. Auswertung | 6h | 0h | offen | Noch nicht begonnen |
| Test | 8h | 2h | offen | Nur Phase 3 getestet |
| Einführung | 4h | 0h | offen | Noch nicht begonnen |
| Dokumentation | 4h | 4h | ±0h | Laufend gepflegt |
| **Gesamt** | **80h** | **57h** | **-23h** | **Phasen 4–5 offen** |

### 9.2 Was lief gut

- Die gewählte Technologie (Flask + SQLAlchemy) hat sich als geeignet und gut lernbar erwiesen
- Die Projektstruktur mit Application Factory Pattern ist sauber und erweiterbar
- Fehler wurden systematisch analysiert, verstanden und gelöst
- Die laufende Dokumentation ermöglicht gute Nachvollziehbarkeit

### 9.3 Was lief weniger gut

- Probleme mit der virtuellen Umgebung nach Ordnerverschiebung kosteten ungeplante Zeit
- Der Flask App-Kontext in der Shell bereitete Schwierigkeiten
- Python-Grundlagen (Syntax, Datentypen, Scoping) mussten parallel erarbeitet werden
- Alter Code wurde nicht vollständig entfernt, was zu Konflikten führte

### 9.4 Lessons Learned

| Erkenntnis | Maßnahme |
|------------|----------|
| Vor Terminal-Befehlen immer `pwd` ausführen | Zur Routine machen |
| venv nie verschieben | Immer neu erstellen nach Verschiebung |
| Code nach Änderungen vollständig lesen | Review-Schritt einbauen |
| Alten Code sofort löschen | Kein auskommentierter Code im Projekt |

### 9.5 Ausblick

| Priorität | Nächster Schritt | Aufwand |
|-----------|-----------------|---------|
| Hoch | Passwort-Hashing implementieren | 1h |
| Hoch | Dashboard HTML-Template | 2h |
| Hoch | Timer Start/Stop Logik | 4h |
| Mittel | Admin CRUD Benutzer | 3h |
| Mittel | Admin CRUD Kategorien | 2h |
| Mittel | Chronik & Auswertung | 6h |

---

## 10. Anhang

### 10.1 Installierte Pakete (requirements.txt)

```
flask
flask-sqlalchemy
flask-login
werkzeug
```

### 10.2 Glossar

| Begriff | Erklärung |
|---------|-----------|
| ORM | Object Relational Mapper — übersetzt Python-Klassen in SQL-Tabellen |
| Blueprint | Flask-Modul zur Aufteilung von Routen in separate Dateien |
| Application Factory | Entwurfsmuster — App wird in einer Funktion erstellt statt global |
| venv | Virtuelle Umgebung — isolierter Python-Kontext pro Projekt |
| CRUD | Create, Read, Update, Delete — die vier Grundoperationen auf Daten |
| MVC | Model-View-Controller — Architekturmuster zur Trennung von Logik und Darstellung |
| Session | Serverseitige Speicherung des Login-Zustands eines Benutzers |
| Decorator | Python-Syntax (`@`) um Funktionen mit zusätzlichem Verhalten zu versehen |
| Primary Key (PK) | Eindeutiger Identifikator eines Datenbankeintrags |
| Foreign Key (FK) | Verweis auf den Primary Key einer anderen Tabelle |
| Hash | Einweg-Verschlüsselung — Passwort kann nicht zurückgerechnet werden |
| DSGVO | Datenschutz-Grundverordnung — EU-Verordnung zum Schutz personenbezogener Daten |
| Black-Box-Test | Test ohne Kenntnis des internen Codes — nur Ein- und Ausgabe wird geprüft |
| Amortisation | Zeitraum bis sich eine Investition durch Einsparungen bezahlt macht |
| SaaS | Software as a Service — Softwarenutzung als Mietmodell über das Internet |

### 10.3 Offene Sicherheitslücken

| ID | Lücke | Risiko | Geplante Lösung | Phase |
|----|-------|--------|-----------------|-------|
| S01 | Plaintext-Passwörter | Hoch | `werkzeug.security` Hashing | Phase 4 |
| S02 | Kein CSRF-Schutz | Mittel | Flask-WTF einbinden | Phase 4 |
| S03 | SECRET_KEY im Quellcode | Mittel | Umgebungsvariable (`.env`) | Phase 4 |
| S04 | debug=True in Produktion | Niedrig | Vor Deployment deaktivieren | Phase 7 |

### 10.4 Verwendete Quellen

| Quelle | URL | Genutzt für |
|--------|-----|-------------|
| Flask Dokumentation | https://flask.palletsprojects.com | Flask, Blueprints, Routing |
| SQLAlchemy Dokumentation | https://docs.sqlalchemy.org | Datenbankmodelle, Abfragen |
| Flask-Login Dokumentation | https://flask-login.readthedocs.io | Authentifizierung, Session |
| Python Dokumentation | https://docs.python.org | Python-Syntax, Grundlagen |

---

*Dokumentation erstellt am 13.04.2026 — wird laufend aktualisiert.*
*Alle Firmen- und Personenangaben sind fiktiv und dienen ausschließlich als Demonstration.*
