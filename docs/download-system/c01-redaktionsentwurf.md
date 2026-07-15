# C01 – Budget- und Sicherheitsarbeitsblatt

## Dokumentstatus

Entwurf für C01, Phase `C01_G2_CANDIDATE`. G2 ist noch nicht erteilt. Das Arbeitsblatt liefert eine strukturierte Orientierung aus eigenen Angaben und Nachweisen; es ist keine Umzugs-, Finanz-, Rechts- oder Behördenfreigabe.

Kanonischer Versionsstand:

- Content-Contract: `1.3.0`
- Berechnungsregeln: `1.3.0`
- Daten-Schema: `1.2.0`
- Kategorie-Taxonomie: `1.0.1`

## M01 – Einführung

### Zweck und Hauptaufgabe

C01 ordnet persönliche Einnahmen, notwendige und optionale Kosten, einmalige Startkosten sowie Rücklagen in drei nachvollziehbaren Szenarien. Das konkrete Arbeitsergebnis ist eine dokumentierte, vorläufige Budgetübersicht mit offenen Nachweisen und nächsten Prüfschritten.

### Zielgruppe und Grenze

C01 ist für Personen gedacht, die ihre eigenen Unterlagen für eine sachliche Budgetorientierung zusammentragen. Nicht gedacht ist C01 für eine verbindliche Entscheidung über Umzug, Aufenthaltsrecht, Steuer, Finanzierung, Förderung oder behördliche Zulässigkeit. Es gibt keine Erfolgsgarantie.

## M02 – Anleitung

1. Bereite die benötigten Unterlagen vor: Einkommensnachweise, Verträge, Reserve mit Stichtag, Miet- und Nebenkostenunterlagen, Energie-, Versicherungs-, Mobilitäts- und Kommunikationsunterlagen sowie einmalige Start- und Gebührennachweise.
2. Trage jede Position mit Betrag, Währung, Zeitraum, Zuverlässigkeit, Nachweisstatus und einer kurzen Notiz ein.
3. Verwende die verständlichen Zeiträume monatlich (MONTHLY), jährlich (ANNUAL), wöchentlich (WEEKLY), einmalig oder Szenario (SCENARIO).
4. Prüfe die drei Fälle: Normalfall (NORMAL), Stressfall (STRESS) und Mindestfall (MINIMUM).
5. Lies Ergebnis, Warnungen und offene Bedingungen und kläre fehlende Nachweise separat.

Die Grundausfüllung dauert etwa 45–90 Minuten, wenn die wichtigsten Unterlagen vorliegen. Fehlende Nachweise werden anschließend separat geklärt. Dies ist nur eine Bearbeitungsorientierung.

## M03 – Eingaben

| Einnahme | Betrag | Zeitraum | Zuverlässigkeit | Nachweisstatus |
| --- | ---: | --- | --- | --- |
| regelmäßige Arbeitseinnahme | EUR | monatlich (MONTHLY) | regelmäßig bestätigt (VERIFIED_REGULAR) | GEKLÄRT |
| weitere Einnahme | EUR | jährlich (ANNUAL) | geschätzt (ESTIMATED) | OFFEN |

Für jede Position sind Betrag, Währung, Zeitraum, Datenart, Nachweisstatus, Zuverlässigkeit, Pflichtstatus und Quellenhinweis zu dokumentieren. Sichtbare Statuswerte sind ausschließlich: `GEKLÄRT`, `TEILWEISE_GEKLÄRT`, `OFFEN`, `OFFIZIELL_ZU_PRÜFEN`, `FACHLICH_ZU_PRÜFEN`, `AKTUELL_NICHT_TRAGFÄHIG`.

Nichtanwendbarkeit ist kein Status. Die Darstellung lautet: Status: `GEKLÄRT`; Nicht anwendbar: ja; Begründung: konkrete Begründung.

## M04 – Hauptarbeitsbereich

| Kostenart | Betrag | Zeitraum | Einordnung |
| --- | ---: | --- | --- |
| notwendige Kosten | EUR | monatlich (MONTHLY) | Pflichtposition |
| optionale Kosten | EUR | monatlich (MONTHLY) | freiwillige Position |
| Erstmonatskosten (FIRST_MONTH_COSTS) | EUR | einmalig | Überschneidung geprüft |

Technische Kennungen erscheinen nur ergänzend nach einer verständlichen deutschen Bezeichnung. `verlässliche Monatseinnahmen (MONTHLY_INCOME_TOTAL)` werden getrennt von gemeldeten, aber noch nicht regelmäßig bestätigten Einnahmen ausgewiesen.

## M05 – Checkliste

