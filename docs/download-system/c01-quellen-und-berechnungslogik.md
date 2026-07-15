# C01 Quellen- und Berechnungslogik

Status: `C01_CONTENT_CORE`; kein PDF-Build und keine Veröffentlichung zulässig.

Vertrag: Portfolio-ID `C01`; Produkt-ID `IMR-DL-C01`; Titel **Italien-Neustart: Budget- und Sicherheitsarbeitsblatt**; Dokumentklasse `B`; Portfolioebene `H1`; Auslieferung `FREE_DIRECT`; Aktualitätsklasse `U2_MOVING`; Risikoklasse `R2_MODERATE`; Zielumfang 8–12 Seiten. Content-Contract `1.1.0`; Berechnungsregeln `1.1.0`; Daten-Schema `1.0.0`; Kategorie-Taxonomie `1.0.0`.

## Datenklassen

Nutzereingaben werden mit `NUTZEREINGABE` gekennzeichnet. Interne Formeln erzeugen `BERECHNETES_ERGEBNIS`. Redaktionelle Orientierungswerte sind `ORIENTIERUNGSWERT`; redaktionelle Einordnung ist `REDAKTIONELLE_EINORDNUNG`. Nicht belegte Angaben bleiben `OFFEN_ZU_PRÜFEN`. Nachweisstatus sind `GEKLÄRT`, `TEILWEISE_GEKLÄRT`, `OFFEN`, `OFFIZIELL_ZU_PRÜFEN`, `FACHLICH_ZU_PRÜFEN` und `AKTUELL_NICHT_TRAGFÄHIG`.

## Berechnungen

Alle Beträge sind EUR; Monatswerte und Einmalwerte werden niemals vermischt. Jeder Wert trägt Einheit, Zeitraum und Zuverlässigkeitsstatus.

| Ergebnis | Formel |
| --- | --- |
| `MONTHLY_INCOME_TOTAL` | Summe aller als monatlich und verlässlich markierten Einnahmen |
| `ESSENTIAL_MONTHLY_COSTS` | Summe aller notwendigen monatlichen Ausgaben |
| `OPTIONAL_MONTHLY_COSTS` | Summe aller nicht zwingenden monatlichen Ausgaben |
| `MONTHLY_COSTS_TOTAL` | `ESSENTIAL_MONTHLY_COSTS + OPTIONAL_MONTHLY_COSTS` |
| `MONTHLY_BALANCE` | `MONTHLY_INCOME_TOTAL - MONTHLY_COSTS_TOTAL` |
| `ONE_TIME_START_COSTS` | Summe aller einmaligen Startkosten |
| `LIQUID_RESERVE` | Nutzereingabe der verfügbaren Liquiditätsreserve zum sichtbaren Stichtag |
| `RESERVE_COVERAGE_MONTHS` | `LIQUID_RESERVE / ESSENTIAL_MONTHLY_COSTS` |
| `FIRST_MONTH_COSTS` | Nutzereingabe der dem ersten Monat zugeordneten Kosten |
| `STRESS_MONTH_INCOME` | Nutzereingabe der Einnahmen im Stressszenario |
| `STRESS_MONTH_COSTS` | Nutzereingabe der Kosten im Stressszenario |
| `STRESS_MONTH_BALANCE` | `STRESS_MONTH_INCOME - STRESS_MONTH_COSTS` |
| `MINIMUM_CASE_INCOME` | Nutzereingabe der Einnahmen im Mindestfall |
| `MINIMUM_CASE_COSTS` | Nutzereingabe der Kosten im Mindestfall |
| `MINIMUM_CASE_BALANCE` | `MINIMUM_CASE_INCOME - MINIMUM_CASE_COSTS` |
| `USER_DEFINED_RESERVE_TARGET` | Nutzereingabe des selbst gesetzten Rücklagenziels |
| `START_CAPITAL_NEED` | `ONE_TIME_START_COSTS + FIRST_MONTH_COSTS + USER_DEFINED_RESERVE_TARGET` |

Bei einer Division durch null beziehungsweise einem Nenner von null wird `OFFEN_ZU_PRÜFEN` ausgegeben. Es gibt keine automatisch erfundene Sicherheitsschwelle und keinen universellen Mindestbetrag. Es wird nicht versteckt gerundet; Rundung wird erst bei der Darstellung mit dokumentierter Präzision vorgenommen. Normalmonat, Stressmonat und Mindestfall sind getrennte, sichtbare Szenarien.

## Quellenmodell

Nutzereingaben werden nicht als offizielle Quelle ausgegeben. Interne Berechnungen sind reproduzierbar und nicht als Behörden-, Steuer- oder Finanzentscheidung zu formulieren. Redaktionelle Orientierungswerte dürfen erst nach Prüfung aufgenommen werden. Für jeden solchen Wert sind Aussage, Wert, Einheit, Zeitraum, Region, Quellentyp, Quellenstand, Prüfdatum, Aktualitätsklasse und Status zu dokumentieren.

Offizielle Grundlagen und noch offene Quellen werden getrennt geführt. Die vorhandenen Projektrouten `/was-kostet-ein-neustart-in-italien`, `/mit-1000-euro-in-italien-leben`, `/italien-neustart-ohne-job` und `/italien-kostenrechner` sind nur Inhaltsinventar. Artikeltexte oder ungeprüfte Zahlen werden nicht übernommen.

## Signale und Grenzen

Eine Warnung entsteht bei unsicherer Einnahme, unbekannter Kostenposition oder zu geringer Datenbasis. Ein Blocker entsteht bei fehlenden notwendigen Kosten, negativem Mindestfallszenario oder nicht belastbar belegter Haupteinnahme. Farben und Symbole dürfen niemals die alleinige Bedeutung tragen.

Jede Warnung enthält Risiko, Bedeutung und nächsten Prüfschritt. Jeder Blocker nennt Zustand, Bedeutung und zwingende Folgehandlung. Ein Blocker ist keine Behördenentscheidung und keine allgemeine Aussage, dass ein Umzug unmöglich sei.

Berechnungsergebnisse sind keine Umzugsfreigabe, keine individuelle Finanzberatung und keine Erfolgsgarantie. Steuer-, Partita-IVA-, Förder- und Standortlogik gehören nicht zu C01. Produkt-QA, Quellenprüfung, Systemabnahme einschließlich praktischem Assistive-Tech-Nachweis sowie ein späterer kontrollierter PDF-Build bleiben offen.
