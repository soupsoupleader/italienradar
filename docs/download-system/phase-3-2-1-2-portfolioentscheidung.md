# ItalienRadar / IMR - Phase 3.2.1.2 Portfolioentscheidung

## Verbindliche Entscheidung

Die acht Produkte aus Phase 3.2.1.1 sind in diesem Dokument verbindlich klassifiziert. Die Primärklasse, Portfolioebene, Zugangsklasse, Aktualitätsklasse, Risikoklasse, Produktionsstatus, Inhaltsgrenzen und Wellen bilden zusammen den Produktvertrag. Es entstehen in dieser Phase keine PDFs, Formulare, Downloads, E-Mail-Erfassung oder Produktionsänderungen.

## Portfolioübersicht

| ID | Kanonischer Titel | Primärklasse | Ebene | Zugang | Aktualität | Risiko | Status | Umfang |
|---|---|---|---|---|---|---|---|---|
| C01 | Italien-Neustart: Budget- und Sicherheitsarbeitsblatt | `B` | `H1` | `FREE_DIRECT` | `U2_MOVING` | `R2_MODERATE` | `APPROVED_WAVE_1` | 8-12 Seiten |
| C02 | Napoli und Süditalien: Standort- und Kostenvergleich | `B` | `H2` | `FREE_DIRECT` | `U2_MOVING` | `R2_MODERATE` | `APPROVED_LATER` | 8-12 Seiten |
| C03 | Online-Einkommen: Nachweis- und Stabilitätsplan | `C` | `H1` | `LEAD_LATER` | `U2_MOVING` | `R2_MODERATE` | `APPROVED_WAVE_1` | 10-14 Seiten |
| C04 | DACH-Italien: Tragfähigkeits- und Stressplan | `B` | `H2` | `LEAD_LATER` | `U3_SENSITIVE` | `R2_MODERATE` | `APPROVED_LATER` | 8-12 Seiten |
| C05 | Partita IVA: Vorbereitungs- und Unterlagenliste | `E` | `H1` | `FREE_DIRECT` | `U3_SENSITIVE` | `R3_HIGH` | `APPROVED_WAVE_1` | 6-10 Seiten |
| C06 | Regime forfettario: Fragen- und Klärungsbogen | `E` | `H2` | `FREE_DIRECT` | `U3_SENSITIVE` | `R3_HIGH` | `APPROVED_LATER` | 6-10 Seiten |
| C07 | Resto al Sud 2.0: Projekt- und Antragsvorbereitung | `C` | `H3` | `LEAD_LATER` | `U4_EVENT_DRIVEN` | `R3_HIGH` | `APPROVED_LATER` | 12-18 Seiten |
| C08 | ItalienRadar Tool-Ergebnisprotokolle | `D` | `H4` | `DYNAMIC_LATER` | `U3_SENSITIVE` | `R3_HIGH` | `DYNAMIC_DEPENDENCY` | 2-6 Seiten je Ergebnis |

## Cross-Phase-Konsistenz

Phase 3.2.1.1 ist die inhaltliche Ausgangsbasis für Klasse, Zugang, Aktualität, Umfang, Einstiegsrouten, Zielgruppe, Problem und Zusatznutzen. Die Umfangsangaben dieses Dokuments behalten deshalb die dort freigegebenen Grenzen bei.

| ADR | Produkt | Feld | Vorher | Nachher | Entscheidung und Grund |
|---|---|---|---|---|---|
| ADR-3212-001 | C04 | Aktualitätsklasse | `U3_SENSITIVE` | `U3_SENSITIVE` | bestätigt: steuer-, beitrags- und geschäftskostenabhängige Annahmen erfordern mindestens vierteljährliche Prüfung |
| ADR-3212-002 | C01-C08 | Produktionsstatus | Empfehlungen aus 3.2.1.1 | Lebenszykluswerte aus 3.2.1.2 | zulässige Übersetzung in `APPROVED_WAVE_1`, `APPROVED_LATER` oder `DYNAMIC_DEPENDENCY`; keine inhaltliche Abwertung |
| ADR-3212-003 | C08 | Kanonischer Produktname | ItalienRadar: dynamische Ergebnisprotokoll-Familie | ItalienRadar Tool-Ergebnisprotokolle | präzisierter Familienname; Klasse D, dynamische Auslieferung, technische Abhängigkeit und sechs Unterprodukte bleiben unverändert |
| ADR-3212-004 | C01-C08 | Problem und Zusatznutzen | Bedarfsmatrixfelder | Produktvertragsfelder | kontrollierte Übersetzung in Nutzeraufgabe und zulässigen Inhalt; Phase 3.2.1.1 bleibt die inhaltliche Referenz |

