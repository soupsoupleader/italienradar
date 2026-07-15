# Phase 3.2.2.2.5 – Systemabnahme

Status: SYSTEM_ACCEPTANCE_BLOCKED

## Baseline, Zweck und Grenzen

- Baseline: `6eb28aa68cb479bfb3467a4455aa4135bc6e4975`
- QA-Plan: `1.0.0`
- Pipeline: `P2_HTML_PRINT`
- Komponentenbibliothek: `1.1.0`
- Design-Tokens/Input-Schema: `1.0.0`, Buildsystem: `1.0.1`
- Technical-System-QA: `PASS`
- Assistive-Tech-Gate: `BLOCKED`
- System-Gate/Entscheidung: `SYSTEM_ACCEPTANCE_BLOCKED`
- Produktpilot erlaubt: `false`

Diese Phase prüft das neutrale statische PDF-Produktionssystem unter technischen, visuellen, Security-, Privacy- und Accessibility-Bedingungen. C01–C07-Produktdaten, Produktquellen, G2/G3/G4, Veröffentlichung, Websiteänderung und Deployment bleiben ausgeschlossen. Es wurde kein Produkt erzeugt.

## Traceability und QA-Abgrenzung

`system-acceptance-traceability.json` ordnet 24 produktive `QA-*`-Fälle genau einer System-, Produkt- oder Release-Kategorie zu. `ARCH-C08-001` ist separat als ein nicht-produktiver Architekturcheck geführt. Produktinhalte und Produktquellen sind delegiert; sie werden nicht als PASS gewertet. `UNMAPPED = 0`, und `NOT_TESTED` wird niemals als PASS behandelt. Die Systemtests verwenden ausschließlich das Präfix `SYSQA-`.

## Ausführungsmatrix

Der Runner prüft A: aktueller Worktree, B: sauberer detached Worktree, C: sauberer Pfad mit Leerzeichen und Unicode, D: Offline-Umgebung, E: parallele Builds sowie F: zeitgetrennte Builds. Für jeden Kontext werden Build-ID, HTML-Hash und Bundle-Nachweis temporär protokolliert. Negative Tests umfassen die zwölf Baseline-Fälle plus zwölf zusätzliche Vertrags-, Pfad-, Renderer- und Kollisionsfälle. Die 24 Negativtests bestanden.

A–F waren funktional erfolgreich und erzeugten dieselbe Build-ID `4713DD97AE1B274831B75C487EB9D87F671786A37444E3A2B46A4C1055DD4906`. Die frühere Zeilenendenabweichung ist durch die 1.0.1-Kanonisierung behoben. Die frühere Chrome-stderr-Störung ist durch kontrollierte Prozessauswertung behoben.

Die Matrix, Source-Hashes, Umgebungsdaten und Reports liegen ausschließlich unter `.tmp/phase-3-2-2-2-5/system-acceptance/`.

## Technische Prüfbereiche

Geprüft werden Baseline-Integrität, JSON-/Python-/PowerShell-Verträge, M01–M12-Parität, Mastertemplate, deterministische Datenbindung, Offline-Ressourcen, Rendererauflösung, Fehlercontainment, Pfadunabhängigkeit, Parallelität, PDF-Geometrie, Metadaten, Struktur, Links, Fonts, Sicherheit, Datenschutz und visuelle Farbvarianten.

Die PDF-Abnahme verwendet Chrome Headless, PyMuPDF und Pillow. Das PDF-Skill-Referenzfile war lokal nicht verfügbar; deshalb gilt: `PDF_SKILL_FILE_AVAILABLE = false`, Fallback: `Chrome Headless + PyMuPDF + Pillow + 200-dpi visual inspection`.

## Accessibility und Assistive-Tech-Gate

Strukturelle Prüfungen für Sprache, Titel, Überschriften, Listen, Tabellen, Links und Tagged-PDF-Merkmale werden getrennt von der praktischen Lesereihenfolge dokumentiert. Ein tatsächlicher Screenreader-, PAC-/Acrobat- oder gleichwertiger Assistive-Tech-Nachweis ist in der lokalen Umgebung nicht verfügbar. Daher lautet `SYSQA-A11Y-ASSISTIVE = BLOCKED`.

Dieser Blocker darf nicht durch `StructTreeRoot` oder `MarkInfo` ersetzt werden. Die technische Nachbesserung ist PASS; wegen des fehlenden praktischen Assistive-Tech-Nachweises lautet die Systementscheidung `SYSTEM_ACCEPTANCE_BLOCKED`, nicht `SYSTEM_READY_FOR_PRODUCT_PILOT`. Es wird keine PDF/UA- oder PDF/A-Konformität behauptet.

## Produkt-Gates und offene Punkte

`G2`, `G3` und `G4` bleiben unerfüllt. Es gibt keine Produktfreigabe, keine Veröffentlichung und keine Websiteintegration. Für 3.2.2.2.6 offen ist ein geeigneter praktischer Accessibility-Nachweis und danach die erneute Systementscheidung.

Generierte PDFs, HTML-Dateien, Bundles, Reports, Renderbilder, Testfixtures und Logs bleiben unversionierte Nachweise. Die sechs QA-Quelldateien dokumentieren diesen blockierten Status und werden separat versioniert. Das lokale A11Y-Reviewpaket sowie alle Ergebnisprotokolle bleiben unversioniert. Nach einer unabhängigen praktischen Prüfung ist die Systementscheidung neu zu treffen.
