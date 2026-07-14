# ItalienRadar / IMR - Phase 3.2.1.3.2 Designprinzipien, Dokumentraster und visuelle Hierarchie

## Geltungsbereich und Status

- Phase: `3.2.1.3.2`
- Status: `DESIGN_STANDARD_DRAFT`
- Grundlage: Phasen 3.2.1.1, 3.2.1.2 und 3.2.1.3.1
- Geltung: künftige statische Downloadprodukte `C01` bis `C07`
- Nicht Bestandteil: PDF-, DOCX- oder PPTX-Erzeugung, HTML-, CSS- oder JavaScript-Änderungen, Bilder, Logos, Downloadseiten, Formulare, Lead-Erfassung, Templates, Commit, Push oder Deployment

Der Standard übersetzt die redaktionellen Arbeitsdokumente in einen verbindlichen visuellen Produktionsrahmen. Er ändert keine Produktklasse, Nutzeraufgabe, Zielgruppe, Inhaltsgrenze, Risiko- oder Aktualitätsklasse aus den kanonischen Produktverträgen.

`C08` ist eine dynamische Ergebnisprotokoll-Familie. Sie erhält in dieser Phase kein Seitenraster und keine Ergebnisvorlage. Spätere C08-Protokolle MÜSSEN das hier definierte Grunddesign für Farben, Typografie und Metadaten berücksichtigen; variable Ergebniszonen, Seitenumbrüche und technische Komponenten werden gesondert geplant.

## Normative Sprache

| Begriff | Bedeutung |
|---|---|
| MUSS | Zwingende Voraussetzung. Eine Abweichung führt zu `FAIL`. |
| DARF NICHT | Zwingendes Verbot. Ein Verstoß führt zu `FAIL`. |
| SOLL | Starke Empfehlung. Eine Abweichung braucht eine dokumentierte Begründung. |
| KANN | Optionale Möglichkeit ohne Abnahmepflicht. |

## Markenwirkung und Gestaltungsprinzip

Alle Dokumente MÜSSEN seriös, geordnet, realistisch, praktisch, modern, ruhig und verlässlich wirken. Sie DÜRFEN NICHT wie ein Lifestyle-Magazin, Influencer-E-Book, aggressive Verkaufsbroschüre, amtliches Formular, Steuerberaterdokument, luxuriöses Reiseprospekt oder eine generische KI-Vorlage wirken.

Verbindliche Reihenfolge der Gestaltungsentscheidungen:

1. Funktion vor Dekoration.
2. Klarheit vor visueller Dichte.
3. Arbeitsnutzen vor Markeninszenierung.

Die Website-Markenreferenz wird als tiefes Grün für tragende Identität, gedämpftes Gold für sparsame Hervorhebung, helle Flächen und sachliche Statusfarben interpretiert. Diese Richtung MUSS die späteren konkreten Werte leiten, DARF aber nicht als unverändertes Weblayout in ein Dokument kopiert werden.

## Seitenformat und Sicherheitszonen

`C01` bis `C07` MÜSSEN im DIN-A4-Hochformat (`210 × 297 mm`) konzipiert werden. Ein vollständiges Dokument DARF NICHT ohne gesonderte Freigabe im Querformat produziert werden.

| Bereich | Zielwert | Zulässiger Bereich |
|---|---|---|
| Linker Außenrand | 20 mm | 18-22 mm |
| Rechter Außenrand | 20 mm | 18-22 mm |
| Oberer Seitenrand | 19 mm | 16-22 mm |
| Unterer Seitenrand | 19 mm | 16-22 mm |
| Physische Sicherheitszone | mindestens 12 mm | nicht unterschreitbar |

Kein Text, keine Seitenzahl, kein Eingabefeld und kein wichtiges Element DARF näher als 12 mm an den physischen Seitenrand gelangen. Kopf- und Fußzeilen MÜSSEN innerhalb der Sicherheitszone liegen. Inhalte DÜRFEN NICHT auf randlosen Druck angewiesen sein.

Eine einzelne Querformatseite KANN nur für eine Tabelle oder Vergleichsmatrix vorgesehen werden, wenn sie mindestens fünf funktional notwendige Spalten hat, die Hochformat-Alternative geprüft und verworfen wurde und die Abweichung später im Produktkonzept dokumentiert ist.

## Grundraster und Abstandssystem