Die Begriffe „primäre Nutzeraufgabe“ und „zulässiger Inhalt“ präzisieren die in Phase 3.2.1.1 festgehaltenen Probleme und Zusatznutzen. Sie ersetzen diese Ausgangswerte nicht.

## Produktverträge

### C01 - IMR-DL-C01

- Nutzeraufgabe und Zielgruppe: Neustartplanende dokumentieren Monatskosten, Startkosten, Mindestreserve und Stressmonate.
- Einstiege: `/italien-kostenrechner`, `/was-kostet-ein-neustart-in-italien`, `/mit-1000-euro-in-italien-leben`.
- Module: `RISK`, `DECISION`, `NEXT_STEP`.
- Zulässiger Inhalt: Monatsbudget, Startkosten, Rücklagen, Mindest-Einkommensgrenze, Stressmonat, Abgleich mit Kostenrechner.
- Inhaltsgrenze: keine Stadtteilvergleiche, Partita-IVA-Fragen, Förderlogik oder individuelle Steuerberechnung.

### C02 - IMR-DL-C02

- Nutzeraufgabe und Zielgruppe: Standortinteressierte vergleichen Orte nach Miete, Mobilität, Arbeit, Internet, Alltag, Behördenzugang und eigenen Ausschlusskriterien.
- Einstiege: `/napoli-neustart`, `/leben-in-neapel-kosten`, `/sueditalien-guenstig-leben`.
- Module: `WORKSHEET`, `DECISION`, `RISK`.
- Inhaltsgrenze: keine objektiven Sicherheitsurteile, Stadtteilempfehlungen oder individuelle Sicherheitsberatung.

### C03 - IMR-DL-C03

- Nutzeraufgabe und Zielgruppe: Personen mit Online-Einkommen dokumentieren Angebot, Kunden, Einnahmenhistorie, Rücklagen, Stressmonate und Umzugsmindestbedingungen.
- Einstiege: `/online-geld-in-italien`, `/online-einkommen-in-italien-aufbauen`, `/online-einkommen-realitaetscheck`.
- Module: `WORKSHEET`, `RISK`, `DECISION`, `NEXT_STEP`.
- Inhaltsgrenze: kein Businessplan, Umsatzversprechen, Verkaufsleitfaden, Erfolgssystem oder Steuerdokument.
- Lead-Regel: Bis Phase 3.2.6 keine E-Mail-Abgabe, Nutzererfassung oder automatische Zustellung.

### C04 - IMR-DL-C04

- Nutzeraufgabe und Zielgruppe: Nutzer mit DACH-Einnahmen prüfen reale verfügbare Mittel, Geschäfts- und Reisekosten, Kundenkonzentration und Stressmonate.
- Einstiege: `/dach-einnahmen-italien-kostenstruktur`, `/dach-italien-hebel-rechner`.
- Module: `WORKSHEET`, `RISK`, `RESULT`.
- Abgrenzung: C03 prüft Nachweis und Stabilität; C04 prüft Tragfähigkeit nach Kosten und Stressszenarien. C01 bleibt das allgemeine persönliche Budget.

### C05 - IMR-DL-C05

- Nutzeraufgabe und Zielgruppe: Selbstständigkeitsplanende strukturieren Tätigkeit, Unterlagen, Fragen und Gesprächspunkte für Fachstellen.
- Einstiege: `/partita-iva`, `/partita-iva-deutsche-italien`, `/partita-iva-vorpruefung`.
- Module: `CHECK`, `SOURCE`, `WORKSHEET`.
- Zulässiger Inhalt: Tätigkeit, Einnahmenerwartung, Kundenstruktur, Startzeitpunkt, Identitäts- und Adressunterlagen, Codice fiscale, ATECO- und INPS-Fragen, Rechnungs- und Dokumentationsfragen.
- Inhaltsgrenze: keine individuelle ATECO-, INPS-, Steuer- oder Eröffnungsempfehlung. Das Produkt bleibt frei zugänglich.

