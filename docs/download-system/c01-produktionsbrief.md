# C01 Produktionsbrief

Status: `C01_G2_CANDIDATE`; Content-Contract `1.2.1`; Berechnungsregeln `1.2.1`; Daten-Schema `1.1.0`; Kategorie-Taxonomie `1.0.1`. G2 ist noch nicht erteilt.

## Produktvertrag

- Portfolio-ID: `C01`
- Produkt-ID: `IMR-DL-C01`
- Titel: **Italien-Neustart: Budget- und Sicherheitsarbeitsblatt**
- Dokumentklasse: `B`
- Portfolioebene: `H1`
- Auslieferungsmodell: `FREE_DIRECT`
- Aktualitätsklasse: `U2_MOVING`
- Risikoklasse: `R2_MODERATE`
- Zielumfang: 8–12 Seiten

## Aufgabe und Nutzergrenze

Das Arbeitsblatt unterstützt Menschen dabei, Monatsbudget, einmalige Startkosten, Rücklage und finanzielle Stressmonate für einen Italien-Neustart nachvollziehbar zu erfassen und rechnerisch zu prüfen. Es liefert Rechenwerte und offene Prüfbedingungen, aber keine Umzugsfreigabe und keine individuelle Finanzberatung.

Die Zielgruppe sind Personen, die Kosten, Startpuffer und Risikomonate vor einer persönlichen Entscheidung strukturiert vorbereiten möchten. Der konkrete Arbeitsnutzen besteht in einer prüfbaren Trennung von Einnahmen, notwendigen und optionalen Kosten, Einmalkosten, Szenarien und Nachweisen.

Das Nutzerproblem ist, dass laufende Kosten, einmalige Startkosten, unsichere Einnahmen und Rücklagen häufig nicht in einer gemeinsamen, nachvollziehbaren Betrachtung vorliegen.

Enthalten sind Monatsbudget, Startkosten, Rücklagen, verlässliche Einnahmen, Mindest-Einkommensgrenze als nutzerdefinierte Vergleichsgröße, Normalmonat, Stressmonat, Mindestfall, Kostenrechner-Abgleich, offene Kostenpositionen und nächste Prüfschritte.

Ausgeschlossen sind Steuerberechnung, Partita-IVA-Prüfung, Förderlogik, Standortbewertung, individuelle Finanzberatung, Erfolgsgarantien, universelle Mindestbeträge und eine scheinbar verbindliche Umzugsfreigabe.

## Komponenten- und Datenplanung

| Komponente | C01-Zweck |
| --- | --- |
| M01 | Ziel, Nutzung und Grenzen des Arbeitsblatts |
| M02 | Bearbeitungsreihenfolge und benötigte Unterlagen |
| M03 | Einnahmen, Monatskosten, Startkosten und Rücklagen |
| M04 | Monatsbudget, Startkosten und Szenarien |
| M05 | Vollständigkeit und Nachweisstatus |
| M06 | Unterschied zwischen Schätzung und bestätigtem Wert |
| M07 | Unsichere Einnahmen, unbekannte Kosten oder zu geringe Datenbasis |
| M08 | Fehlende notwendige Kosten, negatives Mindestfallszenario oder nicht belegte Haupteinnahme |
| M09 | Normalmonat, Stressmonat, Mindestfall, Rücklagenreichweite und offene Bedingungen |
| M10 | Priorisierte Nachweise und Korrekturen |
| M11 | Grundlagen, Orientierungswerte und Prüfstand |
| M12 | Produkt-ID, Version, Klasse, Risiko, Aktualität und Quellenstand |

Benötigte Nutzereingaben werden als `NUTZEREINGABE` und mit Zeitraum, Einheit und Nachweisstatus erfasst. Berechnete Ergebnisse werden als `BERECHNETES_ERGEBNIS` gekennzeichnet. Orientierung und redaktionelle Einordnung bleiben von Nutzereingaben getrennt.

## Berechnete Ergebnisse und Signale

Der Draft sieht Monats-Einnahmen und -Kosten, Einmalkosten, Liquiditätsreserve, Reserve-Reichweite, Normal-, Stress- und Mindestfall sowie den Startkapitalbedarf vor. Division durch null ergibt `OFFEN_ZU_PRÜFEN` und niemals eine künstliche Sicherheit.

Warnungen markieren unsichere Einnahmen, unbekannte Kosten oder eine zu geringe Datenbasis. Blocker markieren fehlende notwendige Kosten, ein negatives Mindestfallszenario oder eine nicht belastbar belegte Haupteinnahme. Kein Signal ist ausschließlich farb- oder symbolabhängig.

## Freigabeabhängigkeiten und Nicht-Ziele

`release_eligible = false`, `publication_status = CONTENT_IN_PROGRESS`, `pdf_build_allowed = false`, `public_pdf_allowed = false`, `website_integration_allowed = false` und `deployment = false`. Der Assistive-Tech-Gate bleibt erforderlich; Systemabnahme und Produktfreigaben sind nicht erteilt.

Quellen werden erst nach Prüfung mit Aussage, Wert, Einheit, Zeitraum, Region, Quellentyp, Quellenstand, Prüfdatum, Aktualitätsklasse und Status übernommen. Vorhandene Projektrouten dienen nur als Inhaltsinventar; Artikeltexte werden nicht kopiert.

Offen für die nächste Phase sind redaktionelle Ausarbeitung, Quellenprüfung, Produkt-QA, Systemfreigabe einschließlich Assistive-Tech-Nachweis, Mastertemplate-Bindung und ein später separat freizugebender PDF-Build.