Das primäre Inhaltsraster MUSS einspaltig sein. Es gilt für Fließtext, Anweisungen, Warnungen, Quellen, Ergebnisbereiche und die meisten Eingabefelder. Ein zweispaltiges Raster KANN für kurze Vergleichswerte, kompakte Checklisten, Metadaten, zwei gleichwertige Eingabebereiche sowie Vorher-/Nachher-Vergleiche eingesetzt werden. Lange Fließtexte DÜRFEN NICHT zweispaltig gesetzt werden. Mehr als zwei Textspalten sind nicht zulässig.

| Token | Bereich | Verwendung |
|---|---|---|
| `SPACE_XS` | 2-3 mm | Label zu Eingabefeld |
| `SPACE_S` | 4-5 mm | zusammengehörige Absätze |
| `SPACE_M` | 7-9 mm | Elemente eines Moduls |
| `SPACE_L` | 12-15 mm | Hauptabschnitte |
| `SPACE_XL` | 18-24 mm | neue Kapitel oder große Ergebnisblöcke |

Die genannten Tokens MÜSSEN verwendet werden. Frei erfundene Abstände pro Seite sind nicht zulässig.

## Visuelle Hierarchie

Jede Hierarchieebene MUSS sich durch mindestens zwei Merkmale unterscheiden, etwa Größe, Gewicht, Abstand, Position, Rahmen oder Hintergrund. Farbe allein DARF NIE die einzige Unterscheidung sein.

| Rolle | Zweck | Mindestunterscheidung |
|---|---|---|
| `V0_COVER_TITLE` | Produkttitel auf dem Cover | Größe, Gewicht, Abstand |
| `V1_CHAPTER` | Kapitelüberschrift | Größe, Gewicht, oberer Abstand |
| `V2_SECTION` | Hauptabschnitt | Gewicht, Abstand, Position |
| `V3_SUBSECTION` | Unterabschnitt | Gewicht, Abstand |
| `V4_INSTRUCTION` | Arbeitsanweisung | Gewicht, Modulfläche oder Rahmen |
| `V5_BODY` | Fließtext | Basisrolle |
| `V6_FIELD_LABEL` | Feldbezeichnung | Gewicht, Größe oder Position |
| `V7_NOTE_SOURCE` | Hinweis oder Quelle | Größe, Abstand, Flächenlogik |
| `V8_METADATA` | Versions- und Statusdaten | Größe, Position, Rahmen |

## Typografie und Lesefluss

Es darf maximal eine primäre Schriftfamilie verwendet werden. Eine zweite Familie KANN ausschließlich für markennahe Titel vorgesehen werden. Fließtext DARF NICHT dekorativ sein. Die spätere Auswahl MUSS bei PDF-Einbettung stabil sein, deutsche Zeichen unterstützen und `I`, `l`, `1`, `O` und `0` klar unterscheiden. In dieser Phase werden keine Schriftdateien ausgewählt oder eingebettet.

| Rolle | Zielgröße |
|---|---|
| Cover-Titel | 26-32 pt |
| Cover-Unterzeile | 12-16 pt |
| Kapitelüberschrift | 19-23 pt |
| Hauptabschnitt | 15-18 pt |
| Unterabschnitt | 12,5-15 pt |
| Fließtext und Arbeitsanweisung | 10,5-12 pt |
| Tabelleninhalt | mindestens 9 pt |
| Feldbezeichnung | mindestens 9,5 pt |
| Quellen | mindestens 8,5 pt |
| Fußzeile | mindestens 8 pt |

Fließtext DARF NICHT kleiner als 10,5 pt gesetzt werden. Tabellen DÜRFEN NICHT allein zur Platzersparnis verkleinert werden. Großbuchstaben DÜRFEN NICHT für längere Textpassagen und Kursivschrift DARF NICHT für zentrale Anweisungen verwendet werden. Unterstreichung ist primär Links vorbehalten.

Fließtext SOLL ungefähr 55-80 Zeichen pro Zeile und einen Zeilenabstand von 1,25-1,5-facher Schriftgröße haben. Linksbündiger Flattersatz ist Standard. Blocksatz SOLL vermieden werden, wenn große Wortabstände entstehen. Absätze werden durch Abstand, nicht durch Einrückung getrennt.

## Farbrollen und Kontrastgrundlage

Die folgende semantische Palette MUSS später mit konkreten, messbaren Farbwerten umgesetzt werden:

