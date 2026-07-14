# ItalienRadar / IMR - Phase 3.2.1.3.3 Technischer PDF-, Metadaten-, Datei- und Sicherheitsstandard

## Geltungsbereich und Status

- Phase: `3.2.1.3.3`
- Status: `PDF_TECHNICAL_STANDARD_DRAFT`
- Grundlage: Phasen 3.2.1.1, 3.2.1.2, 3.2.1.3.1 und 3.2.1.3.2
- Design-Baseline-Commit: `86027ca2025a6c5261d4554c08c1468ac6113cf3`
- Vollständig betroffen: statische Dokumente `C01` bis `C07`
- Nur architektonisch betroffen: dynamische Ergebnisprotokoll-Familie `C08`
- Nicht Bestandteil: PDF- oder DOCX-Erzeugung, Buildsystem, HTML-, CSS- oder JavaScript-Änderungen, Schriftinstallation, Formulare, Downloadseiten, Lead-Erfassung, Dateiupload, Commit, Push oder Deployment

Dieser Standard ändert keine Produktklasse, Nutzeraufgabe, Zielgruppe, Risikoklasse, Aktualitätsklasse oder Inhaltsgrenze. Er definiert nur technische Mindestanforderungen für spätere PDF-Dateien.

## Normative Sprache

| Begriff | Bedeutung |
|---|---|
| MUSS | Zwingende technische Anforderung. Eine Abweichung führt zu `FAIL`. |
| DARF NICHT | Zwingendes Verbot. Ein Verstoß führt zu `FAIL`. |
| SOLL | Starke Empfehlung. Eine Abweichung braucht eine dokumentierte Begründung. |
| KANN | Optionale technische Möglichkeit ohne Abnahmepflicht. |

## Produktionsprinzip und Quellennachweis

Eine veröffentlichte PDF MUSS aus einer versionierten Quelldatei erzeugt werden:

`strukturierte Quelle -> reproduzierbarer Build -> PDF-Ausgabe -> technische Prüfung -> Rendering -> visuelle Prüfung -> Freigabe`

Eine veröffentlichte PDF DARF NICHT ausschließlich manuell in der PDF-Datei bearbeitet werden. Fachliche Änderungen MÜSSEN zuerst in der Quelle erfolgen. Jede PDF MUSS auf eine eindeutig identifizierbare Quellversion zurückführbar sein. Ein erneuter Build derselben Quellversion SOLL ein funktional gleichwertiges Ergebnis liefern.

Manuelle Nachbearbeitung der finalen PDF MUSS als Ausnahme dokumentiert werden. Nicht reproduzierbare Bearbeitungsschritte blockieren die Freigabe.

## Pipelineklassen und Auswahlregel

| Pipeline | Quelle und Ausgabe | Geeignet für |
|---|---|---|
| `P1_DOCUMENT` | Dokumentquelle, etwa DOCX, -> kontrollierte PDF-Konvertierung | längere Planungsdokumente, Überschriften, Tabellen, Checklisten und Fließtext |
| `P2_HTML_PRINT` | HTML plus Print-CSS -> kontrollierter PDF-Renderer | standardisierte Layouts, automatisierte Builds und wiederverwendbare Komponenten |
| `P3_PROGRAMMATIC` | strukturierte Daten plus Template -> PDF-Bibliothek oder Renderdienst | dynamische Ergebnisse, Serienerzeugung und C08-Protokolle |

`C01` bis `C07` KÖNNEN `P1_DOCUMENT` oder `P2_HTML_PRINT` verwenden. `C08` wird voraussichtlich `P2_HTML_PRINT` oder `P3_PROGRAMMATIC` benötigen. Eine Pipeline DARF NICHT gewählt werden, wenn sie keine reproduzierbare Ausgabe, keine nutzbare Tag-Struktur oder keine sichere Schriftunterstützung ermöglicht. Die endgültige Pipelineentscheidung erfolgt erst nach einem technischen Prototypen.

## PDF-Basisformat und Seitengeometrie

Jede veröffentlichte Datei MUSS eine valide PDF sein, ohne Reparaturwarnung in verbreiteten PDF-Readern funktionieren und vollständig lokal lesbar sein. PDF 1.7 oder eine technisch gleichwertige moderne Ausgabe SOLL verwendet werden. Eine andere Version benötigt dokumentierte Kompatibilitätsprüfung ohne Verlust von Sicherheits- oder Accessibility-Funktionen.

PDF/A-2u oder ein vergleichbarer Archivstandard KANN später angestrebt werden. PDF/A- oder PDF/UA-Konformität DARF NICHT behauptet werden, ohne geeignete Validatorprüfung.

