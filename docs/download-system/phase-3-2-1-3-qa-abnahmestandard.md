# ItalienRadar / IMR - Phase 3.2.1.3.4 Verbindlicher QA-, Prüf- und Abnahmestandard

## Geltungsbereich und Status

- Phase: `3.2.1.3.4`
- Status: `QA_ACCEPTANCE_STANDARD_DRAFT`
- Technische Baseline: `7053a42dfaa956174a89f5d3244ac27c674da060`
- Vollständig betroffen: statische Produkte `C01` bis `C07`
- Nur als zukünftiges QA-Profil betroffen: `C08`
- Nicht Bestandteil: PDF-, Template- oder DOCX-Erzeugung, Buildsystem, Prüfskripte, Website- oder Formularänderungen, aktive C08-Datenverarbeitung, Commit, Push oder Deployment

Dieser Standard überführt Inhalts-, Design-, Accessibility- und PDF-Technikregeln in einen einheitlichen Freigabeprozess. Er ändert keine Produktklasse, Nutzeraufgabe, Zielgruppe, Inhaltsgrenze, Risiko- oder Aktualitätsklasse, Pipeline- oder Datenschutzentscheidung.

## Normative Sprache und Prüfergebnisse

| Begriff | Bedeutung |
|---|---|
| MUSS | Verbindliche Anforderung. Eine Abweichung führt zu `FAIL`. |
| DARF NICHT | Verbindliches Verbot. Ein Verstoß führt zu `FAIL`. |
| SOLL | Starke Empfehlung. Eine Abweichung benötigt eine Begründung. |
| KANN | Optionale Möglichkeit ohne Abnahmepflicht. |

| Ergebnis | Bedeutung |
|---|---|
| `PASS` | Anforderung vollständig erfüllt |
| `FAIL` | Anforderung nicht erfüllt |
| `NOT_APPLICABLE` | sachlich nicht anwendbar und begründet |
| `BLOCKED` | wegen fehlender Voraussetzung nicht prüfbar |
| `WAIVED` | bekannte Abweichung wurde formal befristet genehmigt |
| `NOT_TESTED` | Prüfung nicht ausgeführt; für Pflichtprüfungen keine Freigabe zulässig |

`NOT_TESTED` DARF NIE als `PASS` behandelt werden. `WAIVED` ist nur im Rahmen der Waiver-Regel zulässig.

## Gates und Reifegrade

| Gate | Zielstatus | Zweck | Mindestvoraussetzungen |
|---|---|---|---|
| `G1_ARCHITECTURE_APPROVED` | `ARCHITECTURE_APPROVED` | Produktvertrag freigeben | Produkt-ID, Primärklasse, Zielgruppe, Hauptaufgabe, Inhaltsgrenzen, Aktualitäts- und Risikoklasse sowie Auslieferungsmodell vorhanden |
| `G2_DESIGN_READY` | `DESIGN_READY` | Inhalts- und Designkonzept freigeben | vollständige Anatomie, klassenspezifischer Arbeitsbereich, Quellen, Disclaimer, Warnungen, Statuslogik und keine Vertragsabweichung |
| `G3_READY_TO_PUBLISH` | `READY_TO_PUBLISH` | erzeugte PDF freigeben | Inhalt, Design, Accessibility, PDF-Technik, Sicherheit, Links, Quellenstand, Version, Rendering und Druck bestanden |
| `G4_PUBLISHED` | `PUBLISHED` | Betrieb freigeben | richtige Datei unter richtiger URL, korrekter MIME-Type, Prüfsumme, sichtbare Version, keine parallele Altversion und aktive Aktualitätsüberwachung |

`C01` bis `C07` haben G1 grundsätzlich bestanden. In dieser Phase werden Gates nur definiert und nicht an einem Produkt oder einer PDF ausgeführt. `C08` DARF NICHT über diese statischen Gates freigegeben werden, bevor sein eigenes Daten-, Datenschutz-, Ergebnis- und Generierungsprofil existiert.

## Prüfarten und Testfamilien

Jeder Testfall MUSS genau eine primäre Prüfart erhalten.

| Prüfart | Einsatz |
|---|---|
| `AUTOMATED` | reproduzierbare Struktur-, Dateiname-, Metadaten-, Seitenformat-, Linksyntax-, Sicherheits- oder Integritätsprüfung |
| `MANUAL` | fachliche und semantische Prüfung von Inhalt, Grenzen, Warnungen, Quellen und Beratungssicherheit |
| `VISUAL` | Prüfung gerenderter Seiten auf Hierarchie, Überläufe, Graustufen, Tabellen, Felder, Umbrüche und Druckbarkeit |
| `ASSISTIVE_TECH_REVIEW` | Prüfung von Lesereihenfolge, Tags, Überschriften, Tabellen, Linktexten, Formularlabels und Tab-Reihenfolge |
| `CROSS_SOURCE` | Vergleich von Produktvertrag, Quelle, PDF, Release, Prüfsumme oder Vorgängerversion |

