# Phase 3.2.2.1 – P2-Final-QA und Pipelineentscheidung

Stand: 15.07.2026
Baseline: `d2a69bfa916c2a2dc25c862694ecf4c54d9bffcf`

## Entscheidung

**SELECTED: P2_HTML_PRINT**

P2 erfüllt die Entscheidungsregel: P0 = 0, P1 = 0, A4, Rendering, Text/Sonderzeichen, Sicherheitsprüfung und funktionale Reproduzierbarkeit bestanden. Wave-1-Produkte sind mit der geprüften HTML-/CSS-Komponentenstruktur realistisch umsetzbar.

P1 ist nicht auswählbar. Die allgemeine Klasse `P1_DOCUMENT` wird nicht global verworfen.

## P2-Final-QA

Zwei getrennte Chrome-PDFs wurden aus derselben unveränderten HTML-/CSS-Quelle erzeugt. Beide haben zwei A4-Seiten, identische Strukturmetriken, identische Inhalte und identische Renderabmessungen. Die SHA-256-Werte unterscheiden sich; die PDFs haben aber dieselbe Länge und nur zwei abweichende Bytes in den Zeitstempeln (`CreationDate`/`ModDate`). Das ist ein zulässiger nicht-fachlicher Metadatenunterschied.

Technisch bestanden: PDF ohne Reparaturwarnung geöffnet, A4 Hochformat, MediaBox/CropBox konsistent, Text extrahierbar, Sonderzeichen `Ä Ö Ü ä ö ü ß €` korrekt, nicht verschlüsselt, keine JavaScript-/Launch-/OpenAction-/Additional-Action-Strukturen, keine EmbeddedFiles/Anhänge/privaten Builddaten oder versteckten Endpunkte. Schriften sind als eingebettete Subsets vorhanden; fehlende oder ersetzte Glyphen wurden nicht festgestellt.

Die PDFs enthalten `StructTreeRoot`, `MarkInfo`, `de-DE`, einen Titel, H1/H2/H3 sowie `Table/TR/TH/TD`-Tags. Link-Tags sind nicht vorhanden, da die neutrale Quelle keine Links enthält. Praktische Lesereihenfolge ist nutzbar. Es wird ausdrücklich keine PDF/UA- oder PDF/A-Konformität behauptet.

Die Farb-, Graustufen- und Schwarz-Weiß-Prüfung bestanden: Warnung und Blocker sind zusätzlich durch Beschriftung und Linienführung unterscheidbar; keine Information hängt ausschließlich von Farbe ab.

## P1-Vergleich

`P1_DOCUMENT_WORD` bleibt `ENVIRONMENT_BLOCKED`: strukturierte DOCX-Erzeugung und OpenXML-Vorprüfung bestanden, Word-COM-Öffnen bestanden, `SaveAs2` und `ExportAsFixedFormat` liefen in einen Timeout; es wurde kein P1-PDF erzeugt. Weitere Word-Diagnose ist nicht erforderlich.

## Schutz der Nutzeränderung und Abschluss

`datenschutz.html` wurde nicht gelesen oder geändert. Start-Hash: `22FA400E95D4762C799679992A9E865181797AA5C29654A781D30EDD402BDFDA`; der End-Hash ist identisch. Es wurde nichts gestaged, zurückgesetzt, gestasht, committed, gepusht oder deployed.

Die Prototypen, Quellen, Reports und Renderbilder bleiben unversioniert. Die kanonischen Ergebnisdateien sind diese Markdown-Datei und `phase-3-2-2-1-pipelinevergleich.json`.
