# C01 – Redaktioneller Entwurf

Produkt: **Italien-Neustart: Budget- und Sicherheitsarbeitsblatt**
Produkt-ID: `IMR-DL-C01` · Klasse `B` · Aktualität `U2_MOVING` · Risiko `R2_MODERATE`
Content-Contract `1.2.0` · Berechnungsregeln `1.2.0` · Daten-Schema `1.1.0` · Kategorie-Taxonomie `1.0.1`
Status: `CONTENT_IN_PROGRESS`; der Text ist kein PDF und keine Freigabe.

## M01 – Einführung

Dieses Arbeitsblatt ordnet persönliche Angaben zu regelmäßigen Einnahmen, notwendigen und optionalen Monatskosten, einmaligen Startkosten und Rücklagen. Es berechnet daraus nachvollziehbare Zwischenstände und stellt Normal-, Stress- und Mindestfall getrennt dar.

Es leistet eine strukturierte Rechenhilfe. Es prüft nicht, ob ein Umzug möglich, sinnvoll oder behördlich zulässig ist. Es ersetzt keine Steuer-, Rechts-, Versicherungs-, Förder- oder Finanzberatung und enthält keine Erfolgsgarantie oder allgemeine Mindestreserve.

Arbeite mit einer eindeutigen Test- oder Produktkennung, einem Stichtag und einem sichtbaren Nachweisstatus. Unbekannte Werte bleiben offen.

## M02 – Anleitung

1. Sammle die Unterlagen, die Einnahmen und Kosten tatsächlich belegen können, und notiere den Prüfstand.
2. Erfasse jede Einnahme einzeln. Kennzeichne, ob sie regelmäßig bestätigt, teilweise bestätigt, geschätzt, unregelmäßig oder unbekannt ist.
3. Erfasse notwendige Monatskosten einzeln und ordne jede Position einer kontrollierten Kategorie, Einheit und Periode zu.
4. Erfasse optionale Monatskosten getrennt von notwendigen Kosten.
5. Erfasse einmalige Startkosten separat. Sie werden nicht in Monatskosten eingerechnet.
6. Trage die Liquiditätsreserve mit sichtbarem Stichtag und das selbst gesetzte Rücklagenziel ein.
7. Fülle Normal-, Stress- und Mindestfall mit ausdrücklich eingegebenen Szenariowerten und Annahmen aus.
8. Prüfe offene Werte, Nachweise, Warnungen und Blocker. Korrigiere zuerst fehlende Pflichtpositionen.

## M03 – Eingaben

Verwende je Feld eine Zeile mit Bezeichnung, Betrag, Währung `EUR`, Zeitraum, Datenrolle, Nachweisstatus, Zuverlässigkeitsstatus und Notiz.

- Einnahme: Bezeichnung, Betrag, `MONTHLY`, `ANNUAL`, `WEEKLY` oder `SCENARIO`, Zuverlässigkeit und Nachweis.
- Notwendige Monatskosten: Miete, Versorgung, Grundnahrung, Gesundheit/Absicherung, notwendige Mobilität, Kommunikation und Verpflichtungen.
- Optionale Monatskosten: Freizeit, Auswärtsessen, Abonnements, optionale Reisen und Anschaffungen.
- Einmalkosten: Anreise, Umzug, Unterkunft zum Start, Kaution, erste Miete, Grundausstattung, Aktivierung, Dokumente und sonstige Startkosten.
- Rücklage: Betrag, Stichtag und Nachweisstatus; sie ist ein Bestandswert und keine Monatskostenposition.
- Szenarien: Einnahmen, Kosten, Annahmen, offene Bedingungen und Evidenzstatus für `NORMAL`, `STRESS` und `MINIMUM`.

## M04 – Tabellenentwürfe

### Einnahmen

| Position | Kategorie | Betrag | Zeitraum | Zuverlässigkeit | Nachweis |
| --- | --- | --- | --- | --- | --- |
| Nutzerzeile | kontrollierte Kategorie | offen | offen | UNKNOWN | OFFEN |

### Monatskosten

| Position | Kostenklasse | Betrag | Zeitraum | notwendig/optional | Status |
| --- | --- | --- | --- | --- | --- |
| Nutzerzeile | ESSENTIAL oder OPTIONAL | offen | offen | sichtbar | OFFEN |

### Startkosten

| Position | Kategorie | Betrag | ONE_TIME | Quelle/Nachweis | Status |
| --- | --- | --- | --- | --- | --- |
| Nutzerzeile | kontrollierte Startkategorie | offen | ONE_TIME | offen | OFFEN |

### Szenarien und Ergebnisse

| Szenario | Einnahmen | Kosten | Saldo | Annahmen | offene Bedingungen |
| --- | --- | --- | --- | --- | --- |
| NORMAL | offen | offen | offen | offen | offen |
| STRESS | offen | offen | offen | offen | offen |
| MINIMUM | offen | offen | offen | offen | offen |

Die Ergebnisübersicht zeigt zusätzlich gemeldete Einnahmen, verlässliche Einnahmen, unsichere Einnahmen, Rücklagenreichweite, Startkapitalbedarf und offene Pflichtwerte. Keine Zeile gibt eine Freigabeentscheidung aus.