Kontrollierte Testfamilien sind `QA-ARCH`, `QA-CONTENT`, `QA-BOUNDARY`, `QA-SOURCE`, `QA-DESIGN`, `QA-TYPOGRAPHY`, `QA-COLOR`, `QA-TABLE`, `QA-FORM`, `QA-A11Y`, `QA-PDF`, `QA-METADATA`, `QA-LINK`, `QA-SECURITY`, `QA-PRIVACY`, `QA-RENDER`, `QA-PRINT`, `QA-MOBILE`, `QA-VERSION`, `QA-RELEASE` und `QA-REGRESSION`.

Test-IDs haben das Muster `QA-<FAMILIE>-<NNN>`, etwa `QA-SECURITY-001`. Eine ID DARF NICHT für eine andere Bedeutung wiederverwendet werden.

## Verbindliches Testfallschema und Nachweise

Jeder Testfall MUSS die folgenden Felder enthalten:

`test_id`, `title`, `test_family`, `applicable_products`, `applicable_classes`, `applicable_gate`, `test_type`, `severity_on_failure`, `requirement`, `procedure`, `expected_result`, `evidence_required`, `result`, `reviewer`, `review_date`, `waiver_allowed`.

Zulässige Nachweisarten sind `SOURCE_REVIEW`, `RENDERED_PAGE_SET`, `TOOL_OUTPUT`, `METADATA_EXPORT`, `LINK_REPORT`, `ACCESSIBILITY_REPORT`, `PDF_STRUCTURE_REPORT`, `PRINT_OUTPUT`, `HASH_RECORD`, `RELEASE_RECORD`, `WAIVER_RECORD` und `CROSS_SOURCE_COMPARISON`.

## Kanonisches Testinventar

Die produktive Testinventur umfasst ausschließlich die 24 Tabellenzeilen im Abschnitt „Pflicht-Testfälle“. Ein im Gespräch oder in einer Arbeitsanweisung genanntes Beispiel ist kein produktiver Testfall, solange es nicht als Zeile in dieser Tabelle definiert ist. Die frühere Angabe von 25 war ein Zählfehler und ist nicht Teil des verbindlichen Inventars.

| Kennzahl | Kanonischer Wert |
|---|---:|
| `test_cases_total` | 24 |
| `mandatory_test_cases` | 24 |
| `optional_test_cases` | 0 |
| `example_test_cases` | 0 |
| `unique_test_ids` | 24 |
| `duplicate_test_ids` | 0 |
| `undefined_test_references` | 0 |

Es gilt verbindlich: `test_cases_total = mandatory_test_cases + optional_test_cases`, `unique_test_ids = test_cases_total`, `duplicate_test_ids = 0` und `undefined_test_references = 0`. Künftige Beispieltests MÜSSEN entweder ohne produktive `QA-*`-ID bleiben oder ausdrücklich `EXAMPLE_ONLY` tragen und dürfen nicht in `test_cases_total` eingehen.

## Fehlerklassen und Freigabematrix

| Klasse | Beispiele | Waiver | Wirkung |
|---|---|---|---|
| `P0_BLOCKER` | Datei nicht öffnungsfähig, falsches Produkt, sensible Daten, Schadcode, ausführbare Aktion, zentrale Seiten fehlen, Datenschutzverletzung | nie | keine Freigabe |
| `P1_CRITICAL` | falsche Kernaussage oder Berechnung, abgeschnittener Hauptinhalt, unlesbare Schrift, falsche Version, zentraler Link defekt, fehlender sensibler Disclaimer, unbrauchbare Kern-A11y | grundsätzlich nie | keine Freigabe |
| `P2_MAJOR` | fehlende Metadaten, fehlerhafte Lesezeichen, einzelne Tabellenstruktur, Druckproblem, unvollständige Quelle, deutliche Designabweichung | formal, befristet | grundsätzlich vor Release beheben |
| `P3_MINOR` | kleine Abstandsabweichung, geringe optische Inkonsistenz, nicht kritische Metadaten- oder Kompressionsverbesserung | formal, befristet | dokumentiert nachlagerbar |

