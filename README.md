# Italia Money Radar

Italia Money Radar ist ein deutschsprachiges Online-Projekt für Menschen, die einen Neustart in Italien realistisch prüfen wollen.

## Aktueller Stand

Version 0.1 — Fundament

## Enthälten:

- Startseite
- Italien-Kostenrechner
- Impressum-Grundgerüst
- Datenschutz-Grundgerüst
- rechtliche Hinweise
- keine Cookies
- kein Tracking
- keine Nutzerkonten
- keine Zahlungsfunktion

## Projektziel

Tools, Rechner und Orientierung zu:

- Italien-Kosten
- Napoli-Neustart
- Online-Einkommen
- Partita IVA
- Resto al Sud
- Italienische Standortvorteile

## Wichtiger Hinweis
Dieses Projekt bietet allgemeine Informationen und Orientierung. Keine Steuerberatung, Rechtsberatung, Finanzberatung, Immobilienvermittlung oder Fördergarantie.

## Seitenstruktur (Schritt 1.7)

- `index.html` — Startseite mit Überblick und Verlinkung auf alle Tools
- `italien-kostenrechner.html` — interaktiver Kostenrechner mit echten Standort-Faktoren
- `napoli-neustart.html` — strategische Orientierung für einen Neustart in Napoli/Süditalien
- `online-geld-in-italien.html` — Online-Einkommen als Hebel, Modelle und Reihenfolge
- `partita-iva.html` — Grundcheck Partita IVA, regime forfettario, Reihenfolge
- `resto-al-sud-check.html` — Fördercheck Resto al Sud, Invitalia, Förderlogik
- `impressum.html`, `datenschutz.html`, `404.html` — Rechtliches & Fehlerseite
- `sitemap.xml` — alle URLs für Suchmaschinen


## Datenquellen (Standort-Faktoren)
Die Stadt-Faktoren im Kostenrechner (`js/app.js` → `CITY_DATA`) stützen sich auf:

- **Nomisma – Osservatorio Immobiliare 2024**: Quadratmeterpreise Kaltmiete pro Stadt
- **Numbeo Cost of Living Index 2024/2025** (März 2025, Bezug Land = 100)
- **ISTAT – Indici prezzi al consumo (FOI) 2024**
- **ARERA** – konsolidierte Endkundenpreise Strom & Gas, 4. Quartal 2024
- **ÖPNV-Monatstickets 2024** (ATM Milano, ATAC Roma, ANM Napoli, GTT Torino, TPER Bologna)
- **OAM / MIMIT Spritpreisstatistik 2024** (Pendler-Faktor)

Methodik: gewichteter Mittelwert (Miete 40 %, Lebensmittel 20 %, Freizeit 20 %, Transport 10 %, Energie 10 %), Referenz Neapel = 1,00.
Die Faktoren sind eine Orientierungshilfe, keine exakte Prognose. Innerhalb einer Stadt können Mieten je nach Stadtteil um Faktor 1,3–1,8 schwanken.

## Run lokal

- Mit Python 3 (einfach und plattformübergreifend):

```
cd "c:\Users\Jaenu\OneDrive\Dokumente\ItalienRadar"
python -m http.server 8000

# Dann im Browser öffnen: http://localhost:8000
```

- Alternativ: VS Code Erweiterung `Live Server` zum schnellen Testen.

## Hinweise / offene Punkte

- Doppelter JS-Code: Es gibt `js/app.js` (aktives Skript für den Kostenrechner) und eine zusätzliche Kopie unter `website/js/app.js`. Prüfen, ob `website/js/app.js` absichtlich für einen separaten Build benötigt wird, ansonsten zusammenführen oder löschen.
- `italien-kostenrechner.html` enthält ein Byte-Order-Mark (BOM) am Dateianfang; das ist meist unproblematisch, kann aber beim Parsen mancher Tools auffallen.