`C01` bis `C07` MÜSSEN im DIN-A4-Hochformat (`210 × 297 mm`, ungefähr `595 × 842` PDF-Punkte) erzeugt werden. `MediaBox` und `CropBox` MÜSSEN konsistent sein. `TrimBox` und `BleedBox` KÖNNEN ohne Beschnitt identisch gesetzt werden. Wechselnde Seitengrößen ohne dokumentierten Grund, US-Letter-Seiten, negative Seitenboxen, Inhalte außerhalb der sichtbaren CropBox, Druckmarken und Beschnittzugaben sind in öffentlichen Arbeitsdokumenten nicht zulässig.

## Metadaten und sichtbarer Buildstand

Jede PDF MUSS mindestens `Title`, `Author`, `Subject`, `Keywords`, `Language`, `Product ID`, `Version`, `Creation date` und `Modification date` enthalten.

| Feld | Verbindlicher Wert oder Regel |
|---|---|
| `Author` | `ItalienRadar` |
| `Language` | `de-DE` |
| `Title` | kanonischer Produkttitel |
| `Subject` | knappe Hauptfunktion aus dem Produktvertrag |
| `Keywords` | ItalienRadar, Italien, Produktthema, Produkt-ID und Dokumentklasse |
| interne Produktmetadaten | `product_id`, `document_version`, `update_class`, `risk_class`, `source_version`, `build_version` |

Dokumentversion, Aktualisierungsdatum und Quellenstand MÜSSEN sichtbar sein. Intern MÜSSEN zusätzlich Build-ID, Quellcommit oder vergleichbare Quellversion und Generatorversion nachvollziehbar bleiben.

Die PDF DARF NICHT persönliche Redakteursnamen ohne Absicht, private E-Mail-Adressen, lokale Dateipfade, Windows-Benutzernamen, temporäre Verzeichnisse, interne Serveradressen, API-Schlüssel, Kommentare, Bearbeitungsnotizen oder nutzlose sensible Buildinformationen enthalten.

## Dateinamen und Versionierung

Das Grundformat lautet `<produkt-slug>-v<major>-<minor>.pdf`, zum Beispiel `italien-neustart-budget-sicherheitsarbeitsblatt-v1-0.pdf`.

Dateinamen MÜSSEN Kleinbuchstaben und Bindestriche verwenden, ohne Leerzeichen, Umlaute, ß oder weitere Sonderzeichen auskommen und eine stabile verständliche Versionsnummer enthalten. `final.pdf`, `final-neu.pdf`, `final2.pdf`, `letzte-version.pdf` und `dokument-aktuell.pdf` sind nicht zulässig.

Die sichtbare Dokumentversion lautet `v1.0`, `v1.1` oder `v2.0`. Die Major-Version MUSS bei struktureller Neufassung, geänderter Hauptlogik, neuen zentralen Modulen, wesentlich geändertem Ergebnis oder inkompatibler Änderung steigen. Die Minor-Version MUSS bei aktualisierten Zahlen, Quellenkorrekturen, kleinen redaktionellen Änderungen oder nicht struktureller Korrektur steigen. Eine interne Build-Version wie `build 2026.07.14.1` KANN ergänzt werden, ersetzt aber nicht die öffentliche Dokumentversion.

Eine dynamische C08-Datei benötigt zusätzlich eine nicht personenbezogene Ergebniskennung, etwa `italien-kostenrechner-ergebnis-8f31c2-v1-0.pdf`. Diese Kennung DARF NICHT unmittelbar aus E-Mail-Adresse, Name, Telefonnummer, IP-Adresse oder vollständigem Zeitstempel entstehen.

## Schriften, Textkodierung, Bilder und Kompression

Jede verwendete Schrift MUSS rechtlich für Einbettung und Verteilung zugelassen sein. Notwendige Schriften MÜSSEN eingebettet oder als technisch sichere Standardschrift verfügbar sein. Subset-Einbettung SOLL verwendet werden, sofern sie zuverlässig funktioniert. Umlaute, ß, Eurozeichen und italienische Sonderzeichen MÜSSEN korrekt dargestellt und extrahierbar sein.

Nicht eingebettete exotische oder lizenzrechtlich unklare Schriften, fehlende Glyphen, unerwartete Ersatzschriften und Text als Bild zur Umgehung von Schriftproblemen sind nicht zulässig. Spätere QA MUSS Schriftfamilien, Einbettungs- und Subset-Status, fehlende Glyphen und Ersatzschriften prüfen.