| Rolle | Zweck |
|---|---|
| `BRAND_PRIMARY` | Markenidentität, Titel und sparsame Hervorhebung |
| `BRAND_SECONDARY` | zurückhaltender Akzent |
| `TEXT_PRIMARY` | Haupttext mit höchstem Kontrast |
| `TEXT_SECONDARY` | sekundäre Erläuterungen und Metadaten |
| `BACKGROUND` | Seitenhintergrund |
| `SURFACE` | ruhige Modulfläche |
| `BORDER` | Begrenzung und Tabellenlinien |
| `INFO` | sachlicher Hinweis |
| `WARNING` | relevantes Risiko oder offene Annahme |
| `CRITICAL` | bearbeitungs- oder veröffentlichungsblockierendes Problem |
| `SUCCESS` | abgeschlossener oder bestätigter Arbeitsschritt |
| `INPUT_AREA` | beschreibbare oder ausfüllbare Fläche |

Bedeutungen DÜRFEN NICHT nur über Farbe vermittelt werden. Jede Statusfarbe MUSS zusätzlich Text oder ein eindeutiges Symbol erhalten. Rot DARF NICHT dekorativ und Grün DARF NICHT als automatische fachliche Bestätigung verwendet werden. Gelb DARF NICHT für normalen Fließtext eingesetzt werden. Hintergrundflächen mit Text MÜSSEN sehr hell bleiben. Das Dokument MUSS in Graustufen verständlich sein.

Fließtext benötigt klaren Hell-Dunkel-Kontrast; hellgrauer Text auf weißem Hintergrund ist nicht zulässig. Warnungen DÜRFEN NICHT nur durch Rot markiert und Links MÜSSEN zusätzlich unterstrichen oder durch eindeutigen Kontext erkennbar sein. Eingabefelder MÜSSEN in Schwarz-Weiß sichtbar bleiben. Konkrete Kontrastmessungen folgen bei Template-Produktion und QA.

## Cover, Kopfzeile und Fußzeile

Das Cover MUSS ItalienRadar, kanonischen Produkttitel, kurze Funktionsbeschreibung, Produkt-ID, Version und Aktualisierungsstand enthalten. Die Hierarchie lautet Marke, Produkttitel, Funktionsbeschreibung, Metadaten. Vollflächige schwer druckbare Fotos, Text auf unruhigem Bild, künstliche 3D-Effekte, übermäßige Schatten, große dekorative Icons, konkurrierende Titel sowie „ultimativ“ oder „garantiert“ sind nicht zulässig.

Die Kopfzeile KANN einen verkürzten Produkttitel, Kapitelname oder ItalienRadar-Kennung enthalten und DARF NICHT auf dem Cover erscheinen. Die Fußzeile MUSS Produkt-ID, Version und Seitenzahl enthalten. Bei `U3_SENSITIVE` oder `U4_EVENT_DRIVEN` MUSS sie zusätzlich den Aktualisierungsstand enthalten. Seitenzahlen werden später einheitlich als `Seite X von Y` oder `X / Y` entschieden.

## Standardisierte Modularten

| Modul | Funktion | Visuelle Regel |
|---|---|---|
| `M01_INTRODUCTION` | Einleitung | `V2_SECTION`, ruhige Textfläche |
| `M02_INSTRUCTION` | Arbeitsanweisung | `V4_INSTRUCTION`, feste Innenabstände |
| `M03_INPUT_AREA` | Eingabebereich | sichtbares Label, Schreibfläche, Begrenzung |
| `M04_TABLE` | Tabelle | Kopfzeile, Linienlogik, Umbruchregeln |
| `M05_CHECKLIST` | Checkliste | Kontrollfeld und Textbezeichnung zusammen |
| `M06_INFO` | Hinweis | sachliche Flächen- oder Rahmenlogik |
| `M07_WARNING` | Warnung | Risiko, Grund und nächster Schritt |
| `M08_BLOCKER` | kritischer Blocker | klare Sperrbedeutung und Folgehandlung |
| `M09_RESULT` | Ergebnisbereich | von Eingaben klar getrennt |
| `M10_NEXT_STEP` | nächste Schritte | priorisierte Folgehandlung |
| `M11_SOURCE` | Quelle | vollständig und lesbar, sekundär gesetzt |
| `M12_METADATA` | Metadaten | kompakt, getrennt von Quellen |

Jedes verwendete Modul MUSS eine eindeutige Funktion, feste Überschriftsebene, feste Innenabstände, definierte Rahmen- oder Flächenlogik und Seitenumbruchregeln haben. Nicht jedes Produkt muss jedes Modul verwenden.

## Hinweise, Warnungen und Blocker

