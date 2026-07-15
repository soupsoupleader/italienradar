# IMR Komponentenbibliothek M01–M12

Phase 3.2.2.2.3 baut auf Baseline `64c5f07c0b531c9d23266b2a9a061c678842d5c8` und dem abgeschlossenen Designsystem 1.0.0 auf. Die Bibliothek ist in Integrationshärtung 1.1.0 für `P2_HTML_PRINT`, `C01`–`C07` und lokale Source Sans 3 Assets vorgesehen; `C08` bleibt ausgeschlossen.

Die Härtung entfernt das missbrauchte `SPACE_XS` als Zeichenabstand, führt sichere `data-bind-text`-, `data-bind-href`-, `data-repeat`- und `data-repeat-item`-Marker ein und legt deterministisches ID-Namespacing für jede Komponenteninstanz fest. Im Produktionskontext verwendet M01 H2; die einzige H1 gehört zum Cover des Mastertemplates.

## Umfang und Grenzen

Die Bibliothek enthält genau die normativen Komponenten `M01_INTRODUCTION` bis `M12_METADATA`. Jede Quelle besitzt eine eindeutige `data-component-id`, Version `1.1.0`, neutrale Fallbacktexte und funktioniert ohne JavaScript. Das Manifest dokumentiert alle Binding-Slots, Wiederholungsgruppen, Link-Slots und Heading-Grenzen. Ein Produkt-Build muss IDs deterministisch namespacen.

Nicht enthalten sind C01-Inhalt, Produktprofile, Mastertemplate, öffentliche PDFs, Websiteänderungen, Formulare, AcroForm/XFA, Lead-Erfassung und Deployment. Es werden keine neue Schriftfamilie, Farbrolle, Typografierolle, Abstandsklasse, Modulnummer, Produktklasse, Risikoklasse oder Aktualitätsklasse eingeführt.

## Semantik und Verträge

| ID | Semantik | Eingaben/Varianten | Umbruch und Accessibility |
|---|---|---|---|
| M01 | `section`, Überschrift, Absätze | Ziel, Nutzung, Grenze, Test-ID | Überschrift mit erstem Absatz; keine Erfolgsgarantie |
| M02 | `section`, `h2`, `ol`, `li` | Voraussetzungen, geordnete Schritte | Schritt zusammenhalten, echte Liste |
| M03 | `fieldset`, `legend`, Label, statische Fläche | Feld, Einheit, Hinweis | `aria-readonly`, sichtbare Zuordnung; keine PDF-Form |
| M04 | `table`, Caption, Kopf, Körper, Summe | Spalten, Zeilen, Totals | `scope`, Kopf wiederholen, Zeilen nicht teilen |
| M05 | `fieldset`, `legend`, `ul`, `li` | Aufgaben und Statuswerte | Status sichtbar, Kontrollfeld dekorativ, Eintrag zusammen |
| M06 | `aside`, Überschrift, Text | neutrale Erläuterung | Textlabel und Kontrast, Block teilbar nach Inhalt |
| M07 | `aside`, Überschrift, Text | Risiko, Bedeutung, Prüfschritt | Label, Kontrast, Block zusammen; keine Angstkommunikation |
| M08 | `aside`, Überschrift, Text | Blockade, Folgehandlung | sichtbarer BLOCKER, Block zusammen; nur echte Blockade |
| M09 | `section`, `h2`, `dl` | Eingaben, Status, Begründung, offene Punkte | Ergebniszone zusammen; keine Entscheidung aus Selbstauskunft |
| M10 | `section`, `h2`, `ol`, beschreibender Link | priorisierte Folgehandlung | erste Priorität klar, kein CTA-Druck oder Tracking |
| M11 | `section`, `h2`, `ul` | Herausgeber, Titel/Funktion, Stand, Datum, Abschnitt | Quelle nicht entkoppeln; beschreibender Linktext |
| M12 | `footer`, `h2`, `dl` | ID, Version, Klassen, Quellen-/Buildstand | maschinen- und menschenlesbar; keine privaten Builddaten |

## CSS-Vertrag

`components.css` referenziert ausschließlich freigegebene `--imr-*`-Variablen aus `design-tokens.css`. Es definiert nur semantische `.imr-component--*`-Klassen sowie neutrale Strukturwerte. Es enthält keine `@font-face`-Regel, keine neue Farbe oder Schriftgröße, keinen externen Load, kein `@import`, keine Websiteklasse, keine Produktregel, kein JavaScript und kein `position: fixed`. Umbruchschutz gilt nur für Einheiten, Zeilen und kurze Statusblöcke; lange Module werden nicht pauschal blockiert.

## Sicherheits- und Accessibility-Grenzen

Alle sichtbaren Statuswerte haben Textlabels und bleiben in Graustufe sowie Schwarzweiß verständlich. Die Eingabefläche ist statisch, ohne Formularversand, AcroForm, XFA oder gespeicherte Werte. Links verwenden beschreibenden Text; der neutrale Quellenbeleg darf eine HTTPS-Testreferenz enthalten, die nicht als Buildressource geladen wird. Keine PDF/A- oder PDF/UA-Konformität wird behauptet.

## Lokaler Katalog und QA-Matrix

Der neutrale Katalog liegt ausschließlich unter `.tmp/phase-3-2-2-2-3/component-proof/` und ist kein Mastertemplate. Er verwendet T00-Testwerte, enthält alle M01–M12, eine mehrseitige Tabelle, eine lange Checkliste, Statusblöcke, Schreibfläche, Quellen, Metadaten und einen internen Fragment-Link. Er wird aus derselben unveränderten HTML/CSS-Quelle zweimal mit `P2_HTML_PRINT` erzeugt.

| QA-Familie | Erwartung |
|---|---|
| HTML/A11Y | IDs, Überschriften, Listen, Tabellenköpfe, ARIA-Ziele und interne Links validiert |
| CSS | Tokenparität, keine Fremdfarben/-fonts/-größen, keine externen Ressourcen |
| PDF-Struktur | A4, Text, Tags, Sprache `de-DE`, Titel, Listen/Tabelle/Link |
| Sicherheit | keine Verschlüsselung, Aktionen, Anhänge, Formulare oder Pfade |
| Render | Farbe, Graustufe und Schwarzweiß; keine Überläufe oder unlesbaren Mindestgrößen |
| Komponenten | M01–M12 je `PASS` oder begründet `NOT_APPLICABLE`; kein `FAIL` |

Zeitstempelbedingte PDF-Bytes dürfen abweichen; Seitenzahl, Geometrie, extrahierter Text, Überschriften, Tabellen, Links, Struktur und Sicherheitsmerkmale müssen übereinstimmen.

## Status und nächste Phase

Status: `COMPONENT_LIBRARY_QA_PASSED`

Die Komponentenbibliothek M01–M12 und ihre kanonischen Quelldateien haben die lokale technische, semantische und visuelle Abnahme bestanden. Die Integrationshärtung 1.1.0 ist für die sichere Datenbindung vorbereitet. Der neutrale Katalog, PDFs, Renderbilder und QA-Berichte bleiben unversionierte Prüfnachweise. Es wurde kein Mastertemplate, kein Produkt, kein öffentliches PDF und kein Deployment erzeugt.

Offene Punkte für 3.2.2.2.4 sind das neutrale Mastertemplate, Produktdatenbindung, kontrollierte Rendererauflösung und ein reproduzierbares Buildskript. Erst danach darf Produktinhalt entstehen.
