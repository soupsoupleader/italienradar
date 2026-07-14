# ItaliaRadar / IMR – Phase 3.2.1.1
## Vollständige Bestandsaufnahme und Download-Bedarfsmatrix

> **Status:** ENTWURF – durch Projektleitung unabhängig rekonstruiert und fachlich geprüft.
> **Baseline-Commit:** `cb89827f3c6d92378e4f28672086d24a8d237a88`
> **Produktionsänderungen:** keine
> **PDFs, Formulare, Lead-Erfassung, Commit, Push und Deployment:** nicht Bestandteil dieses Dokuments.

## 1. Dokumentkopf

| Feld | Wert |
|---|---|
| Projekt | ItalienRadar / IMR |
| Phase | 3.2.1.1 |
| Dokument | Download-Bedarfsmatrix |
| Baseline-Commit | `cb89827f3c6d92378e4f28672086d24a8d237a88` |
| Inventur | 25 indexierte Routen plus öffentliche, nicht indexierte `/404` = 26 Seiten |
| Erstellt am | 2026-07-14T16:19:44.860278+00:00 |
| Status | ENTWURF – FREIGABE ERFORDERLICH |

## 2. Baseline und Prüfstand

Die Architektur wurde aus der bestätigten öffentlichen Plattformstruktur abgeleitet. Maßgebliche Quellen sind `sitemap.xml`, die 26 öffentlichen HTML-Dateien, die bestehende Tool-Reihenfolge, die zehn Artikel, die Hub-Struktur sowie die bereits abgeschlossenen Plattformaudits.

### 2.1 Bestätigte Abgrenzung

- `sitemap.xml` enthält 25 indexierbare öffentliche Routen.
- `/404` ist öffentlich, aber bewusst nicht indexiert.
- Rechtstexte und Fehlerseiten bleiben frei zugänglich und erhalten keine Lead-Produkte.
- Die sechs interaktiven Seiten werden nicht als statische Fragekopien dupliziert; sie erhalten später eine gemeinsame dynamische Ergebnisprotokoll-Architektur.
- Es entstehen sieben statische Dokumentkandidaten und eine dynamische Ergebnisfamilie.

## 3. Methodik

### 3.1 Entscheidungsprinzip

Ein Dokument wird nur vorgesehen, wenn es mindestens eine Funktion erfüllt, die die Webseite allein nicht ausreichend leistet: eigene Angaben festhalten, rechnen, vergleichen, Nachweise sammeln, Risiken dokumentieren, einen mehrstufigen Prozess verfolgen oder ein Toolergebnis speichern.

### 3.2 Download-Value-Score

`A×5 + B×5 + C×3 + D×3 + E×2 + F×2 − G×3 − H×3 − I×2`

| Kürzel | Kriterium |
|---|---|
| A | Handlungsbedarf |
| B | Eigenständiger Zusatznutzen |
| C | Wiederverwendung |
| D | Seitenübergreifender Nutzen |
| E | Risikoreduktion |
| F | Druck-/Offline-Nutzen |
| G | Abzug: Duplikationsrisiko |
| H | Abzug: Aktualisierungsaufwand |
| I | Abzug: Fehlinterpretationsrisiko |

Einordnung: 70–100 = P1, 50–69 = P2, 30–49 = P3, unter 30 = kein eigenständiger Download.

### 3.3 Lead-Suitability-Score

`A×5 + B×4 + C×4 + D×3 + E×2 + F×2 − G×5 − H×3`

Ein Score ab 65 zeigt grundsätzliche spätere Lead-Eignung. Er erzwingt keine E-Mail-Schranke. Strategische, rechtliche oder vertrauensbezogene Gründe können einen hochwertigen Kandidaten bewusst als Direktdownload festlegen.

## 4. Bestätigte Seiteninventur

| Nr. | Route | Datei | Seitentyp | Nutzerphase |
|---:|---|---|---|---|
| 1 | `/` | `index.html` | START | ORIENTATION |
| 2 | `/italien-kostenrechner` | `italien-kostenrechner.html` | CALCULATOR | COST_FEASIBILITY |
| 3 | `/italien-tools` | `italien-tools.html` | TOOL_HUB | ORIENTATION |
| 4 | `/napoli-neustart` | `napoli-neustart.html` | TOPIC_HUB | ORIENTATION |
| 5 | `/online-geld-in-italien` | `online-geld-in-italien.html` | TOPIC_HUB | INCOME_BUILDING |
| 6 | `/partita-iva` | `partita-iva.html` | TOPIC_HUB | SELF_EMPLOYMENT_PREP |
| 7 | `/resto-al-sud-check` | `resto-al-sud-check.html` | TOPIC_HUB | FUNDING_PREP |
| 8 | `/was-kostet-ein-neustart-in-italien` | `was-kostet-ein-neustart-in-italien.html` | ARTICLE | COST_FEASIBILITY |
| 9 | `/mit-1000-euro-in-italien-leben` | `mit-1000-euro-in-italien-leben.html` | ARTICLE | COST_FEASIBILITY |
| 10 | `/leben-in-neapel-kosten` | `leben-in-neapel-kosten.html` | ARTICLE | COST_FEASIBILITY |
| 11 | `/italien-neustart-ohne-job` | `italien-neustart-ohne-job.html` | ARTICLE | COST_FEASIBILITY |
| 12 | `/sueditalien-guenstig-leben` | `sueditalien-guenstig-leben.html` | ARTICLE | COST_FEASIBILITY |
| 13 | `/online-einkommen-in-italien-aufbauen` | `online-einkommen-in-italien-aufbauen.html` | ARTICLE | INCOME_BUILDING |
| 14 | `/online-einkommen-realitaetscheck` | `online-einkommen-realitaetscheck.html` | PRECHECK | INCOME_STABILITY |
| 15 | `/dach-einnahmen-italien-kostenstruktur` | `dach-einnahmen-italien-kostenstruktur.html` | ARTICLE | INCOME_STABILITY |
| 16 | `/dach-italien-hebel-rechner` | `dach-italien-hebel-rechner.html` | CALCULATOR | INCOME_STABILITY |
| 17 | `/partita-iva-vorpruefung` | `partita-iva-vorpruefung.html` | PRECHECK | SELF_EMPLOYMENT_PREP |
| 18 | `/partita-iva-deutsche-italien` | `partita-iva-deutsche-italien.html` | ARTICLE | SELF_EMPLOYMENT_PREP |
| 19 | `/regime-forfettario-italien-deutsche` | `regime-forfettario-italien-deutsche.html` | ARTICLE | TAX_CONTRIBUTION |
| 20 | `/forfettario-realitaetscheck` | `forfettario-realitaetscheck.html` | PRECHECK | TAX_CONTRIBUTION |
| 21 | `/resto-al-sud-2-vorpruefung` | `resto-al-sud-2-vorpruefung.html` | PRECHECK | FUNDING_PREP |
| 22 | `/resto-al-sud-2-deutsche-italien` | `resto-al-sud-2-deutsche-italien.html` | ARTICLE | FUNDING_PREP |
| 23 | `/ratgeber` | `ratgeber.html` | GUIDE_HUB | ORIENTATION |
| 24 | `/impressum` | `impressum.html` | LEGAL | LEGAL_TRANSPARENCY |
| 25 | `/datenschutz` | `datenschutz.html` | LEGAL | LEGAL_TRANSPARENCY |
| 26 | `/404` | `404.html` | ERROR | ERROR_RECOVERY |

## 5. Vollständige 26-Seiten-Bedarfsmatrix