Ein Hinweis ist hilfreiche Zusatzinformation und DARF den Arbeitsablauf nicht unterbrechen. Eine Warnung beschreibt relevantes Risiko oder eine ungeklärte Annahme und MUSS einen nächsten Schritt nennen. Ein Blocker bedeutet, dass Bearbeitung oder Entscheidung noch nicht als abgeschlossen gelten darf.

`M08_BLOCKER` DARF nur verwendet werden, wenn eine notwendige Angabe fehlt, eine offizielle Klärung erforderlich ist, eine zentrale Annahme nicht belastbar ist oder eine Quellenprüfung überfällig ist. Eine redaktionelle Empfehlung allein ist kein Blocker.

## Tabellen, Checklisten und Eingabefelder

Tabellen MÜSSEN eine Überschrift, klare Spaltennamen, sichtbare Maßeinheiten, ausreichende Zeilenhöhe, die Trennung von Eingabe und Ergebnis, wiederholte Kopfzeilen auf Folgeseiten sowie erkennbare Summen- und Zwischensummen enthalten. Sie DÜRFEN NICHT nur über Farbe strukturiert, kleiner als 9 pt, unnötig breit oder ohne Kopfzeile auf einer neuen Seite fortgesetzt werden.

Bei breiten Tabellen gilt zwingend diese Reihenfolge: Spalten reduzieren, Inhalte verkürzen, Tabelle aufteilen, Karten- oder Listenansicht prüfen, erst danach einzelne Querformatseite prüfen.

Jedes Kontrollkästchen MUSS eine sichtbare Textbezeichnung haben. Allgemeine Statuswerte sind `OFFEN`, `IN_BEARBEITUNG`, `ERLEDIGT` und `NICHT_RELEVANT`. Für sensible Dokumente gelten `OFFEN`, `INTERN_VORBEREITET`, `FACHLICH_ZU_KLÄREN`, `OFFIZIELL_BESTÄTIGT` und `NICHT_RELEVANT`. Farbpunkte ohne Text, „sicher erfüllt“, unklare Symbole, zu kleine Kontrollfelder und Kontrollfelder direkt am Seitenrand sind nicht zulässig.

Jede Eingabe MUSS sichtbares Label, gegebenenfalls Einheit und Zeitraum, ausreichenden Platz, eindeutige Zuordnung sowie Kennzeichnung als Schätzung, tatsächlicher Wert oder offener Wert enthalten. Vorgesehene Feldtypen sind `SHORT_TEXT`, `LONG_NOTE`, `NUMBER`, `EUR_AMOUNT`, `PERCENTAGE`, `DATE`, `STATUS`, `YES_NO` und `MULTI_SELECT`. Die technische Formularfunktion wird nicht in dieser Phase umgesetzt. Handschriftliche Einzelfelder MÜSSEN eine realistische Schreibhöhe haben.

## Ergebnisbereiche, Quellen und Metadaten

Ergebnisbereiche MÜSSEN sich klar von Eingabebereichen unterscheiden und zusammengefasste Eingaben, Status, offene Fragen, Warnsignale, nächsten Schritt und Prüfdatum aufnehmen können. Ein Ergebnis DARF NICHT nur als Ampelfarbe erscheinen; es benötigt mindestens Status, Begründung, offene Bedingungen und nächsten Schritt.

Quellenblöcke MÜSSEN visuell sekundär, aber vollständig lesbar sein. Sie DÜRFEN NICHT als unlesbare Fußnoten, kleiner als 8,5 pt, nur als rohe URL oder ohne Quellenstand erscheinen. Metadatenblöcke MÜSSEN ruhig und kompakt sein und DÜRFEN NICHT mit Quellen vermischt werden.

## Seitenumbrüche

Folgende Kombinationen DÜRFEN NICHT getrennt werden: Überschrift und erster Folgeabsatz, Feldlabel und Eingabefeld, Warnüberschrift und Warntext, Tabellenkopf und erste Tabellenzeile, Kontrollkästchen und Bezeichnung sowie Ergebnisüberschrift und erster Ergebniswert.

Einzelne letzte Absatzzeilen auf neuer Seite, alleinstehende Überschriften am Seitenende, halbleere Seiten durch unnötige manuelle Umbrüche und Tabellenfortsetzungen ohne sichtbaren Kontext SIND ZU VERMEIDEN. Große Kapitel SOLLEN auf neuer Seite beginnen, sofern dies nicht regelmäßig große Leerflächen erzeugt.

## Produktklassenspezifische Gestaltung C01-C07