Sichtbarer Text MUSS echter, auswählbarer Text sein. Unicode-Mapping MUSS soweit technisch möglich korrekt sein; Suche und Kopieren SOLLEN funktionieren. Vollständig gerasterte Textseiten, unlesbare Zeichencodierung, schwarze Kästchen und unbrauchbare Kopierergebnisse sind nicht zulässig. Technische IDs, Dateinamen und maschinenlesbare Werte SOLLEN ASCII-Bindestriche verwenden.

Fotos SOLLEN ungefähr `150-220 dpi`, Diagramme und textnahe Grafiken `200-300 dpi` haben; Logos SOLLEN Vektorformate verwenden. Bilder MÜSSEN für die Ausgabegröße optimiert sein. Funktionale Grafiken benötigen Textalternative oder Beschreibung, Transparenzen MÜSSEN im Zielrenderer geprüft werden, und externe Bildreferenzen, nachgeladene Webbilder sowie private EXIF- oder Standortdaten sind nicht zulässig. Bildmetadaten SOLLEN vor Einbettung entfernt werden.

Die Farb- und Graustufenregeln des Designstandards MÜSSEN technisch erhalten bleiben. Farbige Statusinformationen benötigen deshalb zusätzlich Text oder ein eindeutiges Symbol; Flächen, Linien, Eingabefelder und Tabellen MÜSSEN bei Farb-, Graustufen- und Schwarz-Weiß-Rendering unterscheidbar und lesbar bleiben.

| Produktklasse | Zielgröße |
|---|---|
| `A` | möglichst unter 1 MB |
| `B` | möglichst unter 2 MB |
| `C` | möglichst unter 4 MB |
| `E` | möglichst unter 3 MB |
| `C08` | grundsätzlich unter 3 MB, abhängig vom Ergebnis |

Dateigröße DARF NICHT auf Kosten der Lesbarkeit reduziert werden. Identische Ressourcen SOLLEN nicht mehrfach eingebettet und nicht verwendete Objekte SOLLEN entfernt werden. Jede Überschreitung braucht eine dokumentierte Begründung.

## Navigation und Links

Dokumente mit mehr als ungefähr fünf Inhaltsseiten SOLLEN ein klickbares Inhaltsverzeichnis und PDF-Lesezeichen enthalten. Lesezeichen MÜSSEN logisch hierarchisch sein, den sichtbaren Überschriften entsprechen und auf die richtige Zielseite führen. Interne Links MÜSSEN korrekt funktionieren und beschreibenden Linktext statt „hier klicken“ verwenden.

Externe Links MÜSSEN vor Veröffentlichung geprüft werden, HTTPS verwenden, wenn verfügbar, und bevorzugt auf offizielle Primärquellen verweisen. URL-Shortener, nicht nachvollziehbare Tracking-Weiterleitungen, `javascript:`-Links, `file:`-Links, lokale Dateipfade, unsichere Aktionen und automatische Linköffnung beim Dokumentstart sind nicht zulässig. Veraltete oder umgeleitete Links MÜSSEN dokumentiert werden.

## PDF-Aktionssicherheit, Rechte und versteckte Daten

PDFs DÜRFEN KEIN JavaScript, keine Launch Actions, keine Open Actions mit ausführbarem Verhalten, keine eingebetteten ausführbaren Dateien, keine automatischen Netzwerkaufrufe, keinen Multimedia-Autostart, keine unsichtbaren Links und keine versteckten Formulareingaben enthalten. Dateianhänge innerhalb einer PDF sind für normale ItaliaRadar-Downloads nicht zulässig.

Freie öffentliche Downloads DÜRFEN NICHT mit Öffnungspasswort geschützt sein, Drucken oder Kopieren unnötig blockieren oder von proprietärer Rechteverwaltung abhängen. Berechtigungsbeschränkungen sind kein Schutz für sensible Informationen; diese DÜRFEN gar nicht erst in öffentliche Dateien gelangen.

Vor Veröffentlichung MUSS auf Kommentare, Notizen, Revisionen, ausgeblendete Ebenen, unsichtbaren Text, eingebettete Quelldateien, Formular-Testwerte, persönliche Metadaten, lokale Pfade, temporäre Links und interne Kennzeichnungen geprüft werden. Nicht benötigte Objekte MÜSSEN entfernt werden.

## Technische Accessibility und Tabellenstruktur