| Gate | Verbindliche Freigabeanforderung |
|---|---|
| `G2_DESIGN_READY` | `P0 = 0`, `P1 = 0`, `P2 = 0`, alle Pflichtprüfungen `PASS`, kein Pflichtfall `NOT_TESTED` oder `BLOCKED` |
| `G3_READY_TO_PUBLISH` | `P0 = 0`, `P1 = 0`, `P2 = 0` oder gültiger Waiver, P3 vollständig dokumentiert, alle G3-Pflichttests ausgeführt, Rendering, Sicherheit und Quellenstand bestanden |
| `G4_PUBLISHED` | G3 erfüllt sowie richtige Release-Datei, Prüfsumme, URL, MIME-Type und sichtbare Version; keine aktiv beworbene Altversion |

## Pflicht-Testfälle

| Test-ID | Gate | Art | Schwere | Anforderung und erwartetes Ergebnis | Nachweis | Waiver |
|---|---|---|---|---|---|---|
| `QA-ARCH-001` | G1 | `CROSS_SOURCE` | `P1_CRITICAL` | Produktvertrag enthält Klasse, Zielgruppe, Hauptaufgabe, Grenzen, Risiko, Aktualität und Auslieferung. | `CROSS_SOURCE_COMPARISON` | nein |
| `QA-CONTENT-001` | G2 | `MANUAL` | `P1_CRITICAL` | Genau eine kanonische Hauptaufgabe; keine zweite gleichwertige Arbeitsstrecke und keine bloße Artikelkopie. | `SOURCE_REVIEW` | nein |
| `QA-CONTENT-002` | G2 | `MANUAL` | `P1_CRITICAL` | Zehnteilige Anatomie, Bearbeitungsreihenfolge, Ergebnis und nächster Schritt sind vorhanden. | `SOURCE_REVIEW` | nein |
| `QA-BOUNDARY-001` | G2 | `CROSS_SOURCE` | `P1_CRITICAL` | Erlaubte Inhalte und Inhaltsgrenzen entsprechen dem Produktvertrag. | `CROSS_SOURCE_COMPARISON` | nein |
| `QA-CONTENT-003` | G2 | `MANUAL` | `P1_CRITICAL` | Keine individuelle Rechts-, Steuer-, Sozialversicherungs- oder Finanzberatung, Förderzusage, Behördenentscheidung, Einkommens- oder Umzugsgarantie. | `SOURCE_REVIEW` | nein |
| `QA-SOURCE-001` | G2/G3 | `MANUAL` | `P1_CRITICAL` | Sensible Aussagen sind klassifiziert, belegt und haben Abschnitts-, Abruf- oder Prüfdatum. | `SOURCE_REVIEW` | nein |
| `QA-SOURCE-002` | G2/G3 | `CROSS_SOURCE` | `P1_CRITICAL` | U2 höchstens 6 Monate, U3 höchstens 3 Monate, U4 vor jeder Veröffentlichung und bei Ereignisänderung geprüft. | `CROSS_SOURCE_COMPARISON` | nein |
| `QA-DESIGN-001` | G3 | `VISUAL` | `P1_CRITICAL` | DIN A4 Hochformat, Sicherheitszone, kein Überlauf, einspaltiges Grundraster und klare Eingabe-/Ergebnis-Trennung. | `RENDERED_PAGE_SET` | nein |
| `QA-TYPOGRAPHY-001` | G3 | `VISUAL` | `P1_CRITICAL` | Fließtext mindestens 10,5 pt, Tabellen mindestens 9 pt, Quellen 8,5 pt, Fußzeile 8 pt; Umlaute und ß korrekt. | `RENDERED_PAGE_SET` | nein |
| `QA-COLOR-001` | G3 | `VISUAL` | `P2_MAJOR` | Farbe, Graustufen und Schwarz-Weiß bleiben verständlich; keine Information nur über Farbe. | `RENDERED_PAGE_SET` | ja |
| `QA-TABLE-001` | G3 | `ASSISTIVE_TECH_REVIEW` | `P2_MAJOR` | Tabellen haben Titel, Einheiten, Kopfzeilen, `Table/TR/TH/TD`, logische Lesereihenfolge und Wiederholung auf Folgeseiten. | `ACCESSIBILITY_REPORT` | ja |
| `QA-FORM-001` | G3 | `ASSISTIVE_TECH_REVIEW` | `P1_CRITICAL` | Falls anwendbar: AcroForm, sichtbare Labels, eindeutige Feldnamen, Tab-Reihenfolge, Speichern und erneutes Öffnen. | `PDF_STRUCTURE_REPORT` | nein |
| `QA-A11Y-001` | G3 | `ASSISTIVE_TECH_REVIEW` | `P1_CRITICAL` | Titel, `de-DE`, Tags, Struktur, Lesereihenfolge, Linkbezeichnungen und funktionale Alternativtexte sind praktisch nutzbar. | `ACCESSIBILITY_REPORT` | nein |
| `QA-PDF-001` | G3 | `AUTOMATED` | `P0_BLOCKER` | PDF öffnet ohne Reparaturwarnung; Version, MediaBox, CropBox, Seitenzahl und A4-Geometrie sind zulässig. | `PDF_STRUCTURE_REPORT` | nein |
| `QA-METADATA-001` | G3 | `AUTOMATED` | `P2_MAJOR` | Title, Author ItalienRadar, Subject, Keywords, `de-DE`, Produkt-ID, Version, Daten und Quellenstand sind korrekt. | `METADATA_EXPORT` | ja |
| `QA-LINK-001` | G3 | `AUTOMATED` | `P1_CRITICAL` | Links sind beschreibend, HTTPS, nicht lokal, nicht `javascript:`, nicht `file:`, nicht verkürzt und zentrale Ziele erreichbar. | `LINK_REPORT` | nein |
| `QA-SECURITY-001` | G3 | `AUTOMATED` | `P0_BLOCKER` | Keine JavaScript-, Launch- oder ausführbare Open-Action, keine automatischen Netzwerkaufrufe, Anhänge, unsichtbaren Links oder versteckten Felder. | `PDF_STRUCTURE_REPORT` | nein |
| `QA-SECURITY-002` | G3 | `AUTOMATED` | `P0_BLOCKER` | Keine API-Schlüssel, lokalen Pfade, privaten Metadaten, Kommentare, eingebetteten Quellen oder Testdaten. | `METADATA_EXPORT` | nein |
| `QA-PRIVACY-001` | G3 | `AUTOMATED` | `P0_BLOCKER` | Keine automatische Übertragung, Telemetrie, Tracking, versteckten Endpunkte oder vorausgefüllten persönlichen Daten. | `PDF_STRUCTURE_REPORT` | nein |
| `QA-RENDER-001` | G3 | `VISUAL` | `P1_CRITICAL` | Jede Seite ist gerendert und gesichtet; kein Schnitt, keine Überlappung, leere Seite, schwarze Kästchen oder fehlende Felder. | `RENDERED_PAGE_SET` | nein |
| `QA-PRINT-001` | G3 | `VISUAL` | `P2_MAJOR` | 100-Prozent-, An-Seite-anpassen-, Graustufen-, Schwarz-Weiß- und Duplexdruck sind nutzbar. | `PRINT_OUTPUT` | ja |
| `QA-MOBILE-001` | G3 | `VISUAL` | `P2_MAJOR` | Desktop, Browser- und mobiler PDF-Viewer zeigen Zoom, Links, Kapitel und Tabellen nutzbar. | `RENDERED_PAGE_SET` | ja |
| `QA-VERSION-001` | G3/G4 | `CROSS_SOURCE` | `P1_CRITICAL` | Dateiname, sichtbare Version, Metadaten, Quellversion, Build-ID und SHA-256 stimmen überein. | `HASH_RECORD` | nein |
| `QA-RELEASE-001` | G4 | `AUTOMATED` | `P0_BLOCKER` | Richtige Datei an richtiger URL, korrekter MIME-Type, Download und Prüfsumme; keine aktive Altversion. | `RELEASE_RECORD` | nein |
| `QA-REGRESSION-001` | G3 | `CROSS_SOURCE` | `P2_MAJOR` | Ab `v1.1` dokumentiert der Vergleich `INTENDED_CHANGE`, `UNINTENDED_CHANGE` oder `UNCHANGED`; unerklärte großflächige Änderung blockiert. | `CROSS_SOURCE_COMPARISON` | ja |