| Nr. | Route | Hauptproblem / Nutzeraufgabe | Bedarf | Entscheidung | Kandidat | Klasse | Download | Lead | Update | Priorität |
|---:|---|---|---|---|---|---|---:|---:|---|---|
| 1 | `/` | Der Nutzer braucht einen geordneten Einstieg statt einzelner, unverbundener Informationen. Aufgabe: Den passenden ersten Prüfpfad wählen. | keiner | `NONE` | — | — | 18 | 20 | U1_STABLE | keine |
| 2 | `/italien-kostenrechner` | Eigene Einnahmen, Fixkosten, Lebenshaltung und Reserve müssen in einer belastbaren Rechnung zusammengeführt werden. Aufgabe: Werte eingeben, Ergebniszone verstehen und später erneut vergleichen. | hoch | `DYNAMIC_LATER` | C08 | D | 88 | 78 | U2_MOVING | P3 |
| 3 | `/italien-tools` | Die Prüfreihenfolge Einkommen, Kosten, Struktur, Steuer und Förderung muss verständlich werden. Aufgabe: Das passende Tool in der richtigen Reihenfolge auswählen. | keiner | `NONE` | — | — | 22 | 18 | U1_STABLE | keine |
| 4 | `/napoli-neustart` | Napoli wird häufig emotional statt nach Alltag, Kosten und Risiken beurteilt. Aufgabe: Standortfragen strukturieren und in die Kostenprüfung wechseln. | mittel | `MERGE` | C02 | B | 54 | 46 | U2_MOVING | P3 |
| 5 | `/online-geld-in-italien` | Online-Einkommen wird als Idee oder Technik statt als nachweisbares System verstanden. Aufgabe: Das passende Aufbau- und Prüfmodul wählen. | mittel | `MERGE` | C03 | C | 58 | 55 | U2_MOVING | P1 |
| 6 | `/partita-iva` | Nutzer springen zu Eröffnung oder Steuersatz, bevor Tätigkeit und Status geklärt sind. Aufgabe: Relevanz einordnen und Unterlagen-/Fragenvorbereitung starten. | mittel | `MERGE` | C05 | E | 60 | 50 | U3_SENSITIVE | P1 |
| 7 | `/resto-al-sud-check` | Förderung wird als Finanzierungssicherheit betrachtet, bevor Projekt und Voraussetzungen geprüft sind. Aufgabe: Prüfreihenfolge verstehen und zur aktuellen Vorprüfung wechseln. | mittel | `MERGE` | C07 | C | 62 | 52 | U4_EVENT_DRIVEN | P2 |
| 8 | `/was-kostet-ein-neustart-in-italien` | Monatskosten, Startkosten, Rücklagen und Risikofälle werden nicht als Gesamtsystem gerechnet. Aufgabe: Eigene Werte und Sicherheitsgrenzen dokumentieren. | hoch | `FREE_DIRECT` | C01 | B | 89 | 79 | U2_MOVING | P1 |
| 9 | `/mit-1000-euro-in-italien-leben` | Ein fixer Monatsbetrag wird ohne Wohn-, Gesundheits-, Mobilitäts- und Pufferprüfung bewertet. Aufgabe: Minimalbudget gegen individuelle Stressfaktoren prüfen. | mittel | `MERGE` | C01 | B | 64 | 52 | U2_MOVING | P1 |
| 10 | `/leben-in-neapel-kosten` | Napoli wird nach Einzelpreisen beurteilt, ohne Alltag, Lage, Mobilität und Risiko zu gewichten. Aufgabe: Standorte und Alltagstauglichkeit mit einem einheitlichen Raster vergleichen. | mittel | `FREE_DIRECT` | C02 | B | 58 | 57 | U2_MOVING | P3 |
| 11 | `/italien-neustart-ohne-job` | Umzug ohne Einkommen wird ohne Reichweite des Puffers, Abbruchkosten und Aufbauzeit bewertet. Aufgabe: Sicherheitszeitraum, Mindestreserve und Einkommensplan dokumentieren. | hoch | `MERGE` | C01 | B | 67 | 63 | U2_MOVING | P1 |
| 12 | `/sueditalien-guenstig-leben` | Günstige Mieten werden mit einem insgesamt tragfähigen Standort verwechselt. Aufgabe: Kosten- und Infrastrukturkompromisse mehrerer Orte vergleichen. | mittel | `MERGE` | C02 | B | 55 | 48 | U2_MOVING | P3 |
| 13 | `/online-einkommen-in-italien-aufbauen` | Nutzer brauchen eine prüfbare Strecke von Angebot und Nachfrage bis zu stabilen Einnahmen. Aufgabe: Belege, Kunden, Einnahmenhistorie und Rücklagen über mehrere Monate dokumentieren. | hoch | `LEAD_LATER` | C03 | C | 82 | 83 | U2_MOVING | P1 |
| 14 | `/online-einkommen-realitaetscheck` | Der aktuelle Einkommensstatus und die offenen Nachweise sollen eindeutig festgehalten werden. Aufgabe: Antworten eingeben, Ergebniszone verstehen und später vergleichen. | hoch | `DYNAMIC_LATER` | C08 | D | 84 | 80 | U2_MOVING | P3 |
| 15 | `/dach-einnahmen-italien-kostenstruktur` | DACH-Brutto wird ohne Abgaben, Geschäftskosten, Reisen und Kundenrisiko als Italien-Budget betrachtet. Aufgabe: Tragfähigkeit und Stressmonat mit realen Abzügen dokumentieren. | hoch | `LEAD_LATER` | C04 | B | 76 | 79 | U3_SENSITIVE | P2 |
| 16 | `/dach-italien-hebel-rechner` | Rechnerergebnisse, Stressmonat und Kundenrisiko müssen speicherbar werden. Aufgabe: Eingaben und Ergebniszone dokumentieren. | hoch | `DYNAMIC_LATER` | C08 | D | 90 | 82 | U3_SENSITIVE | P3 |
| 17 | `/partita-iva-vorpruefung` | Die Ergebniszone und offenen Status-/Unterlagenfragen müssen für die Fachprüfung festgehalten werden. Aufgabe: Antworten dokumentieren und Fragen an Fachstellen vorbereiten. | hoch | `DYNAMIC_LATER` | C08 | D | 86 | 72 | U3_SENSITIVE | P3 |
| 18 | `/partita-iva-deutsche-italien` | Sachverhalt und Unterlagen sind vor Eröffnung oder Beratung nicht strukturiert. Aufgabe: Relevante Daten, Nachweise und Fachfragen sammeln. | hoch | `FREE_DIRECT` | C05 | E | 76 | 56 | U3_SENSITIVE | P1 |
| 19 | `/regime-forfettario-italien-deutsche` | Steuersatz, Ausschlussgründe, Beiträge und Liquidität werden nicht gemeinsam geprüft. Aufgabe: Offene Fachfragen und Rechenannahmen vor einer professionellen Prüfung dokumentieren. | mittel | `FREE_DIRECT` | C06 | E | 50 | 51 | U3_SENSITIVE | P2 |
| 20 | `/forfettario-realitaetscheck` | Ergebniszone, Ausschlussrisiken und offene Beitragsfragen sollen dokumentiert werden. Aufgabe: Antworten und nächste Fachprüfungen festhalten. | hoch | `DYNAMIC_LATER` | C08 | D | 84 | 78 | U3_SENSITIVE | P3 |
| 21 | `/resto-al-sud-2-vorpruefung` | Ergebniszone, Ausschlüsse, Projektlücken und Antragsreife sollen nachvollziehbar festgehalten werden. Aufgabe: Antworten, offene Nachweise und aktuelle Quellen dokumentieren. | hoch | `DYNAMIC_LATER` | C08 | D | 88 | 80 | U4_EVENT_DRIVEN | P3 |
| 22 | `/resto-al-sud-2-deutsche-italien` | Projektidee, Kostenplan, Liquidität, Unterlagen und offizielle Anforderungen sind nicht als Arbeitsprozess gebündelt. Aufgabe: Projekt- und Antragsvorbereitung strukturiert dokumentieren. | hoch | `LEAD_LATER` | C07 | C | 71 | 65 | U4_EVENT_DRIVEN | P2 |
| 23 | `/ratgeber` | Der Nutzer sucht den passenden Vertiefungsartikel. Aufgabe: Artikel nach Problem und Phase auswählen. | keiner | `NONE` | — | — | 20 | 17 | U1_STABLE | keine |
| 24 | `/impressum` | Anbieterkennzeichnung muss frei und aktuell zugänglich sein. Aufgabe: Rechtliche Anbieterinformationen lesen. | keiner | `NONE` | — | — | 4 | 0 | U1_STABLE | keine |
| 25 | `/datenschutz` | Datenverarbeitung muss transparent und frei zugänglich erklärt werden. Aufgabe: Datenschutzinformationen lesen. | keiner | `NONE` | — | — | 4 | 0 | U1_STABLE | keine |
| 26 | `/404` | Der Nutzer muss aus einem Fehlpfad sicher zurückgeführt werden. Aufgabe: Zur Startseite oder einem Kernwerkzeug zurückkehren. | keiner | `NONE` | — | — | 2 | 0 | U1_STABLE | keine |

### 5.1 Entscheidungssummen

- `NONE`: 6
- `DYNAMIC_LATER`: 6
- `MERGE`: 7
- `FREE_DIRECT`: 4
- `LEAD_LATER`: 3

Summe: **26 Seiten**.

## 6. Detaillierte Seitenprofile

### 1. `/` – Berechne deinen Neustart in Italien, bevor du alles riskierst.

- **Datei:** `index.html`
- **Seitentyp / Nutzerphase:** `START` / `ORIENTATION`
- **Primäres Problem:** Der Nutzer braucht einen geordneten Einstieg statt einzelner, unverbundener Informationen.
- **Nutzeraufgabe:** Den passenden ersten Prüfpfad wählen.
- **Bestehende Funktion:** Systemübersicht, Säulen, Einstieg zu Rechnern und Hubs.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Ein eigener Download würde die Startseite nur duplizieren; die spätere Downloadübersicht gehört als Web-Navigation auf die Plattform.
- **Zielgruppe:** alle Einstiegsnutzer
- **Nächster Schritt:** `/italien-kostenrechner`
- **Scores:** Download 18 / Lead 20
- **Aktualität / Sensitivität:** `U1_STABLE` / niedrig
- **Begründung:** Die Startseite soll führen, nicht selbst ein Dokumentprodukt werden. Downloads werden kontextuell an Fachseiten angeboten.

### 2. `/italien-kostenrechner` – Italien-Kostenrechner

- **Datei:** `italien-kostenrechner.html`
- **Seitentyp / Nutzerphase:** `CALCULATOR` / `COST_FEASIBILITY`
- **Primäres Problem:** Eigene Einnahmen, Fixkosten, Lebenshaltung und Reserve müssen in einer belastbaren Rechnung zusammengeführt werden.
- **Nutzeraufgabe:** Werte eingeben, Ergebniszone verstehen und später erneut vergleichen.
- **Bestehende Funktion:** Interaktiver Rechner mit Risikoauswertung.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Ein dynamisches Protokoll kann Eingaben, Ergebniszone, Warnungen und Prüfdatum speichern; statisch ergänzt C01 die Planung.
- **Zielgruppe:** Nutzer mit konkretem Italien-Budget
- **Nächster Schritt:** `/was-kostet-ein-neustart-in-italien`
- **Scores:** Download 88 / Lead 78
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Der stärkste Mehrwert ist keine allgemeine PDF-Kopie, sondern eine später generierte Ergebnisdatei. C01 bleibt das statische Arbeitsinstrument.

