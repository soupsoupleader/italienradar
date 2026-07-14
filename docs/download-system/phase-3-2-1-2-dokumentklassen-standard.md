# ItalienRadar / IMR - Phase 3.2.1.2 Dokumentklassen-Standard

## Status

- Phase: `3.2.1.2`
- Status: `ARCHITECTURE_APPROVED`
- Grundlage: Phase 3.2.1.1, Baseline `cb89827f3c6d92378e4f28672086d24a8d237a88`
- Geltung: zukünftige Download- und Ergebnisdokumente; keine Produktion, keine Lead-Erfassung und keine Produktionsdateiänderung.

## Sechs unabhängige Klassifikationsachsen

| Achse | Zweck | Kontrollierte Werte |
|---|---|---|
| Dokumentklasse | Wie das Produkt funktioniert | `A`, `B`, `C`, `D`, `E` |
| Portfolioebene | Seine strategische Rolle | `H1`, `H2`, `H3`, `H4` |
| Zugangsklasse | Wie es ausgeliefert wird | `FREE_DIRECT`, `LEAD_LATER`, `DYNAMIC_LATER` |
| Aktualitätsklasse | Wie oft geprüft wird | `U1_STABLE`, `U2_MOVING`, `U3_SENSITIVE`, `U4_EVENT_DRIVEN` |
| Risikoklasse | Wie sensibel Aussagen und Folgen sind | `R1_LOW`, `R2_MODERATE`, `R3_HIGH`, `R4_CRITICAL` |
| Produktionsstatus | Position im Lebenszyklus | siehe Lebenszyklus |

Diese Achsen sind nicht austauschbar. Ein Arbeitsblatt kann beispielsweise `H1`, `FREE_DIRECT`, `U2_MOVING`, `R2_MODERATE` und `APPROVED_WAVE_1` sein.

## Dokumentklassen

### A - Schnellcheck

- Umfang: 1 bis 3 Seiten.
- Zweck: eine einzelne Vorab-, Ausschluss- oder Statusentscheidung.
- Pflicht: eindeutige Ja/Nein- oder Statuslogik und ein Verweis auf Tool, Fachseite oder nächsten Schritt.
- Nicht zulässig: lange Erläuterungen, komplexe Planung, Steuerlogik oder personalisierte Ergebnisse.

### B - Arbeitsblatt

- Umfang: 3 bis 8 Seiten.
- Zweck: eigene Werte, Nachweise, Entscheidungen oder Vergleiche eintragen.
- Pflicht: Eingabebereiche, Bearbeitungsreihenfolge, Ergebnis- oder Auswertungsbereich, druck- und digital lesbare Struktur.
- Regel: ohne E-Mail-Sequenz und persönlichen Support verständlich.

### C - Planungsdokument

- Umfang: 8 bis 15 Seiten.
- Zweck: mehrstufigen Prozess mit Phasen, Abhängigkeiten, Zwischenentscheidungen und Abschlussstatus begleiten.
- Pflicht: Startzustand, Bearbeitungsphasen, nächste offizielle oder fachliche Schritte.
- Abgrenzung: Klasse B verarbeitet primär Werte und Einzelentscheidungen; Klasse C begleitet einen Prozess.

### D - Ergebnisdokument

- Umfang: 2 bis 8 Seiten pro Toolergebnis.
- Zweck: Eingaben, Ergebniszone, Datum, Quellenstand, Warnungen und nächste Schritte eines vorhandenen Tools sichern.
- Pflicht: Zeitstempel, Ergebnislogik, Disclaimer und datenschutzkonformes Datenkonzept.
- Einschränkung: technisch abhängig; nicht Teil einer statischen Produktionswelle.

### E - Quellen- und Nachweisdokument

- Umfang: 3 bis 10 Seiten.
- Zweck: offizielle Stellen, Unterlagen, Prüfpfade und Klärungsfragen strukturieren.
- Pflicht: Primärquellen, sichtbarer Quellenstand, Aktualisierungsdatum sowie klare Trennung von Information, Vorbereitung, offizieller Prüfung und Einzelfallberatung.
- Nicht zulässig: Rechts-, Steuer- oder Förderzusage.

## Primärklasse und Module

Jedes Produkt hat genau eine Primärklasse. Zusätzliche Funktionen sind Module und dürfen die Primärklasse nicht ersetzen.