## Produktprofile C01-C08

| Produkt | Zusätzliche Pflichtprüfung |
|---|---|
| `C01` | Budgetformeln, Startkosten, Rücklagen, Normal-/Stress-/Mindestfall, Einheiten und Zeiträume |
| `C02` | keine objektive Sicherheitswertung oder allgemeingültige Rangliste; persönliche Kriterien und Fakten getrennt |
| `C03` | Phasen, Nachweisstatus, Kundenabhängigkeit und keine Umsatz- oder Erfolgsgarantie |
| `C04` | Geschäfts- und Privatkosten getrennt; keine C01-/C03-Duplikation und keine individuelle Steuerberechnung |
| `C05` | ATECO/INPS nur als Klärungsfragen, keine individuelle Einstufung, U3-Quellenstand gültig |
| `C06` | keine endgültige Forfettario-Zuordnung oder individuelle Steuerberechnung; Ausschluss- und Beitragsfragen sichtbar |
| `C07` | aktuelle Invitalia-Primärquelle, keine Förderzusage, U4-Prüfung vor Veröffentlichung, Fristen und Bedingungen aktuell |
| `C08` | nur zukünftiges Profil: Datenmodell-, Ergebnislogik- und Mapping-Version, Datenschutz, Speicher-/Löschkonzept, Missbrauchsschutz und nicht personenbezogene Kennung; keine Testausführung in dieser Phase |

