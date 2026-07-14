# Phase 3.2.1.1 - Integrationsbericht

## Zweck und Quelle

Dieser Bericht dokumentiert die Übernahme der unabhängig geprüften Projektleitungsfassung in die kanonischen Dateien. Maßgebliche Quellen waren zum Integrationszeitpunkt die Dateien `phase-3-2-1-1-download-bedarfsmatrix-geprueft.md` und `phase-3-2-1-1-download-bedarfsmatrix-geprueft.json` im Repository-Stamm.

Die vorherigen lokalen Entwürfe wurden nach erfolgreicher Übernahme entfernt. Sie liefern keine Inhalte für die kanonische Fassung, weil die geprüfte Projektleitungsfassung die Source of Truth ist.

## Abweichungen - Markdown

- Der dynamische Kandidat `D01` wird durch die klarer abgegrenzte Familie `C08` ersetzt.
- `C03` wechselt von `FREE_DIRECT` zu `LEAD_LATER`. In der ersten Produktionswelle bleibt der Kandidat ohne E-Mail-Erhebung, weil eine Lead-Architektur noch nicht implementiert ist.
- `C07` wechselt von `HOLD` zu `LEAD_LATER`; die erforderliche Quellenpflege und fachliche Freigabe bleiben als Voraussetzung dokumentiert.
- Die Portfolio-Scores, Umfänge, Sensitivitätsbewertungen und Seitenwerte wurden durchgängig neu bewertet.
- Die Kandidatentitel wurden präzisiert, unter anderem für `C02`, `C04`, `C06`, `C07` und `C08`.
- Die geprüfte Fassung strukturiert alle 26 Seiten als vollständige Profile und erläutert die sieben statischen Kandidaten sowie die dynamische Ergebnisprotokoll-Familie detaillierter.
- Rein sprachliche Unterschiede betreffen hauptsächlich Projektbezeichnung, Überschriften, Funktionsbezeichnungen und präzisere Nutzeraufgaben. Sie ändern keine Produktionsdatei.

## Abweichungen - JSON

- Der Kandidatenbestand bleibt bei acht Einträgen, aber `D01` wird durch `C08` ersetzt.
- Die geprüfte Fassung hat die Entscheidungsverteilung `NONE=6`, `MERGE=7`, `FREE_DIRECT=4`, `LEAD_LATER=3` und `DYNAMIC_LATER=6`; der alte Entwurf enthielt zusätzlich `HOLD=1`, dafür nur `LEAD_LATER=1` und `FREE_DIRECT=5`.
- Geänderte Seitenentscheidungen: `/online-einkommen-in-italien-aufbauen` von `FREE_DIRECT` zu `LEAD_LATER` und `/resto-al-sud-2-deutsche-italien` von `HOLD` zu `LEAD_LATER`.
- Alle sechs Toolseiten behalten `DYNAMIC_LATER`, werden aber von `D01` auf `C08` umgestellt.
- Die Welle-1-Auswahl bleibt unverändert: `C01`, `C03`, `C05`.
- Die geprüfte Fassung verwendet präzisere Feldnamen: `nr`, `existing_function`, `added_value` und `target_group` auf Seitenebene sowie `download_components`, `lead_components`, `problem`, `sources_needed` und `content_modules` auf Kandidatenebene.
- Nicht übernommene ältere Feldnamen sind `number`, `existing_features`, `working_title`, `additional_value`, `primary_target_group`, `score_components`, `user_stage`, `user_problem`, `required_sources` und `required_elements`.
- Download- und Lead-Scores wurden neu bewertet. Die geprüften Komponenten reproduzieren sämtliche acht Download- und Lead-Gesamtwerte.

## Ergebnis

Die geprüften Markdown- und JSON-Fassungen stimmen bei Kandidaten, Titeln, Auslieferungsmodellen, Scores, Aktualitätsklassen, Prioritäten, Welle-1-Auswahl und Seitenentscheidungen überein. Ältere Inhalte wurden nicht stillschweigend übernommen.