# Phase 3.2.2.2.2 – Verbindliches PDF-Designsystem

Stand: 15.07.2026
Phase: `3.2.2.2.2`
Baseline: `121429fb58ae2675de4661711df84659994e3deb`
Pipeline: `P2_HTML_PRINT`

## Geltungsbereich

Dieses Designsystem ist die versionierte Grundlage für `C01` bis `C07`. Es definiert Tokens, lokale Typografie, DIN A4, Farbrollen, Kontrast, Kopf-/Fußzeilen, Seitenzahlen, Umbrüche und Printregeln. Der lokale Nachweis ist neutral mit Testwert `T00`; er ist weder C01-Inhalt noch Mastertemplate.

Nicht-Ziele: kein Produktinhalt, kein Mastertemplate, keine M01–M12-Implementierung, keine Websiteänderung, keine Lead-Erfassung, keine Formulare oder AcroForm-Felder, kein öffentliches PDF und kein Deployment. `C08` bleibt außerhalb der statischen Produktion.

## Schriftentscheidung und Lizenz

Primärfamilie ist ausschließlich **Source Sans 3**. Verwendet werden die unveränderten statischen WOFF2-Dateien aus dem offiziellen Adobe-Repository `adobe-fonts/source-sans`, Release `3.052` / Tag `3.052R` / Release-Commit `ed18089`. Die Lizenzdatei ist OFL-1.1 und liegt neben den Fontdateien.

| Datei | Gewicht | SHA-256 |
|---|---:|---|
| `source-sans-3-regular.woff2` | 400 | `53492FB3A0DEF77354F166A55D09B63A10855E91C206C7620A81CF56E97F8EC3` |
| `source-sans-3-semibold.woff2` | 600 | `47B9B661B9F395FE7F0D0E119637FBA5C8DAD97BDE3DF60066FD24229C0792F4` |
| `source-sans-3-bold.woff2` | 700 | `8D35C6D40E750A4EE23BBBBA2BD604AD098D172907369B43281507E16B8E2E7A` |
| `LICENSE.md` | OFL-1.1 | `56AF9B9C6715597E458284A474DC118A50A4150E9D547C70F7B4A33C3E6A9328` |

Die lokale Browserprüfung meldete Source Sans 3 geladen. Die Glyphprobe `Ä Ö Ü ä ö ü ß € à è é ì ò ó ù I l 1 O 0` war vollständig sichtbar. Es gibt keine `local()`-Quelle, keinen CDN-Load, keinen externen Import und keine systemweite Schriftinstallation. Ein späterer Build muss bei fehlender Fontladung abbrechen.

## A4-Raster und Maße

| Token | Wert |
|---|---:|
| PAGE_WIDTH / PAGE_HEIGHT | 210 mm × 297 mm |
| ORIENTATION | portrait |
| MARGIN_LEFT / MARGIN_RIGHT | 20 mm / 20 mm |
| MARGIN_TOP / MARGIN_BOTTOM | 19 mm / 19 mm |
| CONTENT_WIDTH / CONTENT_HEIGHT | 170 mm × 259 mm |
| PHYSICAL_SAFETY_ZONE | 12 mm |
| Grundraster | einspaltig |
| kurze gleichwertige Inhalte | maximal zwei Spalten |

Langer Fließtext bleibt einspaltig. Querformat gehört nicht zum Basissystem. Wichtige Inhalte dürfen nicht in die 12-mm-Sicherheitszone ragen und dürfen nicht von randlosem Druck abhängen.

## Spacing, Rahmen und Radien

`SPACE_XS = 2.5mm`, `SPACE_S = 4.5mm`, `SPACE_M = 8mm`, `SPACE_L = 13.5mm`, `SPACE_XL = 21mm` sind die verbindlichen Abstandsklassen. Zusätzlich gelten `BORDER_THIN = 0.25mm`, `BORDER_STANDARD = 0.5mm`, `BORDER_STRONG = 0.8mm`, `RADIUS_SMALL = 1.5mm` und `RADIUS_MEDIUM = 2.5mm`. Radien werden sparsam eingesetzt; es entsteht kein Web-App- oder Broschürencharakter.

## Typografische Hierarchie