## Reviewer- und Freigaberollen

Kontrollierte Rollen sind `AUTHOR`, `CONTENT_REVIEWER`, `DESIGN_REVIEWER`, `TECHNICAL_REVIEWER`, `ACCESSIBILITY_REVIEWER` und `RELEASE_APPROVER`.

Eine Person DARF NICHT gleichzeitig allein Autor, Prüfer aller Bereiche und finaler Release-Freigeber sein. Vor Veröffentlichung MUSS mindestens ein zweiter, unabhängiger Prüfschritt erfolgen. Der Autor KANN eigene Fehler beheben. C05, C06 und C07 benötigen gesonderte Inhaltsprüfung; Sicherheits-P0-Tests müssen technisch nachvollziehbar sein. Der Release-Freigeber MUSS das vollständige Abnahmeprotokoll einsehen.

## Waiver, Abnahmeprotokoll und Rückzug

Ein Waiver ist ausschließlich für `P2_MAJOR` oder `P3_MINOR` zulässig. Er MUSS `waiver_id`, `test_id`, `product_id`, `severity`, `deviation`, `reason`, `risk`, `compensating_control`, `approver`, `approval_date`, `expiry_date` und `follow_up_issue` enthalten. Ohne Ablaufdatum ist er ungültig. P0, P1, Datenschutzverletzungen, Schadcode, falsche Berechnungen, falsche Produkte und fehlende zentrale Seiten sind niemals waiverfähig.

Das Abnahmeprotokoll MUSS mindestens `product_id`, `document_version`, `build_id`, `source_commit`, `release_filename`, `sha256`, `test_plan_version`, `test_date`, `reviewers`, `tests_total`, `tests_passed`, `tests_failed`, `tests_blocked`, `tests_not_tested`, `waivers`, `p0_count`, `p1_count`, `p2_count`, `p3_count`, `gate_result` und `release_decision` enthalten. Zulässige Entscheidungen sind `APPROVED`, `REJECTED`, `REWORK_REQUIRED` und `APPROVED_WITH_WAIVER`; die letzte ist bei P0 oder P1 nicht zulässig.

Ein veröffentlichtes Dokument MUSS zurückgezogen oder deaktiviert werden bei entdecktetem P0, wesentlicher P1-Falschaussage, aufgehobener offizieller Grundlage, geänderter U4-Bedingung, sensiblen personenbezogenen Daten, falscher Auslieferung oder nicht passender Prüfsumme. Der Status wird `UPDATE_REQUIRED` oder bei schwerem Risiko `ARCHIVED`. Die Altdatei DARF NICHT weiter aktiv beworben werden.

## Anforderungsinventar und Traceability-Matrix

Jede verbindliche `MUSS`- oder `DARF NICHT`-Regel der Ausgangsstandards MUSS einer abgeleiteten Requirement-ID und mindestens einem produktiven QA-Test zugeordnet sein. Eine Requirement-ID fasst nur unmittelbar zusammengehörige Teilregeln zusammen, wenn das zugeordnete Verfahren alle Teilregeln prüft. Eine nicht abgedeckte verbindliche Regel ist ein `FAIL` dieser Phase.

Zulässige `coverage_status`-Werte sind `COVERED`, `NOT_APPLICABLE` und `UNMAPPED`. Für diese Phase gilt: `UNMAPPED = 0`, MUSS ohne Test = 0, DARF-NICHT ohne Test = 0, Verweise auf unbekannte Tests = 0 und Tests mit unbekannter Requirement-ID = 0.

Eine Requirement-Zeile kann sowohl eine MUSS- als auch eine DARF-NICHT-Teilregel zusammenfassen, wenn derselbe Test beide Teilregeln prüft. Deshalb sind `must_requirements` und `must_not_requirements` Herkunftszählungen und nicht additiv zu `normative_requirements_total`.

