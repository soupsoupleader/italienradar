# Phase 3.2.2.2.1 – P2-Systemarchitektur für Mastertemplate und PDF-Produktion

Stand: 15.07.2026
Phase: `3.2.2.2.1`
Baseline: `c3797739c6f5178e7abf8d9b00ed1694e70a2780` (`docs(downloads): clarify pipeline completion record`)
Ausgewählte Pipeline: `P2_HTML_PRINT`

## Zweck und Grenzen

Diese Architektur definiert die versionierte Produktionsgrundlage für die statischen Produkte `C01` bis `C07`. Sie trennt Produktdaten, Template, Tokens, Komponenten, Build, PDF-Prüfung und spätere Veröffentlichungsartefakte. Sie ist ein Architekturvertrag, noch kein fertiges Mastertemplate.

In dieser Teilphase werden keine Produktinhalte, Komponenten, Design-Tokens, PDFs oder Websiteänderungen erzeugt. `C08` bleibt eine dynamische Ergebnisprotokoll-Familie und ist für diese statische Architektur nicht freigegeben. Formulare, AcroForm-Felder, E-Mail-Erfassung und individuelle Beratung bleiben außerhalb des Systems.

## Ausgangslage und normative Baseline

Die normativen Eingaben aus Phase 3.2.1.3 legen für `C01` bis `C07` die Produktaufgaben, die zehnteilige Dokumentanatomie, die Primärklassen `B`, `C` und `E`, die Module `M01` bis `M12`, DIN A4 Hochformat, lokale Schriften und Assets, PDF-Sicherheitsregeln, Accessibility-Prüfungen und die Gates `G1` bis `G4` fest. Die Pipelineentscheidung aus Phase 3.2.2.1 wählt `P2_HTML_PRINT`; P1 Word bleibt lokal `ENVIRONMENT_BLOCKED` und wird nicht global verworfen.

Die Abschlusskorrektur von Phase 3.2.2.1 wurde in `c379773` committed und gepusht. Dieser Commit ist die Baseline für diese Architektur. Die bestehende Nutzeränderung an `datenschutz.html` gehört nicht zum PDF-System.

## Repository-Inventur

| Bereich | Befund | Architekturentscheidung |
|---|---|---|
| Website | HTML-Dateien im Repository-Root, `css/style.css`, `js/app.js` | bleibt Live-Website und wird nicht als PDF-Quelle importiert |
| Worker/Deployment | `wrangler.toml`, `_headers`, `robots.txt`, `sitemap.xml` | bleibt Website-/Deploymentbereich und ist vom PDF-Build getrennt |
| Dokumentation | `docs/download-system/` mit Standards und Pipelineentscheidungen | bleibt normative Dokumentations- und Entscheidungsablage |
| Skripte | vorhandenes `scripts/audit-html-attributes.ps1` | bleibt Website-Audit; keine automatische PDF-Abhängigkeit |
| Buildmanifest | keine `package.json`, Lockdatei oder sonstige zentrale Buildmanifestdatei vorhanden | PDF-System erhält ein eigenes maschinenlesbares Buildmanifest in `download-system/manifests/` |
| Assets | keine bestehende PDF-Assetbibliothek; Website-CSS ist vorhanden | PDF-Schriften, Logos und Bilder werden später lokal unter `download-system/assets/` verwaltet |
| Downloads/PDFs | keine versionierte Produktions-PDF-Struktur vorhanden; Prototypen bleiben temporär | `public-downloads/` wird erst nach Release-Gate als Artefaktziel verwendet |
| Temporär | `.tmp/` und `.venv-pdfqa/` sind lokal vorhanden; `.git/info/exclude` enthält bereits P2-Prototyp-Ausschlüsse | neue Build- und QA-Artefakte bleiben unter einem phasenspezifischen temporären Pfad |
| Kollisionen | Root-HTML, `css/`, `js/`, Workerdateien und Website-Audits haben eigene Zuständigkeit | `download-system/` ist die einzige PDF-Systemwurzel; keine gleichnamigen Websitepfade verwenden |