| Rolle | Größe | Gewicht | Zeilenhöhe |
|---|---:|---:|---:|
| V0_COVER_TITLE | 30 pt | 700 | 1.10 |
| COVER_SUBTITLE | 14 pt | 400 | 1.35 |
| V1_CHAPTER | 21 pt | 700 | 1.20 |
| V2_SECTION | 16.5 pt | 700 | 1.25 |
| V3_SUBSECTION | 13.5 pt | 600 | 1.30 |
| V4_INSTRUCTION | 11.5 pt | 600 | 1.40 |
| V5_BODY | 11 pt | 400 | 1.42 |
| V6_FIELD_LABEL | 9.5 pt | 600 | 1.30 |
| V7_NOTE_SOURCE | 9 pt | 400 | 1.40 |
| V8_METADATA | 8.5 pt | 400 | 1.35 |
| TABLE_BODY / TABLE_HEADER | 9.25 pt | 400 / 600 | 1.30 / 1.25 |
| FOOTER | 8.25 pt | 400 | 1.25 |

Fließtext ist linksbündiger Flattersatz ohne Absatz-Einrückung. Absatztrennung verwendet `SPACE_S`; Blocksatz, lange Versalpassagen, zentrale kursive Anweisungen und Tabellen unter 9 pt sind nicht zulässig. Quellen bleiben mindestens 8.5 pt groß.

## Farbrollen und Kontrast

Die Tokenwerte stehen in `download-system/tokens/design-tokens.json` und werden ausschließlich über `--imr-*`-Properties in `design-tokens.css` gespiegelt. Definiert sind Brand-, Text-, Hintergrund-, Surface-, Border-, Info-, Warning-, Critical-, Success- und Input-Rollen.

Die programmatische Prüfung ohne Vorabrundung ergab für alle funktionalen Text-/Hintergrundpaare PASS. Der schlechteste erforderliche Wert ist `5.045585` (`BRAND_SECONDARY` auf `BACKGROUND`) und liegt über 4.5:1. Die Borderfarbe `#8F9B94` erreicht auf Weiß `2.882996` und wird deshalb ausschließlich als dekorative Trennlinie verwendet; funktionale Abgrenzungen verwenden kontraststärkere Brand-/Statusfarben. Der vollständige Bericht liegt unter `.tmp/phase-3-2-2-2-1/design-token-proof/contrast-report.json`.

Farbe ist nie die alleinige Information. `HINWEIS` nutzt Label und Standardrahmen, `WARNUNG` Label und stärkeren linken Rand, `BLOCKER` Label und vollständigen starken Rahmen, `STATUS` ein sichtbares Statuslabel. Rot und Grün sind nicht dekorativ beziehungsweise keine fachliche Bestätigung.

## Cover-, Kopf- und Fußzeilenvertrag

Das Cover hat keinen laufenden Kopf, zeigt ItalienRadar, neutralen Titel, Funktionsbeschreibung, Produkt-ID, Version und Aktualisierungsstand in einem ruhigen Metadatenbereich. Es verwendet weder vollflächige Dunkelfläche noch Foto, 3D-Effekt oder Marketingversprechen.

Innenseiten reservieren `HEADER_HEIGHT_TARGET = 7mm` und `FOOTER_HEIGHT_TARGET = 7mm`. Der Kopf darf verkürzten Titel, Kapitelname und ItalienRadar-Kennung führen. Der Fuß muss Produkt-ID, Version und die Seitenzahl im Format **Seite X von Y** enthalten; bei U3/U4 kommt der Aktualisierungsstand hinzu. Die echte Gesamtseitenzahl wird erst im Buildschritt 3.2.2.2.4 erzeugt; der Proof simuliert sie.

## Seitenumbruch und Print

`ORPHANS = 3` und `WIDOWS = 3`. Überschrift/Folgeabsatz, Feldlabel/Eingabefläche, Warnung/Blocker, Tabellenkopf/erste Datenzeile, Kontrollfeld/Bezeichnung, Ergebnisüberschrift/erster Wert und Quelle/Quellenbezeichnung bleiben zusammen. H1–H3 verwenden `break-after: avoid-page`; kurze Statusblöcke, Checklistenelemente, Eingabegruppen und Tabellenzeilen `break-inside: avoid-page`. Tabellenköpfe wiederholen sich auf Folgeseiten.

Lange Module erhalten kein pauschales `break-inside: avoid`. Große Kapitel beginnen bevorzugt neu, aber nicht auf Kosten regelmäßig mehr als etwa eines Drittels ungenutzter Vorseite. Es gibt keine alleinstehende Überschrift, keine einzelne letzte Absatzzeile auf einer neuen Seite und keine funktional unbegründete halbleere Seite.