Zulässige Module: `CHECK`, `WORKSHEET`, `PLAN`, `RESULT`, `SOURCE`, `RISK`, `DECISION`, `NEXT_STEP`.

Ein Produkt hat höchstens vier unterstützende Module. Mehr als vier Module, mehr als eine primäre Nutzerentscheidung oder unvereinbare Aktualitätsklassen lösen eine Aufteilungspflicht aus.

## Portfolioebenen

| Ebene | Rolle | Regel |
|---|---|---|
| `H1` | Kernprodukt | Breites Grundproblem, mehrere Einstiege, hohe Wiederverwendung |
| `H2` | Vertiefungsprodukt | Spezifischer Cluster nach Grundverständnis |
| `H3` | Spezialprodukt | Hohe Sensitivität, Quellenpflicht oder begrenzte Zielgruppe |
| `H4` | Dynamisches Systemprodukt | Ergebnis aus konkreten Tooldaten, eigene Technik- und Datenschutzarchitektur |

## Zugangsklassen

- `FREE_DIRECT`: ohne E-Mail direkt verfügbar. Pflicht für Grundlagen, Quellen, Warnungen und Unterlagenvorbereitung.
- `LEAD_LATER`: später grundsätzlich als Lead-Magnet geeignet, aber noch keine aktive E-Mail-Schranke. Vor Datenschutz-, Double-Opt-in- und Zustellarchitektur keine Erfassung.
- `DYNAMIC_LATER`: später aus Tool- oder Nutzerdaten generiert.
- `NONE` und `HOLD` sind Seitenentscheidungen, keine Produktzugangsklassen.

## Aktualitäts- und Risikoklassen

| Klasse | Mindestprüfung | Beispiele |
|---|---|---|
| `U1_STABLE` | jährlich | Methodik, stabile Checklisten |
| `U2_MOVING` | halbjährlich | Kosten-, Markt- und Budgetannahmen |
| `U3_SENSITIVE` | vierteljährlich | Partita IVA, Forfettario, Sozialversicherung |
| `U4_EVENT_DRIVEN` | vor Veröffentlichung und bei offizieller Änderung | Programme, Fristen, Förderbedingungen |

| Klasse | Bedeutung |
|---|---|
| `R1_LOW` | allgemeine Planung, geringe Veraltungs- oder Beratungserwartung |
| `R2_MODERATE` | Finanz-, Kosten- und Rücklagenszenarien |
| `R3_HIGH` | Steuer, Sozialversicherung, formale Selbstständigkeit, Förderung oder Beratungsnähe |
| `R4_CRITICAL` | erhebliche unmittelbare Folgen; nur nach gesonderter fachlicher Freigabe |

Aktuell ist kein Produkt `R4_CRITICAL`. C08 wird auf Familienebene konservativ als `R3_HIGH` geführt; einzelne spätere Toolprotokolle können nach eigener Prüfung niedrigere Risikostufen erhalten.

## Lebenszyklus

`DISCOVERED` -> `ARCHITECTURE_APPROVED` -> `DESIGN_READY` -> `CONTENT_IN_PROGRESS` -> `QA_REQUIRED` -> `READY_TO_PUBLISH` -> `PUBLISHED` -> `UPDATE_REQUIRED` -> `ARCHIVED`

Sonderstatus: `APPROVED_WAVE_1`, `APPROVED_LATER` und `DYNAMIC_DEPENDENCY`. Ein Produkt darf nicht unmittelbar von `DISCOVERED` zu `PUBLISHED` wechseln.

## Governance

Ein neues Produkt ist nur zulässig, wenn ein eigenständiges Nutzerproblem, ein zusätzlicher Arbeitsnutzen, genau eine Primärklasse, eine Pflegeklasse, eine verantwortbare Auslieferung und keine unnötige Überschneidung nachweisbar sind.

Zusammenführung ist Pflicht, wenn mehr als 60 Prozent der Nutzeraufgaben, Eingaben, Ergebnisentscheidung sowie Einstiegsseiten identisch sind. Aufteilung ist Pflicht bei mehr als einer primären Entscheidung, mehr als vier Modulen, vermischten allgemeinen und hochsensiblen Inhalten oder nicht gemeinsam pflegbaren Aktualitätsklassen.

Grundlagen, Primärquellen, Sicherheitswarnungen, zentrale Disclaimer, Behördeninformationen und Datenschutzinformationen dürfen nicht hinter einer E-Mail-Schranke liegen.