| requirement_id | source_file | source_section | normative_strength | requirement_summary | qa_test_ids | applicable_products | applicable_gate | coverage_status |
|---|---|---|---|---|---|---|---|---|
| `REQ-CONTENT-001` | Inhaltsstandard | Qualitätsdimensionen | MUSS | Konkrete Nutzeraufgabe, Verständlichkeit, Beratungssicherheit und Handlungsfähigkeit. | `QA-CONTENT-001`, `QA-CONTENT-003` | C01-C07 | G2 | COVERED |
| `REQ-CONTENT-002` | Inhaltsstandard | Hauptaufgaben und Arbeitsnutzen | MUSS/DARF NICHT | Genau eine kanonische Hauptaufgabe, keine zweite Arbeitsstrecke und keine Artikelkopie. | `QA-CONTENT-001` | C01-C07 | G2 | COVERED |
| `REQ-CONTENT-003` | Inhaltsstandard | Sachlichkeit und Sprache | MUSS/DARF NICHT | Sachliche deutsche Texte, erklärter Fachbegriff, keine Zusage, Garantie oder individuelle Beratung. | `QA-CONTENT-003`, `QA-TYPOGRAPHY-001` | C01-C07 | G2/G3 | COVERED |
| `REQ-CONTENT-004` | Inhaltsstandard | Mindestanatomie | MUSS | Alle zehn Dokumentfunktionen, inklusive Status, Quellen, Disclaimer und nächstem Schritt. | `QA-CONTENT-002` | C01-C07 | G2 | COVERED |
| `REQ-CONTENT-005` | Inhaltsstandard | Klassenspezifische Regeln | MUSS/DARF NICHT | Klasse B, C und E erfüllen ihren Arbeitsbereich und überschreiten keine Klassen- oder Beratungsgrenze. | `QA-CONTENT-002`, `QA-BOUNDARY-001` | C01-C07 | G2 | COVERED |
| `REQ-CONTENT-006` | Inhaltsstandard | Statuswerte und Warnsignale | MUSS/DARF NICHT | Kontrollierte Statuswerte, kein Garantie-Status; jede Warnung enthält Risiko, Bedeutung und nächsten Schritt. | `QA-CONTENT-002`, `QA-CONTENT-003` | C01-C07 | G2 | COVERED |
| `REQ-PORTFOLIO-C01-001` | Portfolio JSON | C01 Vertrag und Inhaltsgrenze | DARF NICHT | Keine Steuerberechnung, Standortbewertung oder Förderprüfung; Budget- und Szenariologik bleibt C01-spezifisch. | `QA-BOUNDARY-001` | C01 | G2 | COVERED |
| `REQ-PORTFOLIO-C02-001` | Portfolio JSON | C02 Vertrag und Inhaltsgrenze | DARF NICHT | Keine objektive Sicherheitswertung, Stadtteilempfehlung oder individuelle Sicherheitsberatung. | `QA-BOUNDARY-001` | C02 | G2 | COVERED |
| `REQ-PORTFOLIO-C03-001` | Portfolio JSON | C03 Vertrag und Inhaltsgrenze | DARF NICHT | Kein Businessplan, Verkaufsleitfaden, Umsatzversprechen oder Steuerdokument. | `QA-BOUNDARY-001`, `QA-CONTENT-003` | C03 | G2 | COVERED |
| `REQ-PORTFOLIO-C04-001` | Portfolio JSON | C04 Vertrag und Inhaltsgrenze | DARF NICHT | Keine C01-/C03-Duplikation und keine individuelle Steuer- oder Beitragsberechnung. | `QA-BOUNDARY-001` | C04 | G2 | COVERED |
| `REQ-PORTFOLIO-C05-001` | Portfolio JSON | C05 Vertrag und Inhaltsgrenze | DARF NICHT | Keine individuelle ATECO-/INPS-Beratung, Steuerberatung oder Eröffnungsempfehlung. | `QA-BOUNDARY-001`, `QA-CONTENT-003` | C05 | G2 | COVERED |
| `REQ-PORTFOLIO-C06-001` | Portfolio JSON | C06 Vertrag und Inhaltsgrenze | DARF NICHT | Keine individuelle Steuerberechnung oder endgültige Regime-Zuordnung. | `QA-BOUNDARY-001`, `QA-CONTENT-003` | C06 | G2 | COVERED |
| `REQ-PORTFOLIO-C07-001` | Portfolio JSON | C07 Vertrag und Inhaltsgrenze | MUSS/DARF NICHT | Aktuelle Invitalia-Primärquelle und keine Förderzusage. | `QA-SOURCE-001`, `QA-SOURCE-002`, `QA-BOUNDARY-001` | C07 | G2/G3 | COVERED |
| `REQ-PORTFOLIO-C08-001` | Portfolio JSON | C08 Architekturgrenze | DARF NICHT | Keine statische Freigabe, Speicherung oder Generierung ohne gesondertes Konzept. | `QA-ARCH-001` | C08 | G1 | COVERED |
| `REQ-SOURCE-001` | Inhaltsstandard | Quellenregeln | MUSS | Sensible Aussagen sind klassifiziert, mit Quellenstand, Bezug und Datum versehen. | `QA-SOURCE-001` | C01-C07 | G2/G3 | COVERED |
| `REQ-SOURCE-002` | Inhaltsstandard | Aktualitätsregeln | MUSS/DARF NICHT | U2/U3/U4-Prüffristen, Änderungsprotokoll und `UPDATE_REQUIRED` bei Überfälligkeit. | `QA-SOURCE-002`, `QA-RELEASE-001` | C01-C07 | G2/G3/G4 | COVERED |
| `REQ-DESIGN-001` | Designstandard | Markenwirkung und Raster | MUSS/DARF NICHT | Funktionale, nicht werbliche Gestaltung, A4-Hochformat, Sicherheitszone und einspaltiges Grundraster. | `QA-DESIGN-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-002` | Designstandard | Abstand und Hierarchie | MUSS/DARF NICHT | Kontrollierte Abstände und mindestens zwei Unterscheidungsmerkmale je Hierarchieebene, nie nur Farbe. | `QA-DESIGN-001`, `QA-COLOR-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-003` | Designstandard | Typografie | MUSS/DARF NICHT | Mindestgrößen, lesbarer Zeilenfluss, keine dekorative Schrift oder unzulässige Textauszeichnung. | `QA-TYPOGRAPHY-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-004` | Designstandard | Farbe und Kontrast | MUSS/DARF NICHT | Semantische Farbrollen, Text/Symbol zusätzlich zur Farbe, Kontrast sowie Grau- und Schwarz-Weiß-Lesbarkeit. | `QA-COLOR-001`, `QA-PRINT-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-005` | Designstandard | Cover, Kopf- und Fußzeile | MUSS/DARF NICHT | Covermetadaten, korrekte Kopf-/Fußzeile, Produkt-ID, Version, Seitenzahl und Sensitivitätsstand. | `QA-DESIGN-001`, `QA-RENDER-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-006` | Designstandard | Module, Tabellen und Felder | MUSS/DARF NICHT | Funktionsklare Module, Tabellen, Kontrollkästchen und Eingabefelder mit sichtbaren Bezeichnungen und Umbruchregeln. | `QA-TABLE-001`, `QA-FORM-001`, `QA-RENDER-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-007` | Designstandard | Ergebnis, Quellen und Umbrüche | MUSS/DARF NICHT | Ergebnis- und Quellenbereiche trennen; kein Ampelergebnis allein, keine unlesbaren Quellen und keine getrennten Kontextpaare. | `QA-DESIGN-001`, `QA-RENDER-001` | C01-C07 | G3 | COVERED |
| `REQ-DESIGN-008` | Designstandard | Druck, Bildschirm und Icons | MUSS/DARF NICHT | Farb-, Grau-, Schwarz-Weiß-, Duplex- und Bildschirmnutzung; funktionale Bilder/Icons mit Textbedeutung. | `QA-PRINT-001`, `QA-MOBILE-001`, `QA-COLOR-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-001` | PDF-Technikstandard | Produktionsprinzip und Pipeline | MUSS/DARF NICHT | Versionierte, reproduzierbare Quelle; keine ausschließlich manuelle PDF-Bearbeitung und keine ungeeignete Pipeline. | `QA-VERSION-001`, `QA-PDF-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-002` | PDF-Technikstandard | PDF-Format und Geometrie | MUSS/DARF NICHT | Valide A4-PDF, konsistente MediaBox/CropBox und keine unzulässigen Seitenboxen oder Druckmarken. | `QA-PDF-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-003` | PDF-Technikstandard | Metadaten, Dateiname und Version | MUSS/DARF NICHT | Vollständige öffentliche/interne Metadaten, sichere Dateinamen und konsistente Major-/Minor-Version. | `QA-METADATA-001`, `QA-VERSION-001` | C01-C07 | G3/G4 | COVERED |
| `REQ-TECH-004` | PDF-Technikstandard | Schriften, Text und Bilder | MUSS/DARF NICHT | Lizenzierte/eingebettete Schriften, echter Unicode-Text, lesbare Glyphen, optimierte Bilder ohne externe oder private Metadaten. | `QA-TYPOGRAPHY-001`, `QA-A11Y-001`, `QA-RENDER-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-005` | PDF-Technikstandard | Navigation und Links | MUSS/DARF NICHT | Korrekte Lesezeichen und Links, HTTPS, keine lokalen, verkürzten, Tracking- oder ausführbaren Links. | `QA-LINK-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-006` | PDF-Technikstandard | Aktionssicherheit und versteckte Daten | DARF NICHT | Kein JavaScript, Launch/Open-Action, Anhang, Netzwerkaufruf, unsichtbarer Link, Testwert, Kommentar oder interne Daten. | `QA-SECURITY-001`, `QA-SECURITY-002` | C01-C07 | G3 | COVERED |
| `REQ-TECH-007` | PDF-Technikstandard | Accessibility und Tabellen | MUSS/DARF NICHT | Sprache, Titel, Tags, Lesereihenfolge, Linktext, Alternativtext sowie logische Tabellenstruktur. | `QA-A11Y-001`, `QA-TABLE-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-008` | PDF-Technikstandard | Formulare und Datenschutz | MUSS/DARF NICHT | AcroForm-orientierte Felder, keine JavaScript-Abhängigkeit, keine Übertragung, Telemetrie, Tracking oder ungenehmigte Speicherung. | `QA-FORM-001`, `QA-PRIVACY-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-009` | PDF-Technikstandard | C08 Daten- und Sicherheitsgrenze | DARF NICHT | Keine C08-Speicherung, Drittübertragung, Personen-URL oder externe PDF-Dienste ohne gesonderte Freigabe. | `QA-ARCH-001` | C08 | G1 | COVERED |
| `REQ-TECH-010` | PDF-Technikstandard | Integrität und Dateitrennung | MUSS/DARF NICHT | Source/build/release/archive getrennt, Release-Hash, keine Builddatei als Veröffentlichung. | `QA-VERSION-001`, `QA-RELEASE-001` | C01-C07 | G3/G4 | COVERED |
| `REQ-TECH-011` | PDF-Technikstandard | Rendering, Regression und Reader | MUSS/DARF NICHT | Vollständiges Rendering, Fehlererkennung, begründete Regression und Reader-/Mobilprüfung. | `QA-RENDER-001`, `QA-REGRESSION-001`, `QA-MOBILE-001` | C01-C07 | G3 | COVERED |
| `REQ-TECH-012` | PDF-Technikstandard | Fehler und Release-Gate | MUSS | P0/P1 blockieren; technische, Render-, Metadaten-, Link-, Sicherheits-, Dateiname- und Versionsprüfung bestehen. | `QA-RELEASE-001`, `QA-SECURITY-001`, `QA-VERSION-001` | C01-C07 | G3/G4 | COVERED |