### C06 - IMR-DL-C06

- Nutzeraufgabe und Zielgruppe: Forfettario-Interessierte bereiten Ausschluss-, INPS-, Liquiditäts- und Fachfragen vor.
- Einstiege: `/regime-forfettario-italien-deutsche`, `/forfettario-realitaetscheck`.
- Module: `CHECK`, `SOURCE`, `DECISION`.
- Inhaltsgrenze: keine individuelle Steuerbetragberechnung und keine endgültige Zuordnung zu einem Steuerregime.

### C07 - IMR-DL-C07

- Nutzeraufgabe und Zielgruppe: Förderinteressierte strukturieren Projektidee, Zielgruppe, Ausgaben, Liquidität, Unterlagen und offene offizielle Prüfpunkte.
- Einstiege: `/resto-al-sud-check`, `/resto-al-sud-2-deutsche-italien`, `/resto-al-sud-2-vorpruefung`.
- Module: `SOURCE`, `WORKSHEET`, `RISK`, `NEXT_STEP`.
- Pflicht: jede Veröffentlichung gegen aktuelle Invitalia-Primärquellen, Fristen und Programmbedingungen prüfen.
- Inhaltsgrenze: keine Förderzusage; Basisinformationen, Quellen und Warnungen bleiben frei zugänglich.

### C08 - IMR-DYN-C08

- Nutzeraufgabe und Zielgruppe: Toolnutzer speichern ein konkretes Ergebnis mit Eingaben, Ergebniszone, Warnungen, Zeitstempel und nächsten Schritten.
- Einstiege: die sechs Tools `/italien-kostenrechner`, `/online-einkommen-realitaetscheck`, `/dach-italien-hebel-rechner`, `/partita-iva-vorpruefung`, `/forfettario-realitaetscheck`, `/resto-al-sud-2-vorpruefung`.
- Module: `RESULT`, `NEXT_STEP`, `RISK`.
- Unterprodukte: `C08-01` bis `C08-06`, je eines pro Tool.
- Architekturgrenze: erst nach Datenmodell, Datenschutz, Ergebnislogik, Fehlerfallbehandlung, Versionierung und PDF-Generierung. Keine personenbezogene Speicherung ohne gesondertes Konzept.

## Nutzerreise und Überschneidungen

`C01` beantwortet das persönliche Gesamtbudget; `C02` den Standortvergleich; `C03` Einkommen und Nachweise; `C04` die geschäftliche Tragfähigkeit von DACH-Einnahmen; `C05` die Partita-IVA-Vorbereitung; `C06` die Forfettario-Klärung; `C07` die Förderprojekt-Vorbereitung; `C08` ausschließlich individuelle Toolergebnisse.

Statische Produkte `C01` bis `C07` werden nie mit `C08` vermischt. C05 und C06 enthalten keine Beratung; C07 enthält keine Förderzusage. Ein neues Produkt ist nur bei eigenständiger Nutzeraufgabe und ohne mehr als 60 Prozent Aufgabenüberschneidung zulässig.

## Produktionswellen

| Welle | Produkte | Zweck |
|---|---|---|
| 1 | `C01`, `C03`, `C05` | Tabellen/Szenarien, Prozessplanung sowie Quellen- und Disclaimerqualität validieren |
| 2 | `C02`, `C04`, `C06` | thematische Vertiefung |
| 3 | `C07` | Spezialprodukt nach U4-Quellenprüfung |
| 4 | `C08-01` bis `C08-06` | separates Software- und Datenschutzvorhaben |

## Abnahme

`C01` bis `C08` sind architektonisch freigegeben. Welle 1 ist verbindlich. Veröffentlichung, Lead-Erfassung, PDF-Produktion und dynamische Generierung sind nicht Bestandteil dieser Phase.