Jede veröffentlichte PDF SOLL technisch strukturiert sein. Mindestanforderungen sind Dokumentsprache `de-DE`, gesetzter Titel, logische Lesereihenfolge, Überschriften-, Listen- und Tabellenstruktur, Linkauszeichnung sowie Alternativtexte für funktionale Bilder. Statische PDFs SOLLEN als getaggte PDFs erzeugt werden.

Tags MÜSSEN ihrer tatsächlichen Funktion entsprechen: `H1-Hn`, `P`, `L`, `LI`, `Table`, `TR`, `TH`, `TD`, `Link` und `Figure`. Rein visuelle Lesereihenfolgen, Überschriften nur durch Schriftgröße, Tabellen als beliebige Textblöcke und leere Alternativtexte sind nicht zulässig. Tags allein reichen nicht: Die Lesereihenfolge MUSS geprüft werden.

PDF-Tabellen MÜSSEN Kopfzellen als `TH`, Datenzellen als `TD`, eine logische Zeilen- und Spaltenzuordnung sowie Kontext auf Folgeseiten haben. Rein grafische und unnötig komplex verschachtelte Tabellen sind nicht zulässig. Kopfzeilen MÜSSEN bei mehrseitigen Tabellen sichtbar wiederholt werden.

## Formulararchitektur und Datenschutz

In dieser Phase werden keine Formularfelder implementiert. Für spätere ausfüllbare PDFs ist `AcroForm` bevorzugt. `XFA` ist nicht zulässig, wenn dies plattformübergreifende Nutzung oder Accessibility einschränkt.

Jedes spätere Feld MUSS eindeutigen technischen Namen, sichtbares Label, Feldtyp, zulässigen Wert, Tab-Reihenfolge, Accessibility-Bezeichnung sowie gegebenenfalls Format- oder Längenregel haben. Beispiele sind `c01.monthly_housing_cost`, `c01.reserve_months` und `c05.ateco_question`; generische Namen wie `Text1`, `Field23` und `CheckBox7` sind nicht zulässig. Formularlogik DARF NICHT von PDF-JavaScript abhängen.

`C01` bis `C07` KÖNNEN später lokal ausfüllbar sein, ohne Daten an ItalienRadar zu übertragen. Automatische Übermittlung, versteckte Endpunkte, Telemetrie, Tracking, vorausgefüllte personenbezogene Daten und Serverspeicherung ohne gesonderte Einwilligung und Architektur sind nicht zulässig. Ein ausfüllbares PDF MUSS später über lokale Speicherung, mögliche sensible Angaben und den sicheren Umgang bei Weitergabe informieren.

## C08 - Dynamische Ergebnisprotokolle

`C08` bleibt technisch getrennt. Vor Umsetzung sind Datenmodell, Eingabe-Ausgabe-Mapping, Ergebnislogik, Datenschutzentscheidung, Speicherstrategie, Löschkonzept, Fehlerfallmodell, Versionsmodell, Renderpipeline sowie Last- und Missbrauchsschutz zwingend erforderlich.

Die bevorzugte Architektur SOLL clientseitige oder kurzlebige Generierung ohne dauerhafte Speicherung nutzen. Dauerhafte Speicherung persönlicher Eingaben, Übertragung sensibler Daten an Dritte, personenbezogene Ergebnis-URLs, öffentlich erratbare Dateinamen, unbegrenzte Speicherung und unprotokollierte externe PDF-Dienste sind ohne gesonderte Freigabe nicht zulässig.

Jedes spätere C08-Protokoll benötigt Tool-ID, Ergebnislogik-Version, Dokumentversion, Erstellungszeitpunkt, Eingabezusammenfassung, Ergebnisstatus, Warnungen, nächste Schritte und Datenschutzhinweis. Diese Anforderungen erzeugen noch keine Generierungslogik oder Datenverarbeitung.

## Dateitrennung und Integrität

Die spätere Dateiarchitektur MUSS mindestens `source/`, `build/`, `release/` und `archive/` unterscheiden: bearbeitbare Quellen, temporäre Ausgaben, freigegebene Dateien und ersetzte Veröffentlichungen. Builddateien DÜRFEN NICHT versehentlich als öffentliche Releases behandelt werden. Konkrete Repositorypfade werden erst in der Speicher- und Dateisystemphase bestimmt.

Vor Veröffentlichung MUSS jede PDF auf Lesbarkeit, valide Struktur, plausible Seitenzahl, korrektes Seitenformat, eingebettete Schriften, korrekte Metadaten, gültige Links, fehlende verbotene Aktionen und versteckte Daten sowie Zielgröße geprüft werden. Jede Release-Datei SOLL einen `SHA-256`-Hash für Integrität und Versionserkennung erhalten.