- [ ] Unterlagen für Einnahmen zusammengestellt – Status: OFFEN
- [ ] Wohn- und Versorgungskosten geprüft – Status: OFFEN
- [ ] notwendige und optionale Kosten getrennt – Status: OFFEN
- [ ] Normalfall, Stressfall und Mindestfall nachvollziehbar beschrieben – Status: OFFEN
- [ ] fehlende Nachweise mit konkreter Folgehandlung versehen – Status: OFFEN

Für ein nicht anwendbares Element wird der kontrollierte Status `GEKLÄRT`, das Merkmal „Nicht anwendbar: ja“ und eine konkrete Begründung geführt.

## M06 – Hinweis

### HINWEIS

Eigene Nachweise und eigene Angaben bleiben die Grundlage. Externe Quellen liefern nur methodischen oder rechtlichen Kontext und ersetzen keine persönliche Prüfung.

## M07 – Warnung

### WARNUNG

Risiko: Eine Einnahme ist nur geschätzt (ESTIMATED) oder nicht regelmäßig bestätigt. Bedeutung: Der Monatssaldo kann sich ändern. Nächster Prüfschritt: den passenden Nachweis beschaffen und den Status aktualisieren.

## M08 – Blocker

### BLOCKER

Blockierende Bedingung: Eine notwendige Kostenposition oder ein Pflichtnachweis fehlt. Zwingende Folgehandlung: Wert oder Nachweis ergänzen, oder die Nichtanwendbarkeit mit Begründung und Status `GEKLÄRT` dokumentieren.

## M09 – Ergebnis- und Statusbereich

Ergebnisse enthalten zusammengefasste Eingaben, Wert, Einheit, kontrollierten Status, Begründung, offene Bedingungen, Warnsignale und Prüfstand. `OFFEN` bleibt sichtbar, wenn Angaben fehlen oder nicht belastbar sind. Ein interner Maschinenstatus `INCOMPLETE` wird nicht als sichtbarer Ergebnisstatus ausgegeben.

Die verlässlichen Monatseinnahmen (MONTHLY_INCOME_TOTAL), notwendige und optionale Monatskosten, der Monatssaldo, einmalige Startkosten, Rücklagenreichweite, Startkapitalbedarf und die drei Szenarien werden getrennt ausgewiesen. Es gibt keine zusammenfassende Freigabeentscheidung.

## M10 – Nächster Schritt

1. Fehlende Pflichtunterlagen beschaffen.
2. Geschätzte Angaben gegen Nachweise prüfen.
3. Offene Bedingungen fachlich oder offiziell prüfen lassen.

## M11 – Quellen und Disclaimer

Externe Referenzen werden als Methodik- oder Kontextquelle geführt. Jede Quelle besitzt Herausgeber, Funktion, Quellenstand, Prüfdatum, betroffene Abschnitte und Prüfstatus. Es werden keine externen Zahlenwerte in die persönliche Berechnung übernommen.

C01 ist eine neutrale Orientierungshilfe. Es werden keine Steuer-, Rechts-, Förder-, Finanzierungs- oder Behördenentscheidungen getroffen und keine Sicherheit oder Eignung zugesagt.

## M12 – Metadaten

- Produkt-/Test-ID: `IMR-DL-C01`
- Dokumentversion: `1.3.0`
- Dokumentklasse: `ORIENTATION_WORKSHEET`
- Risikoklasse: `R2_DECISION_SUPPORT`
- Aktualitätsklasse: `U2_MOVING`
- Quellenstand: `2026-07-15`
- Berechnungsregeln: `1.3.0`
- Daten-Schema: `1.2.0`
- Kategorie-Taxonomie: `1.0.1`
- Content-Contract: `1.3.0`

## Zehnteilige Mindestanatomie

1. **Deckblatt:** C01-Titel, Produktkennung und Dokumentzweck.
2. **Dokumentstatus und Transparenz:** Entwurfsstatus, G2-Grenze und keine Freigabeaussage.
3. **Nutzen und Zielgruppe:** konkrete Budgetorientierung für Personen mit eigenen Unterlagen.
4. **Vorbereitung:** erforderliche Nachweisarten und unverbindliche Bearbeitungsorientierung.
5. **Kurzanleitung:** nummerierte Schritte mit nachvollziehbarem Abschluss.
6. **Hauptarbeitsbereich:** Einnahmen, notwendige und optionale Kosten, Startkosten und Szenarien.
7. **Ergebnis- und Statusbereich:** Werte, Einheiten, Status, Begründung und offene Bedingungen.
8. **Warnsignale und Grenzen:** Warnungen, Blocker und fachliche Grenzen.
9. **Nächste Schritte:** priorisierte Folgehandlungen.
10. **Quellen, Disclaimer und Versionsinformation:** Quellenstand, Disclaimer und kanonische Versionen.