| Produkt | Klasse | Verbindlicher visueller Schwerpunkt |
|---|---|---|
| `C01` | `B` | Budgettabellen, Szenarien, Summen, Rücklagen und Warnsignale; Normal-, Stress- und Mindestfall MÜSSEN auch ohne Farbe unterscheidbar sein. |
| `C02` | `B` | vergleichbare Standortkriterien, Gewichtung, Notizen und Ausschlusskriterien; keine Bestenliste oder scheinbar objektive Rangfolge. |
| `C03` | `C` | zeitlicher Aufbau, Phasen, Nachweise, Zwischenziele und Stabilitätsstatus; die Reihenfolge MUSS visuell verständlich sein. |
| `C04` | `B` | Geschäftseinnahmen, Kostenabzüge, Kundenkonzentration, Stressszenario und Mindestspielraum; persönliches Budget und geschäftliche Tragfähigkeit MÜSSEN getrennt bleiben. |
| `C05` | `E` | Unterlagenstatus, Klärungsfragen, Quellen, erhaltene Auskunft und Prüfdatum; das Dokument DARF NICHT wie ein amtliches italienisches Formular wirken. |
| `C06` | `E` | Ausschlussfragen, Beitragsfragen, Liquidität und offene Fachklärung; kein visuelles verbindliches Steuerergebnis. |
| `C07` | `C` | Projektstruktur, Kostenblöcke, Liquidität, Unterlagen, Fristen und offizielle Prüfpunkte; Programmänderungen und Quellenstand MÜSSEN besonders sichtbar sein. |

## Druck-, Bildschirm- und Iconregeln

Das Design MUSS bei Farb-, Graustufen- und Schwarz-Weiß-Druck, Duplexdruck, 100-Prozent-Druck sowie „An Seite anpassen“ funktionieren. Es MUSS überwiegend helle Hintergründe, wirtschaftlichen Tintenverbrauch, ausreichend starke Linien in Graustufen, beschreibbare Arbeitsflächen und eine verständliche Duplex-Seitenfolge bieten. Vollflächig dunkle Seiten und große Farbflächen ohne Funktion sind nicht zulässig.

Das Dokument bleibt A4, MUSS aber auf kleinen Bildschirmen nutzbar sein: keine unnötig kleinen Texte oder sehr breiten Tabellen, kurze Abschnitte, klare Kapitelorientierung und keine Information nur am äußeren Rand. Ein PDF ersetzt keine responsive Website. Inhalte, die auf einem Smartphone dauerhaft unbrauchbar wären, MÜSSEN später zusätzlich als HTML-Lösung geprüft werden.

Bilder DÜRFEN nur eingesetzt werden, wenn sie funktionalen Informationswert haben und eine reale Situation, Tabelle oder Handlung unterstützen. Icons KÖNNEN Information, Warnung, Blocker, Aufgabe, Quelle oder Ergebnis markieren, MÜSSEN aber eine Textbedeutung erhalten. Gemischte Iconstile sowie KI-typische oder dekorativ überladene Symbole sind nicht zulässig.

## Kontrollierte Vorbereitung für spätere Maschinenlesbarkeit

Diese Phase erzeugt keine JSON-Datei. Für die spätere Übernahme sind ausschließlich vorgesehen: `page_format`, `orientation`, `margin_tokens`, `spacing_tokens`, `visual_hierarchy`, `typography_roles`, `color_roles`, `module_types`, `field_types`, `status_styles`, `table_rules`, `checklist_rules`, `page_break_rules`, `print_requirements`, `screen_requirements` und `product_visual_profiles`.

## Visuelle Abnahmekriterien

Vor Template-Produktion müssen Hauptformat, Seitenränder, Raster, Hierarchie, Typografierollen, Mindestschriftgrößen, Farbrollen, Hinweis-/Warnungs-/Blocker-Bedeutung, Tabellen, Checklisten, Eingabefelder, Seitenumbrüche, Cover, Kopf- und Fußzeile, Druckregeln, Smartphone-Grenzen, C01-C07-Profile und C08-Abgrenzung geprüft werden.

Jede Prüfung erhält genau `PASS`, `FAIL` oder `NOT_APPLICABLE`. Ein `FAIL` blockiert den Übergang zur Template-Produktion.

Dieser Standard ist ein Dokumentationsartefakt. Er erzeugt keine PDF-Datei, keine Designvorlage, keine Website- oder Datenverarbeitungsänderung und keine Auslieferungslogik.