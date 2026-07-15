#!/usr/bin/env python3
"""Forty-five executable regression tests for calculate_c01.py."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_c01 import C01ValidationError, calculate  # noqa: E402

ESSENTIAL=["COST_HOUSING_RENT","COST_HOUSING_SERVICE_CHARGES","COST_ELECTRICITY","COST_GAS_OR_HEATING","COST_WATER","COST_FOOD_BASIC","COST_HEALTH_AND_INSURANCE","COST_TRANSPORT_REQUIRED","COST_INTERNET","COST_MOBILE","COST_CONTRACTUAL_OBLIGATIONS","COST_OTHER_ESSENTIAL"]
VISIBLE_STATUSES={"GEKLÄRT","TEILWEISE_GEKLÄRT","OFFEN","OFFIZIELL_ZU_PRÜFEN","FACHLICH_ZU_PRÜFEN","AKTUELL_NICHT_TRAGFÄHIG"}


def item(identifier, category, amount=None, *, period="MONTHLY", reliability="UNKNOWN", not_relevant=False, evidence="GEKLÄRT"):
    return {"id":identifier,"category_id":category,"label":category,"amount":amount,"currency":"EUR","period":period,"data_type":"NUTZEREINGABE","evidence_status":"GEKLÄRT" if not_relevant else evidence,"reliability_status":reliability,"required_for_result":True,"not_relevant":not_relevant,"not_relevant_reason":"Für diesen Test nicht relevant." if not_relevant else None,"source_ref":None,"note":None}


def base():
    return {"portfolio_id":"C01","canonical_product_id":"IMR-DL-C01","income_items":[item("income-1","INCOME_EMPLOYMENT","100",reliability="VERIFIED_REGULAR")],"essential_cost_items":[item(f"essential-{i}",category,None,not_relevant=True) for i,category in enumerate(ESSENTIAL)],"optional_cost_items":[],"start_cost_items":[],"reserve":{"amount":None,"as_of_date":None,"currency":"EUR"},"first_month_costs":{"amount":None,"currency":"EUR","scope":"RECURRING_FIRST_MONTH_ONLY","overlap_with_start_costs_checked":False,"evidence_status":"OFFEN","note":None},"user_defined_reserve_target":None,"normal_scenario":{},"stress_scenario":{},"minimum_scenario":{}}


def result(output, identifier):
    return next(x for x in output["results"] if x["id"]==identifier)


class C01CalculationTests(unittest.TestCase):
    def test_01_positive_monthly_balance(self):
        data=base(); data["essential_cost_items"][0]=item("rent","COST_HOUSING_RENT","40"); self.assertEqual(result(calculate(data),"MONTHLY_BALANCE")["value"],"60.00")
    def test_02_negative_monthly_balance(self):
        data=base(); data["essential_cost_items"][0]=item("rent","COST_HOUSING_RENT","140"); self.assertEqual(result(calculate(data),"MONTHLY_BALANCE")["value"],"-40.00")
    def test_03_annual_to_monthly_normalization(self):
        data=base(); data["income_items"][0].update(amount="1200",period="ANNUAL"); self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"100.00")
    def test_04_weekly_to_monthly_normalization(self):
        data=base(); data["income_items"][0].update(amount="12",period="WEEKLY"); self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"52.00")
    def test_05_one_time_monthly_separation(self):
        data=base(); data["start_cost_items"]=[item("move","START_MOVING","500",period="ONE_TIME")]; output=calculate(data); self.assertEqual(result(output,"ONE_TIME_START_COSTS")["value"],"500.00"); self.assertEqual(result(output,"MONTHLY_COSTS_TOTAL")["value"],"0.00")
    def test_06_decimal_precision(self):
        data=base(); data["income_items"]=[item("a","INCOME_EMPLOYMENT","0.10",reliability="VERIFIED_REGULAR"),item("b","INCOME_REGULAR_CONTRACT","0.20",reliability="VERIFIED_REGULAR")]; self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"0.30")
    def test_07_zero_essential_cost_denominator(self):
        data=base(); data["reserve"]={"amount":"10","as_of_date":"test","currency":"EUR"}; self.assertEqual(result(calculate(data),"RESERVE_COVERAGE_MONTHS")["status"],"OFFEN")
    def test_08_missing_required_cost_category(self):
        data=base(); data["essential_cost_items"]=data["essential_cost_items"][1:]; self.assertIn("NECESSARY_COST_POSITION_MISSING",[x["condition"] for x in calculate(data)["blockers"]])
    def test_09_required_category_marked_not_relevant(self):
        self.assertNotIn("NECESSARY_COST_POSITION_MISSING",[x["condition"] for x in calculate(base())["blockers"]])
    def test_10_uncertain_income_separated(self):
        data=base(); data["income_items"].append(item("uncertain","INCOME_IRREGULAR","30",reliability="ESTIMATED")); output=calculate(data); self.assertEqual(result(output,"MONTHLY_INCOME_TOTAL")["value"],"100.00"); self.assertEqual(result(output,"UNCERTAIN_MONTHLY_INCOME")["value"],"30.00")
    def test_11_main_income_not_evidenced_blocker(self):
        data=base(); data["income_items"][0]["reliability_status"]="UNKNOWN"; self.assertIn("MAIN_INCOME_NOT_EVIDENCED",[x["condition"] for x in calculate(data)["blockers"]])
    def test_12_negative_minimum_scenario_blocker(self):
        data=base(); data["minimum_scenario"]={"income_items":[item("mi","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[item("mc","COST_HOUSING_RENT","20",period="SCENARIO")],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}; self.assertIn("MINIMUM_CASE_NEGATIVE",[x["condition"] for x in calculate(data)["blockers"]])
    def test_13_incomplete_stress_scenario(self): self.assertEqual(calculate(base())["scenarios"]["STRESS"]["status"],"OFFEN")
    def test_14_duplicate_item_id_rejected(self):
        data=base(); data["income_items"].append(copy.deepcopy(data["income_items"][0])); self.assertRaises(C01ValidationError,calculate,data)
    def test_15_unknown_category_rejected(self):
        data=base(); data["income_items"][0]["category_id"]="COST_UNKNOWN"; self.assertRaises(C01ValidationError,calculate,data)
    def test_16_negative_user_amount_rejected(self):
        data=base(); data["income_items"][0]["amount"]="-1"; self.assertRaises(C01ValidationError,calculate,data)
    def test_17_wrong_currency_rejected(self):
        data=base(); data["income_items"][0]["currency"]="USD"; self.assertRaises(C01ValidationError,calculate,data)
    def test_18_missing_period_rejected(self):
        data=base(); del data["income_items"][0]["period"]; self.assertRaises(C01ValidationError,calculate,data)
    def test_19_no_relocation_approval_output(self):
        output=json.dumps(calculate(base()),ensure_ascii=False); self.assertTrue(all(x not in output for x in ("SAFE_TO_MOVE","APPROVED","RECOMMENDED","FINANCIALLY_SECURE")))
    def test_20_deterministic_repeated_calculation(self): self.assertEqual(calculate(base()),calculate(copy.deepcopy(base())))
    def test_21_category_taxonomy_contains_exactly_35_categories(self):
        categories=json.loads((Path(__file__).resolve().parents[1]/"manifests/c01-budget-categories.json").read_text(encoding="utf-8"))["categories"]; self.assertEqual(len(categories),35); self.assertNotIn("START_EMERGENCY_BUFFER",[x["id"] for x in categories])
    def test_22_contract_draft_engine_result_id_parity(self):
        root=Path(__file__).resolve().parents[1]; c=json.loads((root/"manifests/c01-content-contract.json").read_text()); d=json.loads((root/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text()); self.assertEqual(c["calculated_results"],list(d["calculated_results"])); self.assertEqual(c["calculated_results"],[x["id"] for x in calculate(base())["results"]])
    def test_23_unknown_scenario_category_rejected(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_UNKNOWN","10",period="SCENARIO")],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}; self.assertRaises(C01ValidationError,calculate,data)
    def test_24_wrong_scenario_currency_rejected(self):
        data=base(); si=item("si","INCOME_EMPLOYMENT","10",period="SCENARIO"); si["currency"]="USD"; data["stress_scenario"]={"income_items":[si],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}; self.assertRaises(C01ValidationError,calculate,data)
    def test_25_incomplete_scenario_missing_cost_remains_open(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}; self.assertEqual(calculate(data)["scenarios"]["STRESS"]["status"],"OFFEN")
    def test_26_scenario_open_evidence_remains_open(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[item("sc","COST_FOOD_BASIC","5",period="SCENARIO")],"assumptions":[],"open_conditions":[],"evidence_status":"OFFEN"}; self.assertEqual(calculate(data)["scenarios"]["STRESS"]["status"],"OFFEN")
    def test_27_duplicate_id_across_base_and_scenario_rejected(self):
        data=base(); data["stress_scenario"]={"income_items":[item("income-1","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}; self.assertRaises(C01ValidationError,calculate,data)
    def test_28_start_emergency_buffer_rejected(self):
        data=base(); data["start_cost_items"]=[item("buffer","START_EMERGENCY_BUFFER","10",period="ONE_TIME")]; self.assertRaises(C01ValidationError,calculate,data)
    def test_29_unchecked_first_month_overlap_keeps_start_capital_open(self):
        data=base(); data["start_cost_items"]=[item("start","START_TRAVEL","100",period="ONE_TIME")]; data["first_month_costs"].update(amount="20"); data["user_defined_reserve_target"]="30"; self.assertIsNone(result(calculate(data),"START_CAPITAL_NEED")["value"])
    def test_30_checked_non_overlapping_first_month_costs_calculate(self):
        data=base(); data["start_cost_items"]=[item("start","START_TRAVEL","100",period="ONE_TIME")]; data["first_month_costs"].update(amount="20",overlap_with_start_costs_checked=True); data["user_defined_reserve_target"]="30"; self.assertEqual(result(calculate(data),"START_CAPITAL_NEED")["value"],"150.00")
    def test_31_calculated_results_and_rules_have_parity(self):
        c=json.loads((Path(__file__).resolve().parents[1]/"manifests/c01-content-contract.json").read_text()); self.assertEqual([x["id"] for x in c["calculation_rules"]],c["calculated_results"])
    def test_32_required_input_contract_is_structured(self):
        c=json.loads((Path(__file__).resolve().parents[1]/"manifests/c01-content-contract.json").read_text()); inputs={x["id"]:x for x in c["required_inputs"]}; self.assertEqual(inputs["first_month_costs"]["type"],"NUTZEREINGABE_OBJECT"); self.assertIn("income_items",inputs["stress_scenario"]["fields"])
    def test_33_every_external_source_has_check_date_and_update_class(self):
        m=json.loads((Path(__file__).resolve().parents[1]/"content/c01-source-matrix.json").read_text()); self.assertTrue(all(x["check_date"] and x["update_class"] for x in m["external_references"]))
    def test_34_no_external_numeric_value_without_source(self):
        m=json.loads((Path(__file__).resolve().parents[1]/"content/c01-source-matrix.json").read_text()); self.assertTrue(all(x.get("value") in (None,"") or x.get("source_reference") for x in m["external_references"]))
    def test_35_no_personal_data_in_user_document_requirements(self):
        text=json.dumps(json.loads((Path(__file__).resolve().parents[1]/"content/c01-source-matrix.json").read_text()),ensure_ascii=False); self.assertNotIn("Max Mustermann",text); self.assertNotIn("@",text)
    def test_36_no_universal_minimum_or_relocation_approval_output(self):
        text=(Path(__file__).resolve().parents[1]/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text(); self.assertTrue(all(x not in text for x in ("SAFE_TO_MOVE","READY_TO_PUBLISH","FINANCIALLY_SECURE","UNIVERSAL_MINIMUM")))
    def test_37_versions_are_parity_across_all_c01_files(self):
        root=Path(__file__).resolve().parents[1]; c=json.loads((root/"manifests/c01-content-contract.json").read_text()); d=json.loads((root/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text()); s=json.loads((root/"manifests/c01-data-schema.json").read_text()); self.assertEqual((c["content_contract_version"],c["calculation_ruleset_version"],c["data_schema_version"],s["schema_version"]),("1.3.0","1.3.0","1.2.0","1.2.0"));
        for path in [root.parent/"docs/download-system/c01-produktionsbrief.md",root.parent/"docs/download-system/c01-quellen-und-berechnungslogik.md",root.parent/"docs/download-system/c01-quellenstrategie.md",root.parent/"docs/download-system/c01-redaktionsentwurf.md"]:
            text=path.read_text(encoding="utf-8"); self.assertIn("1.3.0",text); self.assertIn("1.2.0",text); self.assertIn("1.0.1",text)
        self.assertEqual(d["calculation_ruleset_version"],"1.3.0")
    def test_38_ten_part_anatomy_is_present(self):
        text=(Path(__file__).resolve().parents[2]/"docs/download-system/c01-redaktionsentwurf.md").read_text(encoding="utf-8"); self.assertTrue(all(x in text for x in ["Deckblatt","Dokumentstatus und Transparenz","Nutzen und Zielgruppe","Vorbereitung","Kurzanleitung","Hauptarbeitsbereich","Ergebnis- und Statusbereich","Warnsignale und Grenzen","Nächste Schritte","Quellen, Disclaimer und Versionsinformation"]))
    def test_39_visible_status_values_match_standard(self):
        root=Path(__file__).resolve().parents[1]; c=json.loads((root/"manifests/c01-content-contract.json").read_text(encoding="utf-8")); self.assertEqual(set(c["result_status_values"]),VISIBLE_STATUSES); text=(root.parent/"docs/download-system/c01-redaktionsentwurf.md").read_text(encoding="utf-8"); self.assertNotIn("NICHT_RELEVANT",text); self.assertNotIn("OFFEN_ZU_PRÜFEN",text)
    def test_40_not_relevant_is_not_evidence_status(self):
        schema=json.loads((Path(__file__).resolve().parents[1]/"manifests/c01-data-schema.json").read_text()); self.assertNotIn("NICHT_RELEVANT",schema["item_required_fields"]["evidence_status"]); self.assertTrue(base()["essential_cost_items"][0]["not_relevant"])
    def test_41_visible_results_never_use_incomplete(self):
        statuses=[x["status"] for x in calculate(base())["results"]]; self.assertTrue(set(statuses)<=VISIBLE_STATUSES); self.assertNotIn("INCOMPLETE",statuses)
    def test_42_calculation_reference_matches_ruleset(self):
        d=json.loads((Path(__file__).resolve().parents[1]/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text()); self.assertEqual(d["calculation_reference"],"C01_CALCULATION_RULESET_1.3.0")
    def test_43_external_sources_have_affected_sections(self):
        m=json.loads((Path(__file__).resolve().parents[1]/"content/c01-source-matrix.json").read_text()); self.assertTrue(all(x.get("affected_sections") and x.get("verification_status") for x in m["external_references"]))
    def test_44_eurostat_publication_date_is_not_invented(self):
        m=json.loads((Path(__file__).resolve().parents[1]/"content/c01-source-matrix.json").read_text()); euro=next(x for x in m["external_references"] if x["source_id"]=="EXT-HICP-METHOD-001"); self.assertEqual(euro["publication_date"],"NOT_STATED_BY_PUBLISHER")
    def test_45_visible_tables_use_german_primary_labels(self):
        text=(Path(__file__).resolve().parents[2]/"docs/download-system/c01-redaktionsentwurf.md").read_text(encoding="utf-8"); self.assertIn("notwendige Kosten",text); self.assertIn("optionale Kosten",text); self.assertNotIn("OFFEN_ZU_PRÜFEN",text); self.assertTrue(all(f"{de} ({code})" in text for code,de in {"MONTHLY":"monatlich","ANNUAL":"jährlich","WEEKLY":"wöchentlich","SCENARIO":"Szenario","FIRST_MONTH_COSTS":"Erstmonatskosten","ESTIMATED":"geschätzt","MONTHLY_INCOME_TOTAL":"verlässliche Monatseinnahmen","VERIFIED_REGULAR":"regelmäßig bestätigt"}.items()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