## M05 – Checkliste

- [ ] Für jede verwendete Position ist ein Betrag vorhanden oder `NICHT_RELEVANT` begründet.
- [ ] `FIRST_MONTH_COSTS` enthält nur laufende Erstmonatskosten; die Überschneidung mit Einmalkosten ist geprüft.
- [ ] Für jeden Wert ist der Zeitraum vorhanden.
- [ ] Datenrolle und Nachweisstatus sind sichtbar.
- [ ] Ein Nachweis oder die offene Prüfanforderung ist vermerkt.
- [ ] Jede Pflichtkategorie ist geklärt oder begründet nicht relevant.
- [ ] Normal-, Stress- und Mindestfall sind ausgefüllt oder ausdrücklich offen.
- [ ] Offene Kostenpositionen sind markiert und nicht durch Schätzwerte ersetzt.

## M06 – Hinweis

Eine Schätzung ist kein bestätigter Wert. Markiere bestätigte Werte mit ihrem Nachweis und Schätzungen mit `ESTIMATED`. Beide bleiben in der Darstellung unterscheidbar. Ein Orientierungswert braucht Aussage, Wert, Einheit, Zeitraum, Region, Quellentyp, Quellenstand, Prüfdatum, Aktualitätsklasse und Status.

## M07 – Warnung

Eine Warnung wird sichtbar beschriftet. Beispiel: **Risiko:** Eine Einnahme ist nicht als regelmäßig bestätigt. **Bedeutung:** Der ausgewiesene verlässliche Monatswert kann niedriger als der gemeldete Gesamtwert sein. **Nächster Prüfschritt:** Nachweis und Regelmäßigkeit dieser Einnahme prüfen und den Status aktualisieren.

Weitere Warnungen betreffen unbekannte Kostenpositionen, eine zu geringe Datenbasis, einen hohen Anteil unregelmäßiger Einnahmen und ein nicht abgeschlossenes Szenario. Eine Warnung ist keine Entscheidung.

## M08 – Blocker

Ein Blocker wird nur bei einem klaren Zustand ausgelöst. Fehlt eine notwendige Kostenposition, lautet die Folgehandlung: Wert ermitteln oder `NICHT_RELEVANT` mit Begründung dokumentieren. Ist die Haupteinnahme nicht belastbar belegt, lautet die Folgehandlung: Nachweis beschaffen oder die Einnahme als nicht verlässlich behandeln. Ist der Mindestfallsaldo kleiner als null, sind die Annahmen zu prüfen.

Ein Blocker beschreibt eine unvollständige Rechenbasis. Er ist keine Behördenentscheidung und sagt nicht allgemein, dass ein Umzug unmöglich ist.

## M09 – Ergebnis

Zeige `MONTHLY_INCOME_TOTAL` nur aus `VERIFIED_REGULAR` markierten Einnahmen. Zeige gemeldete und unsichere Einnahmen zusätzlich getrennt. Zeige notwendige Monatskosten, optionale Monatskosten, Gesamtkosten, Monatssaldo, einmalige Startkosten, Rücklagenreichweite, Startkapitalbedarf sowie die drei Szenarien.

Jedes Ergebnis trägt Wert, Einheit, Status, verwendete und ausgeschlossene Eingaben sowie eine Erklärung. Bei Division durch null oder fehlenden Szenariowerten bleibt der Status `OFFEN_ZU_PRÜFEN`. Es gibt keine zusammenfassende Freigabeentscheidung.

## M10 – Nächster Schritt

1. Fehlende notwendige Kostenpositionen und Zeiträume ergänzen.
2. Haupteinnahmen und deren Regelmäßigkeit belegen.
3. Einmalige Startkosten mit getrennten Nachweisen prüfen.
4. Stress- und Mindestfall mit ausdrücklich gewählten Nutzerannahmen vervollständigen.
5. Offene Quellenwerte mit Quelle und Prüfdatum nachführen.

## M11 – Quellen

Für jede Quelle werden Quellenart, Herausgeber, Titel oder Funktion, Aussage, Wert, Einheit, Zeitraum, Region, Quellenstand, Prüfdatum, Aktualitätsklasse, Evidenzstatus und Verwendungszweck geführt. Das Inhaltsinventar vorhandener Projektrouten ist keine Primärquelle. Ohne aktuelle, konkrete und prüfbare Quelle bleibt ein Orientierungswert offen.

## M12 – Metadaten

- Produkt-ID: `IMR-DL-C01`
- Dokumentversion: Draft, vor Veröffentlichung
- Dokumentklasse: `B`
- Portfolioebene: `H1`
- Aktualitätsklasse: `U2_MOVING`
- Risikoklasse: `R2_MODERATE`
- Quellenstand: offen bzw. je Quelle dokumentiert
- Berechnungsregelversion: `1.1.0`
- Daten-Schema: `1.0.0`
- Kategorien: `1.0.0`
- Status: `CONTENT_IN_PROGRESS`
- Release: nicht zulässig; PDF-Build, Veröffentlichung, Websiteintegration und Deployment bleiben gesperrt.
