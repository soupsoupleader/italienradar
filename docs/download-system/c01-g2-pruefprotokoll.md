# C01 G2-Prüfprotokoll

Phase: `C01_G2_CANDIDATE`
Status: `CONTENT_IN_PROGRESS`
Entscheidung: `G2_NOT_YET_GRANTED`

## Prüffälle

| Test-ID | Ergebnis | Evidenz | Feststellung | Offene Punkte | Rolle |
| --- | --- | --- | --- | --- | --- |
| QA-CONTENT-001 | OPEN | M01–M12-Redaktionsentwurf | Nutzerziel, Grenzen und Bearbeitungsfolge sind formuliert. | Fachliche Redaktion und Nutzerreview ausführen. | content-reviewer |
| QA-CONTENT-002 | OPEN | Draft, Kategorien, Checkliste | Eingaben, Statuswerte und Szenarien sind strukturiert. | Vollständigkeit mit finalem Fachinhalt prüfen. | content-reviewer |
| QA-BOUNDARY-001 | OPEN | Contract forbidden_content, Release Controls | Steuer-, Förder-, Standort- und Freigabelogik bleiben ausgeschlossen. | Produktreview auf Grenzfälle durchführen. | boundary-reviewer |
| QA-CONTENT-003 | OPEN | Redaktionsentwurf M01–M12 | Nutzertext erklärt Unterlagen, Perioden, Szenarien und Warnungen. | Verständlichkeit mit unabhängiger Person prüfen. | content-reviewer |
| QA-SOURCE-001 | OPEN | Quellenstrategie und Quellenmatrix | Quellenfunktionen sind auf Methodik und Kontext begrenzt; Nutzerbelege sind getrennt. | Quellenabdeckung je späterem Wert vervollständigen. | source-reviewer |
| QA-SOURCE-002 | PASS | Drei externe Matrixeinträge, jeweils check_date und U2_MOVING | Jede verwendete externe Referenz hat Prüfdatum und kontrollierte Aktualitätsklasse; es werden keine externen Zahlenwerte verwendet. | Bei neuen Quellen erneut prüfen. | source-reviewer |

## G2-Grenze

`QA-SOURCE-002` ist der einzige PASS in diesem Protokoll, weil er auf den tatsächlich geprüften Matrixfeldern beruht. Die offenen Fälle sind keine simulierten PASS-Werte. `G2_PASSED`, `G3_PASSED` und `READY_TO_PUBLISH` werden nicht behauptet.

Die Assistive-Tech-Abnahme bleibt unabhängig blockiert. PDF-Build, öffentliche Veröffentlichung, Websiteintegration und Deployment bleiben gesperrt.