### 3. `/italien-tools` – ItalienRadar Tools

- **Datei:** `italien-tools.html`
- **Seitentyp / Nutzerphase:** `TOOL_HUB` / `ORIENTATION`
- **Primäres Problem:** Die Prüfreihenfolge Einkommen, Kosten, Struktur, Steuer und Förderung muss verständlich werden.
- **Nutzeraufgabe:** Das passende Tool in der richtigen Reihenfolge auswählen.
- **Bestehende Funktion:** Tool-Hub und Prozessnavigation.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Ein Gesamtcheck würde die spezialisierten Dokumente verwässern; die Hub-Seite bleibt die bessere, aktualisierbare Navigation.
- **Zielgruppe:** Nutzer mehrerer Prüfmodule
- **Nächster Schritt:** `/online-einkommen-realitaetscheck`
- **Scores:** Download 22 / Lead 18
- **Aktualität / Sensitivität:** `U1_STABLE` / niedrig
- **Begründung:** Der Hub soll auf konkrete Arbeitsdokumente verweisen, aber kein eigenes Sammel-PDF erzeugen.

### 4. `/napoli-neustart` – Napoli-Neustart realistisch prüfen

- **Datei:** `napoli-neustart.html`
- **Seitentyp / Nutzerphase:** `TOPIC_HUB` / `ORIENTATION`
- **Primäres Problem:** Napoli wird häufig emotional statt nach Alltag, Kosten und Risiken beurteilt.
- **Nutzeraufgabe:** Standortfragen strukturieren und in die Kostenprüfung wechseln.
- **Bestehende Funktion:** Napoli-Hub mit Chancen, Risiken und Folgeschritten.
- **Entscheidung:** `MERGE`
- **Kandidat:** C02
- **Zusatznutzen:** C02 stellt ein wiederverwendbares Ortsvergleichsraster bereit; ein eigenes Hub-PDF wäre redundant.
- **Zielgruppe:** Napoli- und Süditalien-Interessierte
- **Nächster Schritt:** `/leben-in-neapel-kosten`
- **Scores:** Download 54 / Lead 46
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Die Seite ist ein Einstieg. Der Arbeitsbedarf liegt beim Vergleich konkreter Standorte und wird deshalb in C02 gebündelt.

### 5. `/online-geld-in-italien` – Online-Geld in Italien aufbauen

- **Datei:** `online-geld-in-italien.html`
- **Seitentyp / Nutzerphase:** `TOPIC_HUB` / `INCOME_BUILDING`
- **Primäres Problem:** Online-Einkommen wird als Idee oder Technik statt als nachweisbares System verstanden.
- **Nutzeraufgabe:** Das passende Aufbau- und Prüfmodul wählen.
- **Bestehende Funktion:** Hub zu Online-Einkommen, Artikeln und Tools.
- **Entscheidung:** `MERGE`
- **Kandidat:** C03
- **Zusatznutzen:** C03 übersetzt die Hub-Logik in einen mehrmonatigen Nachweis- und Stabilitätsprozess.
- **Zielgruppe:** angehende digitale Selbstständige und Remote-Nutzer
- **Nächster Schritt:** `/online-einkommen-in-italien-aufbauen`
- **Scores:** Download 58 / Lead 55
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Kein separates Hub-Dokument. Der konkrete Arbeitsbedarf ist bereits vollständig durch C03 abgedeckt.

### 6. `/partita-iva` – Partita IVA Grundcheck

- **Datei:** `partita-iva.html`
- **Seitentyp / Nutzerphase:** `TOPIC_HUB` / `SELF_EMPLOYMENT_PREP`
- **Primäres Problem:** Nutzer springen zu Eröffnung oder Steuersatz, bevor Tätigkeit und Status geklärt sind.
- **Nutzeraufgabe:** Relevanz einordnen und Unterlagen-/Fragenvorbereitung starten.
- **Bestehende Funktion:** Grundorientierung und Weiterleitung zu Artikel und Vorprüfung.
- **Entscheidung:** `MERGE`
- **Kandidat:** C05
- **Zusatznutzen:** C05 bietet das konkrete Vorbereitungspaket; ein separates Hub-PDF würde dieselben Fragen wiederholen.
- **Zielgruppe:** Nutzer mit geplanter Selbstständigkeit in Italien
- **Nächster Schritt:** `/partita-iva-deutsche-italien`
- **Scores:** Download 60 / Lead 50
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Die sensible Basis bleibt auf der Website frei; das Dokument unterstützt die fachliche Vorbereitung.

### 7. `/resto-al-sud-check` – Resto al Sud Fördercheck

- **Datei:** `resto-al-sud-check.html`
- **Seitentyp / Nutzerphase:** `TOPIC_HUB` / `FUNDING_PREP`
- **Primäres Problem:** Förderung wird als Finanzierungssicherheit betrachtet, bevor Projekt und Voraussetzungen geprüft sind.
- **Nutzeraufgabe:** Prüfreihenfolge verstehen und zur aktuellen Vorprüfung wechseln.
- **Bestehende Funktion:** Förder-Hub und vorsichtige Grundorientierung.
- **Entscheidung:** `MERGE`
- **Kandidat:** C07
- **Zusatznutzen:** C07 bündelt die tatsächliche Projekt- und Unterlagenarbeit; der Hub bleibt frei zugänglich.
- **Zielgruppe:** Gründungs- und Förderinteressierte
- **Nächster Schritt:** `/resto-al-sud-2-deutsche-italien`
- **Scores:** Download 62 / Lead 52
- **Aktualität / Sensitivität:** `U4_EVENT_DRIVEN` / sehr hoch
- **Begründung:** Ein eigenes Hub-PDF wäre zu allgemein und schnell veraltet. Die Arbeitsleistung wird in C07 konzentriert.

### 8. `/was-kostet-ein-neustart-in-italien` – Was kostet ein Neustart in Italien wirklich?

- **Datei:** `was-kostet-ein-neustart-in-italien.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `COST_FEASIBILITY`
- **Primäres Problem:** Monatskosten, Startkosten, Rücklagen und Risikofälle werden nicht als Gesamtsystem gerechnet.
- **Nutzeraufgabe:** Eigene Werte und Sicherheitsgrenzen dokumentieren.
- **Bestehende Funktion:** Kostenartikel mit Ebenen, Szenarien, Tabellen und Risikologik.
- **Entscheidung:** `FREE_DIRECT`
- **Kandidat:** C01
- **Zusatznutzen:** C01 ermöglicht persönliche Eintragungen, Szenarienvergleich und eine dokumentierte Mindestreserve.
- **Zielgruppe:** Auswanderungsinteressierte mit konkretem Budget
- **Nächster Schritt:** `/italien-kostenrechner`
- **Scores:** Download 89 / Lead 79
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Stärkster statischer Downloadkandidat und sinnvoller erster Design-/Funktionsprototyp.

### 9. `/mit-1000-euro-in-italien-leben` – Mit 1.000 Euro in Italien leben: realistisch oder riskant?

- **Datei:** `mit-1000-euro-in-italien-leben.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `COST_FEASIBILITY`
- **Primäres Problem:** Ein fixer Monatsbetrag wird ohne Wohn-, Gesundheits-, Mobilitäts- und Pufferprüfung bewertet.
- **Nutzeraufgabe:** Minimalbudget gegen individuelle Stressfaktoren prüfen.
- **Bestehende Funktion:** Szenarien, Fehler, Risikoampel und Checkliste.
- **Entscheidung:** `MERGE`
- **Kandidat:** C01
- **Zusatznutzen:** Ein separates 1.000-Euro-PDF wäre zu eng und duplizierend; C01 enthält einen eigenen Minimalbudget-/Stressfall.
- **Zielgruppe:** Nutzer mit sehr kleinem Budget
- **Nächster Schritt:** `/italien-kostenrechner`
- **Scores:** Download 64 / Lead 52
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Thema bleibt als Modul in C01 erhalten, nicht als isoliertes Produkt.

### 10. `/leben-in-neapel-kosten` – Leben in Neapel: Kosten, Alltag und Risiken

- **Datei:** `leben-in-neapel-kosten.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `COST_FEASIBILITY`
- **Primäres Problem:** Napoli wird nach Einzelpreisen beurteilt, ohne Alltag, Lage, Mobilität und Risiko zu gewichten.
- **Nutzeraufgabe:** Standorte und Alltagstauglichkeit mit einem einheitlichen Raster vergleichen.
- **Bestehende Funktion:** Detaillierter Standortartikel mit Tabellen und Risikoaspekten.
- **Entscheidung:** `FREE_DIRECT`
- **Kandidat:** C02
- **Zusatznutzen:** C02 macht mehrere Orte vergleichbar und dokumentiert persönliche Muss-/Ausschlusskriterien.
- **Zielgruppe:** Napoli- und Süditalien-Interessierte
- **Nächster Schritt:** `/napoli-neustart`
- **Scores:** Download 58 / Lead 57
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Sinnvoll, aber wegen beweglicher Ortsdaten erst nach dem Kernsystem produzieren.

### 11. `/italien-neustart-ohne-job` – Nach Italien ziehen ohne Job: wann es gefährlich wird

- **Datei:** `italien-neustart-ohne-job.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `COST_FEASIBILITY`
- **Primäres Problem:** Umzug ohne Einkommen wird ohne Reichweite des Puffers, Abbruchkosten und Aufbauzeit bewertet.
- **Nutzeraufgabe:** Sicherheitszeitraum, Mindestreserve und Einkommensplan dokumentieren.
- **Bestehende Funktion:** Risikoartikel mit Szenarien und Sicherheitslogik.
- **Entscheidung:** `MERGE`
- **Kandidat:** C01
- **Zusatznutzen:** C01 übernimmt Puffer und Abbruchreserve; C03 ergänzt den Einkommensaufbau. Ein drittes Dokument wäre redundant.
- **Zielgruppe:** Nutzer ohne gesichertes Einkommen
- **Nächster Schritt:** `/online-einkommen-realitaetscheck`
- **Scores:** Download 67 / Lead 63
- **Aktualität / Sensitivität:** `U2_MOVING` / hoch
- **Begründung:** Bewusst in C01 gebündelt und als sekundäre Nutzerreise mit C03 verknüpft.