Nicht für das PDF-System verwendet werden dürfen: `datenschutz.html`, sämtliche bestehenden Root-HTML-Dateien, `css/`, `js/`, `wrangler.toml`, `_headers`, `robots.txt`, `sitemap.xml`, Website-Auditdateien und Deploymentkonfiguration. Eine kontrollierte Übernahme einzelner Markenwerte ist nur über lokal kopierte, dokumentierte Tokens zulässig.

## Architekturdiagramm

```text
versionierte Produktdaten + Quellen
              │
              ├── Produktprofil C01–C07
              ├── Mastertemplate
              ├── Design-Tokens
              ├── M01–M12-Komponentenvertrag
              └── lokale Schriften und Assets
                              │
                              ▼
                   offline P2 Buildvertrag
                              │
                              ▼
             HTML-Ausgabe + isoliertes Print-CSS
                              │
                              ▼
              lokal ermitteltes Chrome/Chromium
                              │
                              ▼
                 PDF-Metadaten/Postprocessing
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        technische PDF-QA               200-dpi-Render
                │                           │
                └─────────────┬─────────────┘
                              ▼
                  Buildbericht und Manifest
                              │
                   Release-Gate G3/G4
                              │
                              ▼
                  spätere public-downloads/
```

## Verbindlicher Verzeichnisplan