## Render-, Regression- und Kompatibilitätsprüfung

Jede PDF MUSS vor Veröffentlichung vollständig gerendert werden. Die Prüfung umfasst alle Seiten, abgeschnittene oder überlappende Inhalte, Tabellen, Eingabefelder, Sonderzeichen, Seitenumbrüche und zusätzlich die technische Linkprüfung. Mindestens ein verbreiteter Renderer MUSS genutzt werden; bei komplexen Formularen, Transparenzen oder ungewöhnlichen Schriften SOLLEN zwei unterschiedliche Renderer genutzt werden.

Abgeschnittener Text, überlappende Elemente, schwarze Kästchen, fehlende Glyphen, leere Seiten, unbeabsichtigte Seitenumbrüche, unlesbare Tabellen, fehlende Felder und falsche Seitengröße führen zu `FAIL`.

Bei einer neuen Version SOLL die gerenderte Datei gegen die Vorgängerversion verglichen werden. Der Vergleich MUSS beabsichtigte von unbeabsichtigten Layoutänderungen unterscheiden. Unerklärte großflächige Unterschiede blockieren die Freigabe.

Spätere QA SOLL Browser-PDF-Viewer, Adobe Acrobat Reader oder gleichwertigen Reader sowie mobilen PDF-Viewer prüfen. Ausfüllbare PDFs benötigen zusätzlich Prüfung von Speichern, erneutem Öffnen, Drucken und Tab-Reihenfolge. Kein Produkt DARF eine nicht kommunizierte Funktion verlangen, die nur in einem proprietären Reader funktioniert.

## Fehlerklassen und Release-Gate

| Fehlerklasse | Beispiele | Veröffentlichung |
|---|---|---|
| `P0_BLOCKER` | Datei öffnet nicht, falsches Dokument, sensible Daten, gefährliche Aktion, fehlende zentrale Seiten | verboten |
| `P1_CRITICAL` | abgeschnittener Inhalt, falsche Berechnung, unlesbare Schrift, falsche Version, zentraler Link defekt, fehlerhafte Formularspeicherung | verboten |
| `P2_MAJOR` | fehlende Metadaten, fehlerhafte Lesezeichen, Accessibility-Strukturfehler, deutlich überhöhte Dateigröße, unklarer Seitenumbruch | vor Veröffentlichung beheben oder ausdrücklich freigeben |
| `P3_MINOR` | kleine optische Abweichung, nicht kritische Metadatenverbesserung, geringer Kompressionsbedarf | dokumentiert nachlagerbar |

Eine PDF darf nur veröffentlicht werden, wenn `P0 = 0`, `P1 = 0`, `P2 = 0` oder ausdrücklich freigegeben und `P3` dokumentiert ist. Technische Validierung, Renderprüfung, Metadatenprüfung, Linkprüfung, Sicherheitsprüfung, Dateinamenprüfung und Versionsprüfung MÜSSEN bestanden sein.

## Kontrollierte Vorbereitung für spätere Maschinenlesbarkeit

Diese Phase erzeugt keine JSON-Datei. Für eine spätere Übernahme sind ausschließlich vorgesehen: `pdf_version_policy`, `page_geometry`, `metadata_fields`, `forbidden_metadata`, `filename_pattern`, `versioning_rules`, `font_requirements`, `image_requirements`, `compression_targets`, `link_rules`, `forbidden_actions`, `accessibility_tags`, `form_field_rules`, `privacy_rules`, `dynamic_pdf_prerequisites`, `release_checks`, `render_checks`, `error_severity` und `release_gate`.

## Technische Abnahmekriterien

Vor einer PDF-Produktion müssen Produktionsprinzip, Pipelineklasse, Basisformat, Seitengeometrie, Metadaten, Dateinamen, Versionierung, Schriften, Textkodierung, Bilder, Kompression, Navigation, Links, Sicherheitsaktionen, versteckte Daten, Accessibility, Tabellenstruktur, Formulararchitektur, Datenschutz, C08-Abgrenzung, Integrität, Renderprüfung, Regression, Kompatibilität, Fehlerklassen und Release-Gate geprüft werden.

Jede Prüfung erhält `PASS`, `FAIL` oder `NOT_APPLICABLE`. Ein `FAIL` blockiert die Veröffentlichung.

Dieser Standard ist ein Dokumentationsartefakt. Er erzeugt keine PDF-Datei, keine Build- oder Produktionsverzeichnisse, keine aktive Datenerfassung und keine Auslieferungslogik.