### 12. `/sueditalien-guenstig-leben` – Günstig leben in Süditalien: was realistisch ist

- **Datei:** `sueditalien-guenstig-leben.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `COST_FEASIBILITY`
- **Primäres Problem:** Günstige Mieten werden mit einem insgesamt tragfähigen Standort verwechselt.
- **Nutzeraufgabe:** Kosten- und Infrastrukturkompromisse mehrerer Orte vergleichen.
- **Bestehende Funktion:** Vergleichsartikel mit Kosten- und Alltagsfaktoren.
- **Entscheidung:** `MERGE`
- **Kandidat:** C02
- **Zusatznutzen:** C02 enthält das benötigte Vergleichsraster; ein separates Süditalien-Blatt würde denselben Prozess duplizieren.
- **Zielgruppe:** Menschen mit kleinem Budget und Süditalien-Fokus
- **Nächster Schritt:** `/leben-in-neapel-kosten`
- **Scores:** Download 55 / Lead 48
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** In C02 zusammenführen; keine pauschale Bestenliste oder Standortberatung erzeugen.

### 13. `/online-einkommen-in-italien-aufbauen` – Online-Einkommen in Italien aufbauen

- **Datei:** `online-einkommen-in-italien-aufbauen.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `INCOME_BUILDING`
- **Primäres Problem:** Nutzer brauchen eine prüfbare Strecke von Angebot und Nachfrage bis zu stabilen Einnahmen.
- **Nutzeraufgabe:** Belege, Kunden, Einnahmenhistorie und Rücklagen über mehrere Monate dokumentieren.
- **Bestehende Funktion:** Tiefenartikel mit Mindestprüfung, Risiken und Nachweislogik.
- **Entscheidung:** `LEAD_LATER`
- **Kandidat:** C03
- **Zusatznutzen:** C03 ist ein eigenständiger, fortlaufend nutzbarer Arbeitsprozess und deutlich mehr als eine Artikelzusammenfassung.
- **Zielgruppe:** angehende Online-Selbstständige und Remote-Nutzer
- **Nächster Schritt:** `/online-einkommen-realitaetscheck`
- **Scores:** Download 82 / Lead 83
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Starker Lead-Magnet-Kandidat, aber bis Phase 3.2.6 keine E-Mail-Erfassung.

### 14. `/online-einkommen-realitaetscheck` – Online-Einkommen-Realitätscheck

- **Datei:** `online-einkommen-realitaetscheck.html`
- **Seitentyp / Nutzerphase:** `PRECHECK` / `INCOME_STABILITY`
- **Primäres Problem:** Der aktuelle Einkommensstatus und die offenen Nachweise sollen eindeutig festgehalten werden.
- **Nutzeraufgabe:** Antworten eingeben, Ergebniszone verstehen und später vergleichen.
- **Bestehende Funktion:** Interaktive Vorprüfung.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Eine generierte Datei speichert Ergebniszone und offene Nachweise; C03 bleibt der statische Aufbauplan.
- **Zielgruppe:** Nutzer mit geplantem oder bestehendem Online-Einkommen
- **Nächster Schritt:** `/dach-italien-hebel-rechner`
- **Scores:** Download 84 / Lead 80
- **Aktualität / Sensitivität:** `U2_MOVING` / mittel
- **Begründung:** Nicht als statische Wiederholung bauen; später als datensparsame Ergebnisexport-Funktion.

### 15. `/dach-einnahmen-italien-kostenstruktur` – DACH-Einnahmen und Italien-Kosten: wann der Hebel realistisch wird

- **Datei:** `dach-einnahmen-italien-kostenstruktur.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `INCOME_STABILITY`
- **Primäres Problem:** DACH-Brutto wird ohne Abgaben, Geschäftskosten, Reisen und Kundenrisiko als Italien-Budget betrachtet.
- **Nutzeraufgabe:** Tragfähigkeit und Stressmonat mit realen Abzügen dokumentieren.
- **Bestehende Funktion:** Tiefenartikel mit Szenarien, Klumpenrisiko und Nachweisen.
- **Entscheidung:** `LEAD_LATER`
- **Kandidat:** C04
- **Zusatznutzen:** C04 erlaubt eine persönliche Netto-Brücke, Kundenrisiko- und Stressmonatrechnung.
- **Zielgruppe:** Remote-Beschäftigte, Freelancer und Selbstständige
- **Nächster Schritt:** `/dach-italien-hebel-rechner`
- **Scores:** Download 76 / Lead 79
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Eigenständiges Arbeitsproblem; bewusst von C03 getrennt, weil hier grenzüberschreitende Kosten- und Statusannahmen dominieren.

### 16. `/dach-italien-hebel-rechner` – DACH-Italien-Hebel-Rechner

- **Datei:** `dach-italien-hebel-rechner.html`
- **Seitentyp / Nutzerphase:** `CALCULATOR` / `INCOME_STABILITY`
- **Primäres Problem:** Rechnerergebnisse, Stressmonat und Kundenrisiko müssen speicherbar werden.
- **Nutzeraufgabe:** Eingaben und Ergebniszone dokumentieren.
- **Bestehende Funktion:** Interaktiver Tragfähigkeitsrechner.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Dynamischer Export bewahrt konkrete Werte; C04 dient als statischer Vertiefungs- und Planungsbogen.
- **Zielgruppe:** Nutzer mit DACH-Einnahmen
- **Nächster Schritt:** `/partita-iva-vorpruefung`
- **Scores:** Download 90 / Lead 82
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Dynamische Ergebnisdatei ist funktional stärker als ein zweiter statischer Rechnerabdruck.

### 17. `/partita-iva-vorpruefung` – Partita-IVA-Vorprüfung

- **Datei:** `partita-iva-vorpruefung.html`
- **Seitentyp / Nutzerphase:** `PRECHECK` / `SELF_EMPLOYMENT_PREP`
- **Primäres Problem:** Die Ergebniszone und offenen Status-/Unterlagenfragen müssen für die Fachprüfung festgehalten werden.
- **Nutzeraufgabe:** Antworten dokumentieren und Fragen an Fachstellen vorbereiten.
- **Bestehende Funktion:** Interaktive Struktur- und Relevanzvorprüfung.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Späterer Export hält Eingaben, Ergebnis und offene Punkte fest; C05 liefert die statische Unterlagenliste.
- **Zielgruppe:** Nutzer vor einer möglichen italienischen Selbstständigkeit
- **Nächster Schritt:** `/partita-iva-deutsche-italien`
- **Scores:** Download 86 / Lead 72
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Ergebnisexport erst nach Datenschutz- und Architekturentscheidung; keine individuelle Beratung suggerieren.

### 18. `/partita-iva-deutsche-italien` – Partita IVA für Deutsche in Italien

- **Datei:** `partita-iva-deutsche-italien.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `SELF_EMPLOYMENT_PREP`
- **Primäres Problem:** Sachverhalt und Unterlagen sind vor Eröffnung oder Beratung nicht strukturiert.
- **Nutzeraufgabe:** Relevante Daten, Nachweise und Fachfragen sammeln.
- **Bestehende Funktion:** Tiefenartikel mit Grundlogik, Risiken und Quellen.
- **Entscheidung:** `FREE_DIRECT`
- **Kandidat:** C05
- **Zusatznutzen:** C05 erzeugt ein konkretes Vorbereitungspaket für Commercialista oder offizielle Stellen.
- **Zielgruppe:** deutschsprachige Gründungs- und Selbstständigkeitsinteressierte
- **Nächster Schritt:** `/partita-iva-vorpruefung`
- **Scores:** Download 76 / Lead 56
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Wichtige Vorbereitung darf nicht künstlich gegatet werden; Quellenstand und Disclaimer sind Pflicht.

### 19. `/regime-forfettario-italien-deutsche` – Regime forfettario für Deutsche in Italien

