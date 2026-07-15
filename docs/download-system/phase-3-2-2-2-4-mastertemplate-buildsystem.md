# Phase 3.2.2.2.4 – Mastertemplate und Buildsystem

Status: MASTER_TEMPLATE_BUILD_SYSTEM_QA_PASSED

Das neutrale Mastertemplate, das Eingabeschema und das lokale Buildsystem haben die technische, semantische und visuelle T00-Abnahme bestanden. Der Repositoryzustand wird durch die Git-Historie nachgewiesen. Generierte PDFs, Renderbilder, Bundles, Buildberichte und negative Testfixtures bleiben unversionierte Prüfnachweise. Es wurde kein Produkt, kein öffentliches PDF, keine Websiteänderung und kein Deployment erzeugt.

## Baseline und Abhängigkeiten

- Baseline: `301a8ccf3d0404f8e4d181acad6878a6fe32852c`
- Pipeline: `P2_HTML_PRINT`
- Komponentenbibliothek: `1.1.0`, M01–M12
- Design-Tokens: `1.0.0`, lokale Source Sans 3
- Input-Schema: `1.0.0`
- Buildsystem: `1.0.1` nach Systemhärtung

Die Dateien unter `download-system/templates/`, `content/`, `manifests/` und `scripts/` bilden den neutralen lokalen Proofpfad. Es wurde kein Produktprofil, kein öffentliches PDF und kein Deployment begonnen.

## Mastertemplate

`master-template.html` definiert `lang="de-DE"`, UTF-8, genau eine Cover-H1, Inhaltsnavigation, Dokumentgrenze, Komponentenregion und Metadatenabschluss. Die Vorlage enthält keine Produktdaten, kein JavaScript und keine Websiteabhängigkeit.

`master-template.css` definiert das A4-Hochformat, die benannte Cover-Seite, lokale Kopf-/Fußzeilen und Seitenzähler. Es gibt keine feste Seitenzahl. Die Komponenten werden ausschließlich über die freigegebene Token- und Komponenten-CSS eingebunden.

## Datenbindung und Grenzen

`document-input-schema.json` und `build_document.py` erzwingen PROOF/PRODUCTION-Trennung, T00-only im Proof, C01–C07 als zulässige Produktionsprodukte und den Ausschluss von C08. Bindungsmarker, Wiederholungsgruppen, Linkziele und lokale IDs werden geprüft bzw. deterministisch auf `<document-namespace>-<component-id>-<ordinal>-<local-id>` abgebildet.

Der Proof verwendet ausschließlich neutrale T00-Werte. Eingaben werden normalisiert; unbekannte Slots, fehlende Pflichtwerte, Roh-HTML, externe Ressourcen, `file:`-/`javascript:`-Links, Pfadwerte, doppelte IDs und ungültige Produktklassen brechen den Build mit dokumentierten P0-Fehlern ab.

## Renderer und Reproduzierbarkeit

Der Renderer wird kontrolliert aus `ITALIENRADAR_CHROME_PATH`, bekannten Windows-Installationspfaden und dem Registry/App-Paths-Resolver aufgelöst. Lokal wurde Chrome unter `C:\Program Files\Google\Chrome\Application\chrome.exe` verwendet; die Dateiversion ist `144.0.7559.110`, da `--version` in dieser Umgebung keine Ausgabe lieferte. Der Build ist offline konfiguriert und lädt keine entfernten Ressourcen.

Zwei Builds aus derselben unveränderten Eingabe erzeugten denselben Build-Identifier:
`F0211D3C081804D75CBBEB35069FB0597D2119F262D5DD9691842366B2DA24EE`.
Beide PDFs haben 10 A4-Seiten, identischen extrahierten Text, identische Geometrie, Tabelleninhalte, Links, Font-Einbettung und Sicherheitsmerkmale. Kontrollierte PDF-Metadaten wurden nachgelagert normalisiert; der Seiteninhalt wurde dabei nicht neu gerendert.

## Systemhärtung 1.0.1

Die erste Systemabnahme zeigte, dass LF- und CRLF-Worktrees unterschiedliche Quellbytes in das Bundle übernahmen. Textquellen werden deshalb vor Hashbildung und Kopie als UTF-8 ohne BOM mit LF-Zeilenenden kanonisiert; Binärquellen wie WOFF2 bleiben bytegenau. Der Quellcommit wird dynamisch über `git rev-parse HEAD` im Buildmanifest protokolliert. Die normalisierte Chrome-Version wird vor dem Bundle-Build ermittelt und ist Bestandteil des kanonischen Build-ID-Objekts. Die Build-ID-Vertragsänderung gegenüber 1.0.0 ist eine `INTENDED_CHANGE`; inhaltlich unveränderte PDFs müssen ab der neuen Baseline funktional identisch bleiben.

## QA-Ergebnis

- HTML-/Datenbindungsprüfung: PASS
- Capability-Gate (A4, Cover, Margin-Boxen, Seitenzähler, Tagged-Struktur): PASS
- Negative Tests: PASS; kein PDF-Artefakt bei ungültiger Eingabe
- PDF-Struktur: PASS für StructTreeRoot, MarkInfo, Sprache `de-DE`, A4, Source Sans 3 und interne Links
- PDF-Sicherheit: PASS; keine Verschlüsselung, Formulare, JavaScript-, Launch-, EmbeddedFiles- oder Pfadaktionen
- Sonderzeichen und Textreproduzierbarkeit: PASS
- Farbe, Graustufe und Schwarz-Weiß bei 200 dpi: PASS
- Visuelle Stichproben: PASS; keine abgeschnittenen oder überlagerten Inhalte, Tabellenkopf und Statusblöcke lesbar

Es wird keine PDF/A- oder PDF/UA-Konformität behauptet. Das PDF-Skill-Referenzfile war lokal nicht verfügbar; die Prüfung erfolgte ersatzweise mit Chrome Headless, PyMuPDF, Pillow und 200-dpi-Rendervergleich.

## Nicht-Ziele und Übergang

Nicht Bestandteil dieser Phase sind Produktprofile, C01-Inhalt, öffentliche PDFs, Websiteänderungen, Formularfunktionen, Lead-Erfassung und Deployment.

Phase 3.2.2.2.4 wurde nach separater Repositoryabnahme abgeschlossen. Phase 3.2.2.2.5 prüft ausschließlich das neutrale Produktionssystem technisch, visuell, sicherheitsbezogen und hinsichtlich Accessibility. Konkrete C01–C07-Produktdaten, Produkt-Gates und Veröffentlichungen bleiben bis zur Gesamtfreigabe in Phase 3.2.2.2.6 ausgeschlossen.

Proof-PDFs, Bundles, Renderings und Reports bleiben ausschließlich unter `.tmp/phase-3-2-2-2-4/` unversioniert.