| Inventarwert | Kanonischer Wert |
|---|---:|
| `normative_requirements_total` | 36 |
| `must_requirements` | 27 |
| `must_not_requirements` | 32 |
| `covered_requirements` | 36 |
| `not_applicable_requirements` | 0 |
| `unmapped_requirements` | 0 |
| `unknown_qa_test_references` | 0 |
| `tests_with_unknown_requirement_id` | 0 |

## Kontrollierte Vorbereitung für spätere Maschinenlesbarkeit

Diese Phase erzeugt keine JSON-Datei. Unverändert für eine spätere `phase-3-2-1-3-standard.json` vorgesehen sind `test_result_values`, `test_types`, `test_families`, `severity_levels`, `quality_gates`, `release_decisions`, `reviewer_roles`, `waiver_schema`, `test_case_schema`, `evidence_types`, `traceability_schema` und `product_qa_profiles`.

## Abnahmekriterien für diese Teilphase

Der QA-Entwurf ist vollständig, wenn G1-G4, Prüfergebnisse, Prüfarten, Testfamilien, Testfallschema, Fehlerklassen, Freigabematrix, Inhalts-, Quellen-, Design-, Accessibility-, PDF-, Sicherheits-, Render-, Druck-, Mobile-, Link-, Metadaten-, Versions- und Regressionstests, C01-C08-Profile, Rollen, Waiver, Abnahmeprotokoll, Rückzug und Traceability abgedeckt sind.

Dieser Standard ist ein Dokumentationsartefakt. Er erzeugt keine PDF, keine Vorlage, keine Prüfskripte, keine JSON-Datei, keine Websiteänderung, keine C08-Implementierung und keine Auslieferungslogik.