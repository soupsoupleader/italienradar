# C01 Quellenstrategie

Status: `C01_G2_CANDIDATE`; G2 ist noch nicht erteilt.

## Grundsatz

C01 ist primär ein Nutzereingabe-Arbeitsblatt. Persönliche Beträge kommen aus individuellen Nachweisen oder direkten Nutzereingaben. Externe Quellen ersetzen diese Angaben nicht.

Externe Referenzen werden nur als `METHOD_REFERENCE` oder `CONTEXT_ONLY` verwendet. Die aktuelle Matrix enthält keine verwendbaren externen Zahlenwerte. Regionale oder haushaltsabhängige Beträge werden nicht zu einem allgemeinen Italienwert verdichtet.

## Quellenpriorität

1. offizielle Primärquelle
2. offizielle Statistik
3. regulierter Anbieter oder örtlicher öffentlicher Betreiber
4. dokumentierte, regionale und datierte Marktbeobachtung

Ungeprüfte Blogs, Affiliate-Seiten, KI-Zusammenfassungen, undatierte Durchschnittswerte, Social-Media-Behauptungen und Artikelwerte ohne Ursprungsquelle sind ausgeschlossen.

## Verwendete externe Referenzen

- Eurostat HICP-Methodik: methodischer Kontext für Preiszeitraum und Quellenstand, nicht für persönliche Beträge.
- Your Europe, Dokumente und Formalitäten: Kontext für die spätere Prüfung von Unterlagen bei einem Aufenthalt in einem anderen EU-Land.
- Your Europe, Working abroad: Kontext für die spätere Prüfung von Arbeit, Versicherung und länderübergreifenden Bedingungen.

Alle drei Einträge haben einen kontrollierten Quellenstand, ein Prüfdatum und `U2_MOVING`. Die Detailfelder stehen in `c01-source-matrix.json`.

## Persönliche Nachweise

Vorgesehen sind Einkommensnachweise, Arbeits- oder Auftragsverträge, ein Reservebestand mit Stichtag, konkrete Mietunterlagen, Nebenkosten- und Energietarife, Versicherungsunterlagen, Mobilitäts- und Kommunikationsverträge, Nachweise vertraglicher Verpflichtungen sowie konkrete Umzugs-, Kautions- und Gebührennachweise.

Es werden keine Dokumentkopien, Namen, Adressen, Kontoangaben, Vertragsnummern oder Beispielpersonen im Repository gespeichert. Fehlt ein Nachweis, bleibt die Position offen oder wird als unsicher gekennzeichnet.

## Regeln für spätere Zahlen

Ein späterer Orientierungswert benötigt Aussage, Wert, Einheit, Zeitraum, Region, Quellentyp, Herausgeber, Titel, Quellenreferenz, Veröffentlichungsdatum, Prüfdatum, Aktualitätsklasse, Evidenzstatus, zulässige Nutzung, betroffene Kategorien und Notiz. Ohne konkrete Quelle und Prüfdatum wird kein Wert in eine Berechnung übernommen.