- **Datei:** `regime-forfettario-italien-deutsche.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `TAX_CONTRIBUTION`
- **Primäres Problem:** Steuersatz, Ausschlussgründe, Beiträge und Liquidität werden nicht gemeinsam geprüft.
- **Nutzeraufgabe:** Offene Fachfragen und Rechenannahmen vor einer professionellen Prüfung dokumentieren.
- **Bestehende Funktion:** Tiefenartikel mit Szenarien, Ausschlüssen und INPS-Logik.
- **Entscheidung:** `FREE_DIRECT`
- **Kandidat:** C06
- **Zusatznutzen:** C06 strukturiert die individuellen offenen Fragen, ohne eine steuerliche Antwort vorzugeben.
- **Zielgruppe:** Nutzer mit möglicher Forfettario-Relevanz
- **Nächster Schritt:** `/forfettario-realitaetscheck`
- **Scores:** Download 50 / Lead 51
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Nur als freier Klärungsbogen sinnvoll; als Lead-Magnet wäre die Beratungsnähe zu problematisch.

### 20. `/forfettario-realitaetscheck` – Forfettario-Realitätscheck

- **Datei:** `forfettario-realitaetscheck.html`
- **Seitentyp / Nutzerphase:** `PRECHECK` / `TAX_CONTRIBUTION`
- **Primäres Problem:** Ergebniszone, Ausschlussrisiken und offene Beitragsfragen sollen dokumentiert werden.
- **Nutzeraufgabe:** Antworten und nächste Fachprüfungen festhalten.
- **Bestehende Funktion:** Interaktive Steuer-/Beitragsrealitätsprüfung.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Ein späterer Export kann Ergebnis und Quellenstand festhalten; C06 bleibt der statische Fragenbogen.
- **Zielgruppe:** Nutzer mit geplanter Forfettario-Prüfung
- **Nächster Schritt:** `/regime-forfettario-italien-deutsche`
- **Scores:** Download 84 / Lead 78
- **Aktualität / Sensitivität:** `U3_SENSITIVE` / hoch
- **Begründung:** Dynamischer Export nur mit klarer Nichtberatungs-Abgrenzung und aktueller Toollogik.

### 21. `/resto-al-sud-2-vorpruefung` – Resto al Sud 2.0 Vorprüfung

- **Datei:** `resto-al-sud-2-vorpruefung.html`
- **Seitentyp / Nutzerphase:** `PRECHECK` / `FUNDING_PREP`
- **Primäres Problem:** Ergebniszone, Ausschlüsse, Projektlücken und Antragsreife sollen nachvollziehbar festgehalten werden.
- **Nutzeraufgabe:** Antworten, offene Nachweise und aktuelle Quellen dokumentieren.
- **Bestehende Funktion:** Interaktive Fördervorprüfung.
- **Entscheidung:** `DYNAMIC_LATER`
- **Kandidat:** C08
- **Zusatznutzen:** Dynamischer Export dokumentiert den Prüfzeitpunkt und offene Punkte; C07 führt die Projektarbeit.
- **Zielgruppe:** Förderinteressierte mit konkreter Projektidee
- **Nächster Schritt:** `/resto-al-sud-2-deutsche-italien`
- **Scores:** Download 88 / Lead 80
- **Aktualität / Sensitivität:** `U4_EVENT_DRIVEN` / sehr hoch
- **Begründung:** Wegen beweglicher Programmdetails nur später dynamisch und mit sichtbarem Quellen-/Zeitstand.

### 22. `/resto-al-sud-2-deutsche-italien` – Resto al Sud 2.0 für Deutsche in Italien

- **Datei:** `resto-al-sud-2-deutsche-italien.html`
- **Seitentyp / Nutzerphase:** `ARTICLE` / `FUNDING_PREP`
- **Primäres Problem:** Projektidee, Kostenplan, Liquidität, Unterlagen und offizielle Anforderungen sind nicht als Arbeitsprozess gebündelt.
- **Nutzeraufgabe:** Projekt- und Antragsvorbereitung strukturiert dokumentieren.
- **Bestehende Funktion:** Tiefenartikel mit Förderlogik, Grenzen und offiziellen Quellen.
- **Entscheidung:** `LEAD_LATER`
- **Kandidat:** C07
- **Zusatznutzen:** C07 ist ein umfassendes Projektarbeitsbuch und kein Ersatz für Invitalia oder Beratung.
- **Zielgruppe:** Gründungs- und Förderinteressierte
- **Nächster Schritt:** `/resto-al-sud-2-vorpruefung`
- **Scores:** Download 71 / Lead 65
- **Aktualität / Sensitivität:** `U4_EVENT_DRIVEN` / sehr hoch
- **Begründung:** Hoher Nutzwert, aber hoher Pflegeaufwand; erst nach stabiler PDF- und Aktualisierungsarchitektur.

### 23. `/ratgeber` – Ratgeber für deinen Italien-Neustart

- **Datei:** `ratgeber.html`
- **Seitentyp / Nutzerphase:** `GUIDE_HUB` / `ORIENTATION`
- **Primäres Problem:** Der Nutzer sucht den passenden Vertiefungsartikel.
- **Nutzeraufgabe:** Artikel nach Problem und Phase auswählen.
- **Bestehende Funktion:** Ratgeberübersicht und Content-Navigation.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Ein Ratgeber-Sammel-PDF würde Inhalte duplizieren und schnell veralten.
- **Zielgruppe:** Informationssuchende
- **Nächster Schritt:** `/was-kostet-ein-neustart-in-italien`
- **Scores:** Download 20 / Lead 17
- **Aktualität / Sensitivität:** `U1_STABLE` / niedrig
- **Begründung:** Später kann die Seite Downloads katalogisieren, benötigt aber kein eigenes Dokument.

### 24. `/impressum` – Impressum

- **Datei:** `impressum.html`
- **Seitentyp / Nutzerphase:** `LEGAL` / `LEGAL_TRANSPARENCY`
- **Primäres Problem:** Anbieterkennzeichnung muss frei und aktuell zugänglich sein.
- **Nutzeraufgabe:** Rechtliche Anbieterinformationen lesen.
- **Bestehende Funktion:** Rechtliche Pflichtseite.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Kein PDF-Nutzen; eine zweite Version erhöht Inkonsistenzrisiko.
- **Zielgruppe:** alle Nutzer
- **Nächster Schritt:** `/`
- **Scores:** Download 4 / Lead 0
- **Aktualität / Sensitivität:** `U1_STABLE` / hoch
- **Begründung:** Rechtstext bleibt als aktuelle Webversion maßgeblich.

### 25. `/datenschutz` – Datenschutz

- **Datei:** `datenschutz.html`
- **Seitentyp / Nutzerphase:** `LEGAL` / `LEGAL_TRANSPARENCY`
- **Primäres Problem:** Datenverarbeitung muss transparent und frei zugänglich erklärt werden.
- **Nutzeraufgabe:** Datenschutzinformationen lesen.
- **Bestehende Funktion:** Datenschutzerklärung.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Ein PDF würde leicht veralten und darf nie an eine E-Mail-Abgabe gekoppelt werden.
- **Zielgruppe:** alle Nutzer
- **Nächster Schritt:** `/`
- **Scores:** Download 4 / Lead 0
- **Aktualität / Sensitivität:** `U1_STABLE` / hoch
- **Begründung:** Nur die Webversion bleibt maßgeblich und fortlaufend aktualisierbar.

### 26. `/404` – Seite nicht gefunden

- **Datei:** `404.html`
- **Seitentyp / Nutzerphase:** `ERROR` / `ERROR_RECOVERY`
- **Primäres Problem:** Der Nutzer muss aus einem Fehlpfad sicher zurückgeführt werden.
- **Nutzeraufgabe:** Zur Startseite oder einem Kernwerkzeug zurückkehren.
- **Bestehende Funktion:** 404-Rückführung.
- **Entscheidung:** `NONE`
- **Kandidat:** kein Kandidat
- **Zusatznutzen:** Kein Dokumentbedarf.
- **Zielgruppe:** Nutzer ungültiger URLs
- **Nächster Schritt:** `/`
- **Scores:** Download 2 / Lead 0
- **Aktualität / Sensitivität:** `U1_STABLE` / niedrig
- **Begründung:** Fehlerseiten dürfen keine Download- oder Lead-Sackgasse erzeugen.

## 7. Konsolidiertes Kandidatenregister

| ID | Arbeitstitel | Klasse | Auslieferung | Download | Lead | Update | Umfang | Komplexität | Priorität | Status |
|---|---|---|---|---:|---:|---|---|---|---|---|
| C01 | Italien-Neustart: Budget- und Sicherheitsarbeitsblatt | B | `FREE_DIRECT` | 89 | 79 | U2_MOVING | 8–12 | mittel | P1 | `RECOMMENDED_WAVE_1` |
| C02 | Napoli und Süditalien: Standort- und Kostenvergleich | B | `FREE_DIRECT` | 58 | 57 | U2_MOVING | 8–12 | mittel | P3 | `RECOMMENDED_LATER` |
| C03 | Online-Einkommen: Nachweis- und Stabilitätsplan | C | `LEAD_LATER` | 82 | 83 | U2_MOVING | 10–14 | hoch | P1 | `RECOMMENDED_WAVE_1` |
| C04 | DACH-Italien: Tragfähigkeits- und Stressplan | B | `LEAD_LATER` | 76 | 79 | U3_SENSITIVE | 8–12 | hoch | P2 | `RECOMMENDED_LATER` |
| C05 | Partita IVA: Vorbereitungs- und Unterlagenliste | E | `FREE_DIRECT` | 76 | 56 | U3_SENSITIVE | 6–10 | mittel | P1 | `RECOMMENDED_WAVE_1` |
| C06 | Regime forfettario: Fragen- und Klärungsbogen | E | `FREE_DIRECT` | 50 | 51 | U3_SENSITIVE | 6–10 | hoch | P2 | `RECOMMENDED_LATER` |
| C07 | Resto al Sud 2.0: Projekt- und Antragsvorbereitung | C | `LEAD_LATER` | 71 | 65 | U4_EVENT_DRIVEN | 12–18 | sehr hoch | P2 | `RECOMMENDED_LATER` |
| C08 | ItalienRadar: dynamische Ergebnisprotokoll-Familie | D | `DYNAMIC_LATER` | 79 | 82 | U3_SENSITIVE | 2–6 je Ergebnis | sehr hoch | P3 | `DYNAMIC_DEPENDENCY` |

### C01 – Italien-Neustart: Budget- und Sicherheitsarbeitsblatt

- **Dokumentklasse:** `B`
- **Hauptfunktion:** Budgetplanung
- **Nebenfunktion:** Risikoanalyse
- **Primäre Route:** `/was-kostet-ein-neustart-in-italien`
- **Sekundäre Routen:** `/mit-1000-euro-in-italien-leben`, `/italien-neustart-ohne-job`, `/italien-kostenrechner`
- **Zugeordnetes Tool:** `/italien-kostenrechner`
- **Zielgruppe:** Menschen, die Kosten, Startpuffer und Risikomonate für einen Italien-Neustart belastbar planen müssen.
- **Problem:** Kosten werden oft als Monatswert betrachtet, ohne Startkosten, Rücklagen, Stressmonat und Abbruchreserve zusammenzuführen.
- **Eigenständiger Zusatznutzen:** Der Nutzer trägt eigene Werte ein, vergleicht Normal-, Stress- und Mindestfall und dokumentiert eine belastbare Mindestreserve.
- **Auslieferung:** `FREE_DIRECT`
- **Download-Value-Score:** **89**
  - A 5, B 5, C 5, D 5, E 5, F 5, G 1, H 2, I 1
- **Lead-Suitability-Score:** **79**
  - A 5, B 5, C 4, D 5, E 4, F 4, G 2, H 1
- **Aktualitätsklasse / Sensitivität:** `U2_MOVING` / mittel
- **Geschätzter Umfang / Komplexität:** 8–12 / mittel
- **Benötigte Quellen:** bestehende Kostenartikel, Istat/amtliche Preisquellen nur bei konkreten Orientierungswerten
- **Pflichtmodule:** Monatsbudget, Startkosten, Rücklagenreichweite, Stressmonat, Abbruchreserve, Entscheidungszone
- **Nächster Schritt:** `/italien-kostenrechner`
- **Priorität / Status:** `P1` / `RECOMMENDED_WAVE_1`

### C02 – Napoli und Süditalien: Standort- und Kostenvergleich

- **Dokumentklasse:** `B`
- **Hauptfunktion:** Vergleichsblatt
- **Nebenfunktion:** Umzugsplanung
- **Primäre Route:** `/leben-in-neapel-kosten`
- **Sekundäre Routen:** `/napoli-neustart`, `/sueditalien-guenstig-leben`, `/italien-kostenrechner`
- **Zugeordnetes Tool:** `/italien-kostenrechner`
- **Zielgruppe:** Nutzer, die Napoli oder einen süditalienischen Ort nicht nur nach Miete, sondern nach Alltagstauglichkeit vergleichen wollen.
- **Problem:** Standortentscheidungen werden häufig auf Mietpreise reduziert und blenden Mobilität, Gesundheit, Arbeit, Sprache und Infrastruktur aus.
- **Eigenständiger Zusatznutzen:** Ein einheitliches Raster erlaubt den Vergleich mehrerer Orte mit eigenen Gewichtungen, Ausschlusskriterien und offenen Recherchepunkten.
- **Auslieferung:** `FREE_DIRECT`
- **Download-Value-Score:** **58**
  - A 4, B 4, C 4, D 4, E 3, F 5, G 2, H 4, I 2
- **Lead-Suitability-Score:** **57**
  - A 4, B 4, C 3, D 4, E 3, F 2, G 2, H 1
- **Aktualitätsklasse / Sensitivität:** `U2_MOVING` / mittel
- **Geschätzter Umfang / Komplexität:** 8–12 / mittel
- **Benötigte Quellen:** Istat/kommunale Quellen bei Zahlen, keine pauschalen Stadtteilurteile
- **Pflichtmodule:** Ortsvergleich, Wohnkostenrahmen, Mobilität, Gesundheit, Arbeit/Internet, Sprache, Risikofaktoren
- **Nächster Schritt:** `/napoli-neustart`
- **Priorität / Status:** `P3` / `RECOMMENDED_LATER`

### C03 – Online-Einkommen: Nachweis- und Stabilitätsplan

- **Dokumentklasse:** `C`
- **Hauptfunktion:** Nachweisplan
- **Nebenfunktion:** Schritt-für-Schritt-Plan
- **Primäre Route:** `/online-einkommen-in-italien-aufbauen`
- **Sekundäre Routen:** `/online-geld-in-italien`, `/online-einkommen-realitaetscheck`, `/italien-neustart-ohne-job`
- **Zugeordnetes Tool:** `/online-einkommen-realitaetscheck`
- **Zielgruppe:** Menschen mit geplanter oder erster Online-Einnahme, die vor einem Umzug belastbare Belege und Stabilität aufbauen müssen.
- **Problem:** Idee, Umsatz, wiederholbares Einkommen und umzugsfähige Stabilität werden miteinander verwechselt.
- **Eigenständiger Zusatznutzen:** Der Nutzer dokumentiert Angebot, Nachfragebelege, Kundenmix, Zahlungseingänge, Rücklagen und Mindestprüfung über mehrere Monate.
- **Auslieferung:** `LEAD_LATER`
- **Download-Value-Score:** **82**
  - A 5, B 5, C 5, D 5, E 5, F 4, G 1, H 3, I 2
- **Lead-Suitability-Score:** **83**
  - A 5, B 5, C 5, D 5, E 4, F 3, G 1, H 2
- **Aktualitätsklasse / Sensitivität:** `U2_MOVING` / mittel
- **Geschätzter Umfang / Komplexität:** 10–14 / hoch
- **Benötigte Quellen:** keine Einkommensversprechen, bestehende Plattformlogik und Nachweisregeln
- **Pflichtmodule:** Angebotsnachweis, Nachfragebelege, Kundenmix, Einnahmenhistorie, Rücklagen, Mindestprüfung, Plan B
- **Nächster Schritt:** `/online-einkommen-realitaetscheck`
- **Priorität / Status:** `P1` / `RECOMMENDED_WAVE_1`

### C04 – DACH-Italien: Tragfähigkeits- und Stressplan

- **Dokumentklasse:** `B`
- **Hauptfunktion:** Arbeitsblatt
- **Nebenfunktion:** Risikoanalyse
- **Primäre Route:** `/dach-einnahmen-italien-kostenstruktur`
- **Sekundäre Routen:** `/dach-italien-hebel-rechner`, `/italien-kostenrechner`, `/online-einkommen-in-italien-aufbauen`
- **Zugeordnetes Tool:** `/dach-italien-hebel-rechner`
- **Zielgruppe:** Remote-Beschäftigte, Freelancer und Selbstständige mit DACH-Einnahmen und geplantem Lebensmittelpunkt in Italien.
- **Problem:** Bruttoeinnahmen werden ohne Steuer-, Beitrags-, Geschäfts-, Reise- und Kundenrisiken gegen italienische Lebenshaltung gerechnet.
- **Eigenständiger Zusatznutzen:** Das Dokument trennt Einnahmen, Abgaben, Geschäftskosten und Lebenshaltung und führt einen Stressmonat sowie Klumpenrisiko-Nachweis.
- **Auslieferung:** `LEAD_LATER`
- **Download-Value-Score:** **76**
  - A 5, B 5, C 5, D 4, E 5, F 4, G 2, H 3, I 2
- **Lead-Suitability-Score:** **79**
  - A 5, B 5, C 4, D 5, E 4, F 3, G 1, H 2
- **Aktualitätsklasse / Sensitivität:** `U3_SENSITIVE` / hoch
- **Geschätzter Umfang / Komplexität:** 8–12 / hoch
- **Benötigte Quellen:** aktuelle Steuer-/Sozialversicherungsabgrenzung nur als Prüfhinweis, keine Individualberatung
- **Pflichtmodule:** Netto-Brücke, Geschäftskosten, Reise/Arbeitsfähigkeit, Klumpenrisiko, Stressmonat, Rücklagen
- **Nächster Schritt:** `/dach-italien-hebel-rechner`
- **Priorität / Status:** `P2` / `RECOMMENDED_LATER`

### C05 – Partita IVA: Vorbereitungs- und Unterlagenliste

- **Dokumentklasse:** `E`
- **Hauptfunktion:** Unterlagenliste
- **Nebenfunktion:** Fragenkatalog
- **Primäre Route:** `/partita-iva-deutsche-italien`
- **Sekundäre Routen:** `/partita-iva`, `/partita-iva-vorpruefung`
- **Zugeordnetes Tool:** `/partita-iva-vorpruefung`
- **Zielgruppe:** Deutsche und andere deutschsprachige Nutzer, die eine selbstständige Tätigkeit in Italien fachlich vorbereitet prüfen lassen wollen.
- **Problem:** Nutzer suchen vorschnell nach Eröffnung oder Steuervorteilen, bevor Tätigkeit, Status, Unterlagen und Fragen geklärt sind.
- **Eigenständiger Zusatznutzen:** Die Liste sammelt Sachverhalt, Tätigkeit, Wohnsitz, Kunden, Umsatzannahmen, Unterlagen und Fragen für Commercialista/Behörden.
- **Auslieferung:** `FREE_DIRECT`
- **Download-Value-Score:** **76**
  - A 5, B 5, C 5, D 4, E 5, F 5, G 1, H 4, I 3
- **Lead-Suitability-Score:** **56**
  - A 5, B 5, C 4, D 4, E 4, F 2, G 4, H 3
- **Aktualitätsklasse / Sensitivität:** `U3_SENSITIVE` / hoch
- **Geschätzter Umfang / Komplexität:** 6–10 / mittel
- **Benötigte Quellen:** Agenzia delle Entrate, INPS, sichtbarer Aktualitätsstand
- **Pflichtmodule:** Sachverhalt, Tätigkeit, Wohnsitz/Status, Kunden/Umsatz, Unterlagen, Fragen an Fachstelle, Quellen
- **Nächster Schritt:** `/partita-iva-vorpruefung`
- **Priorität / Status:** `P1` / `RECOMMENDED_WAVE_1`

### C06 – Regime forfettario: Fragen- und Klärungsbogen

- **Dokumentklasse:** `E`
- **Hauptfunktion:** Fragenkatalog
- **Nebenfunktion:** Entscheidungsmatrix
- **Primäre Route:** `/regime-forfettario-italien-deutsche`
- **Sekundäre Routen:** `/forfettario-realitaetscheck`, `/partita-iva-deutsche-italien`
- **Zugeordnetes Tool:** `/forfettario-realitaetscheck`
- **Zielgruppe:** Nutzer, die das Forfettario nicht nur nach Steuersatz, sondern nach Ausschlüssen, Beiträgen und Liquidität prüfen müssen.
- **Problem:** Ein niedriger nomineller Steuersatz wird mit einem insgesamt passenden und liquiditätsschonenden Modell verwechselt.
- **Eigenständiger Zusatznutzen:** Der Bogen strukturiert offene Fachfragen, Ausschlussrisiken, INPS-Themen und Rechenannahmen für eine professionelle Prüfung.
- **Auslieferung:** `FREE_DIRECT`
- **Download-Value-Score:** **50**
  - A 4, B 4, C 4, D 3, E 5, F 4, G 2, H 5, I 4
- **Lead-Suitability-Score:** **51**
  - A 4, B 5, C 4, D 4, E 4, F 1, G 3, H 4
- **Aktualitätsklasse / Sensitivität:** `U3_SENSITIVE` / hoch
- **Geschätzter Umfang / Komplexität:** 6–10 / hoch
- **Benötigte Quellen:** Agenzia delle Entrate, INPS, jährliche/vierteljährliche Regelprüfung
- **Pflichtmodule:** Voraussetzungen, Ausschlüsse, Koeffizient, Beiträge, Liquidität, Fachfragen, Quellen
- **Nächster Schritt:** `/forfettario-realitaetscheck`
- **Priorität / Status:** `P2` / `RECOMMENDED_LATER`

### C07 – Resto al Sud 2.0: Projekt- und Antragsvorbereitung

- **Dokumentklasse:** `C`
- **Hauptfunktion:** Projektvorbereitung
- **Nebenfunktion:** Unterlagenliste
- **Primäre Route:** `/resto-al-sud-2-deutsche-italien`
- **Sekundäre Routen:** `/resto-al-sud-check`, `/resto-al-sud-2-vorpruefung`, `/partita-iva-vorpruefung`
- **Zugeordnetes Tool:** `/resto-al-sud-2-vorpruefung`
- **Zielgruppe:** Gründungsinteressierte mit Süditalien-Fokus, die ein Projekt vor einer offiziellen Invitalia-Prüfung strukturieren müssen.
- **Problem:** Förderinteresse wird mit Förderfähigkeit, Antragsreife und Liquiditätsfähigkeit verwechselt.
- **Eigenständiger Zusatznutzen:** Das Dokument verbindet Projektbeschreibung, Zielgruppe, Kostenplan, Eigenmittel, Liquidität, Unterlagen und offene Invitalia-Prüfpunkte.
- **Auslieferung:** `LEAD_LATER`
- **Download-Value-Score:** **71**
  - A 5, B 5, C 5, D 4, E 5, F 5, G 1, H 5, I 4
- **Lead-Suitability-Score:** **65**
  - A 5, B 5, C 5, D 5, E 5, F 1, G 3, H 4
- **Aktualitätsklasse / Sensitivität:** `U4_EVENT_DRIVEN` / sehr hoch
- **Geschätzter Umfang / Komplexität:** 12–18 / sehr hoch
- **Benötigte Quellen:** Invitalia, Normativa, Antragsfenster und aktuelle Programmdetails
- **Pflichtmodule:** Projektkern, Zielgruppe/Region, förderfähige Vorhaben, Kostenplan, Liquidität, Unterlagen, Prüfpfad
- **Nächster Schritt:** `/resto-al-sud-2-vorpruefung`
- **Priorität / Status:** `P2` / `RECOMMENDED_LATER`

### C08 – ItalienRadar: dynamische Ergebnisprotokoll-Familie

- **Dokumentklasse:** `D`
- **Hauptfunktion:** Ergebnisprotokoll
- **Nebenfunktion:** Nächste-Schritte-Plan
- **Primäre Route:** `/italien-kostenrechner`, `/online-einkommen-realitaetscheck`, `/dach-italien-hebel-rechner`, `/partita-iva-vorpruefung`, `/forfettario-realitaetscheck`, `/resto-al-sud-2-vorpruefung`
- **Sekundäre Routen:** `/italien-tools`
- **Zugeordnetes Tool:** `MULTI_TOOL`
- **Zielgruppe:** Nutzer der sechs interaktiven Rechner und Vorprüfungen, die Ergebnisse speichern, ausdrucken oder später erneut prüfen wollen.
- **Problem:** Toolergebnisse sind flüchtig und werden ohne strukturierte Speicherung oder Datumsstand schwer vergleichbar.
- **Eigenständiger Zusatznutzen:** Eine generierte Auswertung hält Eingaben, Ergebniszone, Warnungen, offene Nachweise, Quellenstand und nächste Schritte fest.
- **Auslieferung:** `DYNAMIC_LATER`
- **Download-Value-Score:** **79**
  - A 5, B 5, C 5, D 5, E 5, F 5, G 1, H 4, I 3
- **Lead-Suitability-Score:** **82**
  - A 5, B 5, C 5, D 5, E 5, F 3, G 1, H 3
- **Aktualitätsklasse / Sensitivität:** `U3_SENSITIVE` / hoch
- **Geschätzter Umfang / Komplexität:** 2–6 je Ergebnis / sehr hoch
- **Benötigte Quellen:** jeweilige Toollogik, Datenschutzprüfung, keine personenbezogene Speicherung ohne Rechtsgrundlage
- **Pflichtmodule:** Eingaben, Ergebniszone, Warnungen, offene Punkte, nächste Schritte, Quellenstand, Zeitstempel
- **Nächster Schritt:** `/italien-tools`
- **Priorität / Status:** `P3` / `DYNAMIC_DEPENDENCY`

## 8. Verworfene, zurückgestellte und zusammengeführte Ideen

| ID | Idee | Entscheidung | Ziel | Grund | Neubewertung |
|---|---|---|---|---|---|
| R01 | 1.000-Euro-Realitätscheck als eigenes PDF | `MERGED` | C01 | Der Nutzer benötigt keine zweite Budgetlogik. Der Minimalbudget- und Stressfall wird als klar abgegrenztes Modul in C01 integriert. | Nur neu bewerten, wenn ein eigenständiges interaktives Minimalbudget-Produkt entsteht. |
| R02 | Neustart-ohne-Job-Sicherheitsplan als eigenständiges Dokument | `MERGED` | C01, C03 | Finanzpuffer und Abbruchreserve gehören in C01; Einkommensaufbau und Nachweise in C03. Ein drittes Dokument würde beide Systeme duplizieren. | Nur als späteres Bundle oder Nutzerreise, nicht als neues Kern-PDF. |
| R03 | Süditalien-Kostenvergleich als eigenes PDF | `MERGED` | C02 | Der Vergleichsbedarf ist identisch mit dem Napoli-/Standortraster und wird in C02 ortsneutral abgebildet. | Bei belastbarer eigener Datengrundlage könnte später eine datenbasierte Webansicht entstehen. |
| R04 | Napoli-Stadtteilplan mit konkreten Empfehlungen | `HOLD` | C02 | Konkrete Stadtteilbewertungen, Mietangaben und Sicherheitsurteile sind beweglich und bergen Immobilien-/Standortberatungsnähe. C02 bleibt bei prüfbaren Vergleichsfaktoren. | Erst mit belastbarer Quellen-, Daten- und Aktualisierungsroutine. |
| R05 | Italien-Neustart-Gesamtcheck als großes Sammel-PDF | `REJECTED` | — | Ein universelles Sammeldokument wäre zu breit, veraltet schnell und schwächt die klare modulare Nutzerreise. | Später höchstens als dynamische Web-Roadmap oder kurzes Download-Verzeichnis. |
| R06 | Statische Kopien aller Toolfragen als PDF | `REJECTED` | C08 | Statische Fragekopien bieten kaum Mehrwert. Der sinnvolle spätere Weg ist ein Ergebnisprotokoll aus den tatsächlichen Eingaben. | Nicht als statische PDFs; nur C08 weiterverfolgen. |

## 9. Free-, Lead- und Dynamic-Verteilung

### 9.1 Statische Kandidaten

- **Direkt frei:** C01, C02, C05, C06
- **Späterer Lead-Magnet:** C03, C04, C07
- **Dynamische Ergebnisfamilie:** C08

### 9.2 Schutzregeln

- Offizielle Quellen, Pflichtwarnungen und Basisinformationen bleiben immer frei.
- `LEAD_LATER` ist eine Architekturklassifizierung, keine sofortige E-Mail-Schranke.
- Vor Phase 3.2.6 werden keine E-Mail-Adressen erhoben.
- Ein Dokument darf nicht nur deshalb gegatet werden, weil sein Lead-Score hoch ist.

## 10. Nutzerreisen und Dokumentzuordnung

### A – Allgemeiner Neustart

`/` → `/was-kostet-ein-neustart-in-italien` → `C01` → `/italien-kostenrechner`

Vom Orientierungsproblem zur dokumentierten Budget- und Sicherheitsgrenze.

### B – Kleines Budget / ohne Job

`/mit-1000-euro-in-italien-leben` → `/italien-neustart-ohne-job` → `C01` → `C03` → `/online-einkommen-realitaetscheck`

Puffer, Abbruchreserve und Einkommensnachweise werden getrennt, aber verbunden bearbeitet.

### C – Napoli / Süditalien

`/napoli-neustart` → `/leben-in-neapel-kosten` → `C02` → `/italien-kostenrechner`

Standortvergleich ohne pauschale Bestenliste.

### D – Online-Einkommen

`/online-geld-in-italien` → `/online-einkommen-in-italien-aufbauen` → `C03` → `/online-einkommen-realitaetscheck`

Von der Idee zur nachweisbaren Stabilität.

### E – DACH-Einnahmen

`/dach-einnahmen-italien-kostenstruktur` → `C04` → `/dach-italien-hebel-rechner`

Bruttoannahmen werden in Tragfähigkeit und Stressmonat übersetzt.

### F – Partita IVA

`/partita-iva` → `/partita-iva-deutsche-italien` → `C05` → `/partita-iva-vorpruefung`

Sachverhalt und Unterlagen werden vor der Fachprüfung strukturiert.

### G – Forfettario

`/regime-forfettario-italien-deutsche` → `C06` → `/forfettario-realitaetscheck`

Steuersatz, Beiträge und Ausschlüsse werden als offene Fachfragen geordnet.

### H – Förderung

`/resto-al-sud-check` → `/resto-al-sud-2-deutsche-italien` → `C07` → `/resto-al-sud-2-vorpruefung`

Projektarbeit vor Förderhoffnung.

## 11. Aktualitäts- und Risikoklassen

| Klasse | Bedeutung | Mindestprüfung | Kandidaten |
|---|---|---|---|
| U1_STABLE | stabile Grundlagen | jährlich | keine Kernkandidaten |
| U2_MOVING | Kosten, Marktwerte oder bewegliche Orientierungswerte | halbjährlich | C01, C02, C03 |
| U3_SENSITIVE | Steuer, Sozialversicherung oder strukturabhängige Regeln | mindestens vierteljährlich | C04, C05, C06, C08 |
| U4_EVENT_DRIVEN | Förderprogramme, Fristen und Antragswege | vor Veröffentlichung und bei relevanter Änderung | C07 |

## 12. Empfohlene erste Produktionswelle

### 1. C01 – Italien-Neustart: Budget- und Sicherheitsarbeitsblatt

- **Warum zuerst:** Der Nutzer trägt eigene Werte ein, vergleicht Normal-, Stress- und Mindestfall und dokumentiert eine belastbare Mindestreserve.
- **Einstiegsseiten:** `/was-kostet-ein-neustart-in-italien`, `/mit-1000-euro-in-italien-leben`, `/italien-neustart-ohne-job`, `/italien-kostenrechner`
- **Dokumentklasse / Umfang:** `B` / 8–12
- **Auslieferung:** `FREE_DIRECT`
- **Risiko:** mittel; Pflegeklasse `U2_MOVING`
- **Notwendige Quellen:** bestehende Kostenartikel, Istat/amtliche Preisquellen nur bei konkreten Orientierungswerten
- **Nächster Nutzerschritt:** `/italien-kostenrechner`

### 2. C03 – Online-Einkommen: Nachweis- und Stabilitätsplan

- **Warum zuerst:** Der Nutzer dokumentiert Angebot, Nachfragebelege, Kundenmix, Zahlungseingänge, Rücklagen und Mindestprüfung über mehrere Monate.
- **Einstiegsseiten:** `/online-einkommen-in-italien-aufbauen`, `/online-geld-in-italien`, `/online-einkommen-realitaetscheck`, `/italien-neustart-ohne-job`
- **Dokumentklasse / Umfang:** `C` / 10–14
- **Auslieferung:** `LEAD_LATER`
- **Risiko:** mittel; Pflegeklasse `U2_MOVING`
- **Notwendige Quellen:** keine Einkommensversprechen, bestehende Plattformlogik und Nachweisregeln
- **Nächster Nutzerschritt:** `/online-einkommen-realitaetscheck`

### 3. C05 – Partita IVA: Vorbereitungs- und Unterlagenliste

- **Warum zuerst:** Die Liste sammelt Sachverhalt, Tätigkeit, Wohnsitz, Kunden, Umsatzannahmen, Unterlagen und Fragen für Commercialista/Behörden.
- **Einstiegsseiten:** `/partita-iva-deutsche-italien`, `/partita-iva`, `/partita-iva-vorpruefung`
- **Dokumentklasse / Umfang:** `E` / 6–10
- **Auslieferung:** `FREE_DIRECT`
- **Risiko:** hoch; Pflegeklasse `U3_SENSITIVE`
- **Notwendige Quellen:** Agenzia delle Entrate, INPS, sichtbarer Aktualitätsstand
- **Nächster Nutzerschritt:** `/partita-iva-vorpruefung`

### 12.1 Gesamtbegründung der Welle

C01 testet Tabellen, Rechenfelder, Szenarien und Drucknutzung. C03 testet einen mehrstufigen Arbeitsprozess und die spätere Lead-Qualität. C05 testet Checklisten, Quellenstand, sensible Disclaimer und Unterlagenorganisation. Damit deckt die erste Welle drei unterschiedliche Dokumentarchitekturen ab, ohne direkt das komplexeste Förder- oder Dynamiksystem zu bauen.

## 13. Offene und bereits fixierte Architekturentscheidungen

| ID | Entscheidung | Status | Festlegung |
|---|---|---|---|
| AD-01 | Keine E-Mail-Erfassung vor Phase 3.2.6 | `FIXED` | LEAD_LATER beschreibt die spätere Eignung. Bis zur rechtlichen und technischen Lead-Architektur werden keine Adressen erhoben. |
| AD-02 | Offizielle Quellen und Basiswarnungen bleiben frei | `FIXED` | Quellen, Ausschlussgründe, zentrale Risiken und notwendige Pflichtinformationen werden nie ausschließlich im Lead-Dokument bereitgestellt. |
| AD-03 | C08 ist kein Bestandteil der ersten PDF-Produktion | `FIXED` | Dynamische Ergebnisprotokolle benötigen eine gesonderte technische, datenschutzrechtliche und testbare Exportarchitektur. |
| AD-04 | C02 enthält keine pauschalen Stadtteil- oder Sicherheitsrankings | `FIXED` | Das Dokument nutzt Vergleichsfaktoren, eigene Gewichtung und Quellenfelder statt vermeintlich objektiver Bestenlisten. |
| AD-05 | C05 und C06 geben keine individuelle steuerliche Antwort | `FIXED` | Beide Dokumente organisieren Sachverhalt, Unterlagen, Fragen und Quellen; die fachliche Entscheidung bleibt bei offiziellen Stellen oder qualifizierten Beratern. |
| AD-06 | Initiale Veröffentlichung von C03 | `OPEN_FOR_3.2.5/3.2.6` | C03 wird in Welle 1 produziert. Ob es bis zur Lead-Integration temporär direkt, nur intern oder erst später öffentlich angeboten wird, wird vor Integration entschieden. |

## 14. Abschluss- und PASS/FAIL-Matrix

| Prüfkriterium | Ergebnis |
|---|---|
| Baseline eindeutig dokumentiert | **PASS** |
| 26 Seiten vollständig inventarisiert | **PASS** |
| 25 Sitemap-Routen plus /404 abgegrenzt | **PASS** |
| Jede Seite besitzt eine begründete Entscheidung | **PASS** |
| Sieben statische Kandidaten konsolidiert | **PASS** |
| Eine dynamische Ergebnisfamilie getrennt | **PASS** |
| Free-/Lead-/Dynamic-Trennung vorhanden | **PASS** |
| Score-Formeln mathematisch konsistent | **PASS** |
| Sensible Kandidaten mit Pflegeklasse versehen | **PASS** |
| Verworfene und zusammengeführte Ideen dokumentiert | **PASS** |
| Exakt drei Welle-1-Kandidaten empfohlen | **PASS** |
| Keine Produktionsänderung vorgesehen | **PASS** |
| E-Mail-Erfassung vor Phase 3.2.6 ausgeschlossen | **PASS** |

## Projektleitungsentscheidung

Die Architektur ist in sich konsistent und kann als belastbare Grundlage für Phase 3.2.1.2 verwendet werden. Vor einer Implementierung bleiben alle Kandidaten Entwürfe. Es werden noch keine PDFs, Downloadseiten oder Lead-Formulare veröffentlicht.

**Phase 3.2.1.1 – Analyse und Bedarfsmatrix: fachlich freigabefähiger Entwurf.**