Printausgaben verwenden helle Hintergründe, keine Transparenz und keine vollflächig dunklen Seiten. Eingabeflächen, Statusblöcke und Linien bleiben in Farbe, Graustufe und Schwarz-Weiß unterscheidbar. 100-Prozent-Druck und „An Seite anpassen“ werden im späteren Produkt-QA-Gate geprüft; Duplex darf keine inhaltliche Abhängigkeit zerstören.

## Browser-, Offline- und Postprocessing-Vertrag

Die spätere Rendererauflösung erfolgt in dieser Reihenfolge: `ITALIENRADAR_CHROME_PATH`, registrierter Windows-App-Pfad, standardisierte Program-Files-Pfade, danach kontrollierter Fehler. Im lokalen Nachweis wurde `C:\Program Files\Google\Chrome\Application\chrome.exe` mit Version `144.0.7559.110` verwendet; dieser Benutzerpfad wird nicht in PDFs oder Metadaten geschrieben.

Der Offline-Vertrag verwirft HTTP-/HTTPS-Schriften, externe Bilder, Stylesheets und Skripte. Browser-Hintergrundnetzwerk wird im Produktionsbuild deaktiviert; ein fehlendes Netzwerk darf das Ergebnis nicht verändern. Es gibt keine Website-CSS-Abhängigkeit.

`POSTPROCESSING_MODE = CONDITIONAL_METADATA_ONLY`. Metadaten werden bevorzugt aus kontrollierter HTML-Quelle gesetzt. PyMuPDF darf nur für kontrollierte Metadaten-/Boxkorrektur eingesetzt werden, wenn ein Vorher-/Nachher-Test StructTreeRoot, MarkInfo, Sprache, Tags, Lesereihenfolge, Links und Sicherheitsstruktur bestätigt. Schlägt dieser Test fehl, bleibt Postprocessing deaktiviert. Im aktuellen Proof war keine strukturerhaltende Nachbearbeitung erforderlich; PyMuPDF bestätigte MediaBox/CropBox als identische A4-Rechtecke.

## Lokaler Designnachweis

Der neutrale Proof unter `.tmp/phase-3-2-2-2-1/design-token-proof/` umfasst drei A4-Seiten: Cover/Metadaten, V1–V8/Spacing/Status/Input und Tabelle/Checkliste/Umbruch/Quellen. Die Farb-, Graustufen- und Schwarz-Weiß-Renderungen umfassen jeweils drei Seiten bei 1654 × 2339 Pixel Zielauflösung. Sichtprüfung: kein Überlauf, keine abgeschnittenen Inhalte, keine unerwarteten Umbrüche, lesbare Mindestschrift, unterscheidbare Statusblöcke und sichtbare Eingabefläche.

Die technische PDF-Prüfung ergab drei Seiten, A4-MediaBox/CropBox, Titel, `de-DE`, `StructTreeRoot`, `MarkInfo`, H1/H2/H3, eingebettete Source-Sans-3-Subsets, Unicode-Text und keine Verschlüsselung, JavaScript-, Launch-, OpenAction-, Additional-Action-, EmbeddedFile-, Anhang- oder Linkrisiken. Es wird ausdrücklich keine PDF/A- oder PDF/UA-Konformität behauptet.

## Konsistenz und offene Punkte

JSON ist syntaktisch valide. Die 59 Tokenbereichseinträge referenzieren passende `--imr-*`-Variablen; es gibt keine unbekannten Tokenrollen, doppelten Token-IDs, ungültigen Hexfarben, fehlenden Maßeinheiten, absoluten lokalen Pfade oder personenbezogenen Daten. Source Sans 3 ist genau einmal als Primärfamilie festgelegt. `C01`–`C07` sind unterstützt, `C08` ausgeschlossen, `production_started`, `public_pdf_created` und `deployment` stehen auf `false`.

Offen für 3.2.2.2.3 sind ausschließlich die Implementierung der M01–M12-Komponenten auf Basis dieser freigegebenen Tokens, die konkrete semantische HTML-Struktur je Modul, Komponenten-QA und die Verknüpfung mit neutralen Produktprofilen. Es werden dabei keine neuen Tokenrollen oder Schriftfamilien eingeführt.

## Status

Designsystem, lokale Fonts, Token-JSON/CSS und neutraler Designnachweis sind lokal erstellt und geprüft. Die Designsystemdateien bleiben bis zur separaten Repositoryabnahme uncommitted und unpushed. Kein Produkt, kein öffentliches PDF und kein Deployment wurde begonnen.