| Pfad | Versionierung | Quelle oder Artefakt | Sichtbarkeit | Lebensdauer | Zuständige Phase | Zulässige Dateitypen |
|---|---|---|---|---|---|---|
| `download-system/content/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.4+ | `.json`, später redaktionelle Quellformate |
| `download-system/profiles/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.4+ | `.json` |
| `download-system/templates/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.4+ | `.html`, `.css` |
| `download-system/tokens/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.2+ | `.json`, `.css` |
| `download-system/components/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.3+ | `.html`, `.css` |
| `download-system/assets/fonts/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.2+ | `.woff2`, `.woff`, `.ttf`, Lizenzdateien |
| `download-system/assets/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.2+ | `.svg`, `.png`, `.jpg`, `.json`, Lizenzdateien |
| `download-system/scripts/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.4+ | `.ps1`, `.js`, `.py` oder äquivalente dokumentierte Skripte |
| `download-system/manifests/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.4+ | `.json` |
| `download-system/qa/` | versioniert | Quelle | intern | dauerhaft | 3.2.2.2.5+ | `.json`, `.md` |
| `.tmp/phase-3-2-2-2-1/` | nicht versioniert | generiertes Artefakt | intern | temporär | 3.2.2.2.4+ | generierte Build-/QA-Dateien |
| `public-downloads/` | generiert; Freigabeentscheidung erforderlich | generiertes Artefakt | öffentlich nach Freigabe | releasebezogen | 3.2.2.2.6+ | versionierte `.pdf` nach Dateinamenregel |
| Root-Website, `css/`, `js/` | bestehend, getrennt | bestehender Websitebereich | öffentlich | dauerhaft | außerhalb dieser Architektur | bestehende Website-Dateien |

Der phasenspezifische temporäre Pfad muss vor der ersten Implementierung zusätzlich in einer passenden lokalen Exclude-Regel abgesichert werden. Temporäre Dateien dürfen niemals unter Website- oder Workerpfaden entstehen. PDFs und Renderbilder werden vorerst nicht committed.

## Verantwortungsgrenzen

Produktdaten liefern Inhalte, Quellen, Statuswerte und Eingabedefinitionen. Produktprofile wählen nur aus den normativ erlaubten Klassen, Risiko- und Aktualitätswerten. Das Mastertemplate definiert die gemeinsame Dokumentanatomie; Komponenten liefern semantische Bausteine; Print-CSS definiert das A4-Seitensystem. Kein PDF-Modul liest Website-CSS automatisch.

Der Build rendert offline aus versionierten Quellen und lokalen Assets. Das Postprocessing setzt nur kontrollierte technische Metadaten und darf keine privaten Pfade, Benutzernamen oder Telemetrie eintragen. QA prüft Quelle, HTML/CSS, PDF-Struktur, Sicherheit, Accessibility, Rendering und funktionale Reproduzierbarkeit. Erst das Release-Gate darf ein PDF in `public-downloads/` kopieren.

## Build- und Renderervertrag

Chrome/Chromium ist der ausgewählte Renderer. Das Buildskript muss den lokalen ausführbaren Pfad eindeutig über eine definierte Auflösungskette ermitteln, die tatsächliche Browserversion mit `--version` erfassen und Pfad sowie Version in Buildmanifest und Report schreiben. Ein hart codierter Benutzerpfad ist unzulässig.

Der Build läuft mit deaktiviertem Netzwerk oder einer gleichwertigen Offline-Sperre. HTML, CSS, Schriften, Icons, Logos und Bilder werden ausschließlich aus lokalen, versionierten Quellen gelesen. Nicht erreichbares Netzwerk darf weder Inhalt noch Layout noch Metadaten verändern. Locale, Zeitzone, Datumsformat, Sortierung von Daten und Quellen sowie Build-ID-Regel werden festgelegt und im Manifest dokumentiert.

Die funktionale Reproduzierbarkeit verlangt gleiche Seitenzahl, Seitengeometrie, extrahierbaren Text, Überschriftenreihenfolge, Tabelleninhalte, Links, Renderabmessungen und Sicherheitsmerkmale. Feste Locale ist `de-DE`, die Zeitzone ist `UTC`, und Daten sowie Quellen werden nach expliziter stabiler Reihenfolge sortiert. Zeitstempelunterschiede werden entweder normalisiert oder als nicht-fachliche Metadatenabweichung im Report ausgewiesen. Zufällige IDs und benutzerabhängige Pfade sind verboten.

## PDF-Metadaten und Sicherheitsgrenzen

Mindestens gesetzt werden Titel, Sprache `de-DE`, Produkt-ID, Dokumentversion, Aktualitätsklasse, Risikoklasse, Quellversion und Buildversion. Autor darf nur ein neutrales Systemlabel sein; persönliche Editorennamen, E-Mail-Adressen, lokale Pfade, Windows-Benutzernamen, temporäre Verzeichnisse, Servernamen, API-Schlüssel und interne Kommentare sind verboten.

Jeder Build prüft: keine Verschlüsselung, kein PDF-JavaScript, keine Launch Action, keine ausführbare OpenAction, keine Additional Actions, keine EmbeddedFiles, keine Anhänge, keine automatischen Netzwerkaufrufe, keine `file:`- oder `javascript:`-Links und keine versteckten privaten Buildinformationen. PDF/UA oder PDF/A wird ohne vollständigen geeigneten Validator niemals behauptet.

## Accessibility- und Layoutgrenzen

Die HTML-Quelle verwendet `lang="de-DE"`, einen sinnvollen Dokumenttitel, eine semantische H1–Hn-Struktur, echte Listen und Tabellen, beschreibende Linktexte sowie Alt-Texte für funktionale Bilder. Dekorative Elemente dürfen die Lesereihenfolge nicht stören. Die technische PDF-QA prüft die tatsächlich erzeugten Struktur-Tags; semantisches HTML allein gilt nicht als Nachweis.

Das Basissystem verwendet DIN A4 Hochformat mit 210 × 297 mm, Zielrändern von 20 mm innerhalb der normativen Grenzen von 18–22 mm horizontal und 16–22 mm vertikal, einer Sicherheitszone von mindestens 12 mm sowie den normierten Abstandstokens. Schriftgrößen und Farbrollen folgen dem Designstandard. Warnung und Blocker müssen zusätzlich zu Farbe durch Text, Rahmen oder Symbolik unterscheidbar sein. Tabellen, Checklisten, Eingabefelder, Ergebniszonen und Seitenumbrüche werden jeweils als eigene QA-Familien geprüft.

## Komponentenvertrag M01–M12

Die Module werden in dieser Teilphase nur vertraglich referenziert. Neue Modulnummern werden nicht eingeführt.

| ID | Zweck und semantisches HTML | Eingaben | Accessibility | Seitenumbruch | Verbotene Verwendung | QA-Familien |
|---|---|---|---|---|---|---|
| M01 | Einführung; `section`, `h1`, `p` | Ziel, Grenze, Produkt-ID | eindeutige H1 und Lesereihenfolge | nach Abschnitt erlaubt | Werbeversprechen | CONTENT, A11Y, DESIGN |
| M02 | Anleitung; `section`, `h2`, `ol` | Schritte, Voraussetzungen | echte nummerierte Liste | innerhalb eines Schritts vermeiden | unbestimmte Appelle | CONTENT, A11Y |
| M03 | Eingabe; `fieldset`, `legend`, `label`, Eingabefläche | Felddefinition, Einheit, Hinweis | Label-/Feldzuordnung, keine versteckten Pflichtdaten | Feldgruppe zusammenhalten | personenbezogene Vorbelegung, AcroForm in dieser Phase | FORM, PRIVACY, A11Y |
| M04 | Tabelle; `table`, `caption`, `thead`, `tbody`, `th`, `td` | Zeilen, Spalten, Summen | Header-Zuordnung und stabile Reihenfolge | Tabellenzeilen nicht unkontrolliert trennen | reine Dekoration, unbeschriftete Spalten | TABLE, A11Y, PRINT |
| M05 | Checkliste; `fieldset`, `legend`, `ul`/`ol`, `li` | Aufgaben, Status | sichtbarer Status und echte Liste | Checklisteneinheit zusammenhalten | lange Liste ohne Arbeitslogik | CONTENT, A11Y, RENDER |
| M06 | Hinweis; `aside` mit Überschrift | neutrale Erläuterung | nicht nur über Farbe erkennbar | nach Inhalt erlaubt | Beratung als Empfehlung | CONTENT, COLOR, A11Y |
| M07 | Warnung; `aside` mit Warnlabel | Risiko, Bedeutung, nächster Prüfschritt | Textlabel und Kontrast | Warnblock nicht teilen | Angstmarketing, Erfolgsgarantie | BOUNDARY, COLOR, A11Y |
| M08 | Blocker; `aside` mit Blockerlabel | Ausschluss, Fehler, Folgeaktion | klarer Status und nächste Aktion | Blocker nicht teilen | unklare Ampel | BOUNDARY, COLOR, A11Y |
| M09 | Ergebnis; `section`, `h2`, Statusliste | Eingaben, Ergebnis, offene Punkte | Statuswerte kontrolliert und lesbar | Ergebniszone zusammenhalten | fachliche Entscheidung aus Selbstauskunft | CONTENT, BOUNDARY, A11Y |
| M10 | Nächster Schritt; `section`, `h2`, `ol` | priorisierte Folgehandlung | genau eine Priorität, beschreibende Links | Schrittgruppen zusammenhalten | E-Mail-Erfassung, CTA-Druck | CONTENT, LINK, PRIVACY |
| M11 | Quellen; `section`, `h2`, `ul` | Quelle, Stand, Abrufdatum, Abschnitt | sichtbarer Quellenstand und Linktext | Quelle nicht von Aussage entkoppeln | Trackinglinks, verkürzte URLs | SOURCE, LINK, VERSION |
| M12 | Metadaten; `footer`, `dl` oder strukturierter Block | ID, Version, Klassen, Buildstand | maschinen- und menschenlesbar | als Einheit am Ende | private Builddaten | METADATA, VERSION, PRIVACY |

## Lebenszyklus einer PDF

1. Ein Produktprofil wird gegen `C01`–`C07`, Dokumentklasse, Risikoklasse und Aktualitätsklasse validiert.
2. Produktdaten, Quellenstand, Templateversion, Tokenversion, Komponentenvertrag und lokale Assets werden anhand des Buildvertrags eingefroren.
3. Der Offline-Build erzeugt eine isolierte HTML-/Print-CSS-Ausgabe und protokolliert Renderer, Quellencommit und Buildversion.
4. Chrome/Chromium erzeugt eine PDF in einem temporären Phasenverzeichnis.
5. Metadaten- und Sicherheitsprüfung kontrollieren die PDF-Ausgabe; es werden keine privaten oder lokalen Angaben ergänzt.
6. Technische, Accessibility-, funktionale und visuelle QA erzeugen Reports und 200-dpi-Renderbilder ausschließlich temporär.
7. Gates G1–G3 entscheiden über Architektur, Designreife und Veröffentlichungsreife. G4 prüft Release, Version, Hash und Zielartefakt.
8. Erst nach G4 darf eine freigegebene PDF nach `public-downloads/` kopiert werden. Eine Websiteänderung oder ein Deployment ist ein separater Auftrag.

## C01–C07 und C08

`C01` bis `C07` werden mit ihren normativen Primäraufgaben unterstützt: Arbeitsblätter `C01`, `C02`, `C04`; Planungsdokumente `C03`, `C07`; Quellen-/Nachweisdokumente `C05`, `C06`. Produktprofile dürfen die Risikoklasse, Aktualitätsklasse, Produktgrenze oder Beratungsgrenze nicht überschreiben.

`C08` wird nicht als statisches Produkt freigegeben. Dafür fehlen ein eigenes Datenmodell, Input-/Output-Mapping, Ergebnislogik, Datenschutz- und Speicherentscheidung, Löschkonzept, Fehler- und Versionsmodell, Renderpipeline und Missbrauchsschutz.

## Entscheidungsprotokoll und Nicht-Ziele

Festgelegt sind P2 HTML/Print als Rendererklasse, getrennte Website-/PDF-Verantwortung, lokale Assets, offline reproduzierbare Builds, versionierte Quellen und nicht versionierte generierte Artefakte. Noch nicht entschieden sind die konkrete Tokenpalette, konkrete Schriftfamilie, die Implementierungsdetails des Mastertemplates, die Werkzeugwahl für Postprocessing sowie die exakten Testskripte.

Nicht-Ziele dieser Teilphase sind C01-Inhalt, öffentliches PDF, Websiteänderung, Deployment, Lead-Erfassung, Formulare, Mastertemplate-Implementierung, M01–M12-Code, Metadaten-Postprocessing im Betrieb und eine PDF/UA- oder PDF/A-Freigabe.

## Offene Punkte für 3.2.2.2.2

- konkrete Design-Tokens innerhalb des normierten A4-Rasters festlegen;
- lokal zulässige Schriftfamilie und Lizenznachweis auswählen;
- Farbrollen mit Kontrast- und Schwarz-Weiß-Prüfung konkretisieren;
- Kopf-/Fußzeilen, Seitennummerierung und Umbruchregeln als Basissystem definieren;
- Browserpfad-Auflösung und Offline-Sperre als reproduzierbares Buildmodul spezifizieren;
- Entscheidung für PDF-Metadaten-Postprocessing und Validatoren dokumentieren;
- Ausschlussregel für `.tmp/phase-3-2-2-2-1/` vor dem ersten Build ergänzen.

## Freigabestatus

Architektur dokumentiert, Buildvertrag in der zugehörigen JSON-Datei maschinenlesbar festgelegt, keine Produktionsdatei geändert, keine PDF erzeugt, kein Template implementiert und kein Deployment durchgeführt. Die Systemarchitektur und der Buildvertrag wurden nach separater Abnahme repositoryseitig abgeschlossen. Es wurden keine Produktionsdateien, PDFs, Templates oder Websiteänderungen erzeugt und kein Deployment durchgeführt.
