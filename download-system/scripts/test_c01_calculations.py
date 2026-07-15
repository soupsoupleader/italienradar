#!/usr/bin/env python3
"""Forty-five executable regression tests for calculate_c01.py."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from calculate_c01 import C01ValidationError, calculate  # noqa: E402


ESSENTIAL = [
    "COST_HOUSING_RENT", "COST_HOUSING_SERVICE_CHARGES", "COST_ELECTRICITY", "COST_GAS_OR_HEATING", "COST_WATER", "COST_FOOD_BASIC", "COST_HEALTH_AND_INSURANCE", "COST_TRANSPORT_REQUIRED", "COST_INTERNET", "COST_MOBILE", "COST_CONTRACTUAL_OBLIGATIONS", "COST_OTHER_ESSENTIAL"
]


def item(identifier: str, category: str, amount=None, *, period="MONTHLY", reliability="UNKNOWN", not_relevant=False, evidence="GEKLÄRT") -> dict:
    return {"id":identifier,"category_id":category,"label":category,"amount":amount,"currency":"EUR","period":period,"data_type":"NUTZEREINGABE","evidence_status":"GEKLÄRT" if not_relevant else evidence,"reliability_status":reliability,"required_for_result":True,"not_relevant":not_relevant,"not_relevant_reason":"Für diesen Test nicht relevant." if not_relevant else None,"source_ref":None,"note":None}


def base() -> dict:
    data = {"portfolio_id":"C01","canonical_product_id":"IMR-DL-C01","income_items":[item("income-1","INCOME_EMPLOYMENT","100",reliability="VERIFIED_REGULAR")],"essential_cost_items":[item(f"essential-{i}", category, None, not_relevant=True) for i, category in enumerate(ESSENTIAL)],"optional_cost_items":[],"start_cost_items":[],"reserve":{"amount":None,"as_of_date":None,"currency":"EUR"},"first_month_costs":{"amount":None,"currency":"EUR","scope":"RECURRING_FIRST_MONTH_ONLY","overlap_with_start_costs_checked":False,"evidence_status":"OFFEN","note":None},"user_defined_reserve_target":None,"normal_scenario":{},"stress_scenario":{},"minimum_scenario":{}}
    return data


def result(output: dict, identifier: str) -> dict:
    return next(x for x in output["results"] if x["id"] == identifier)


class C01CalculationTests(unittest.TestCase):
    def test_01_positive_monthly_balance(self):
        data=base(); data["essential_cost_items"][0]=item("rent","COST_HOUSING_RENT","40")
        self.assertEqual(result(calculate(data),"MONTHLY_BALANCE")["value"],"60.00")

    def test_02_negative_monthly_balance(self):
        data=base(); data["essential_cost_items"][0]=item("rent","COST_HOUSING_RENT","140")
        self.assertEqual(result(calculate(data),"MONTHLY_BALANCE")["value"],"-40.00")

    def test_03_annual_to_monthly_normalization(self):
        data=base(); data["income_items"][0]["amount"]="1200"; data["income_items"][0]["period"]="ANNUAL"
        self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"100.00")

    def test_04_weekly_to_monthly_normalization(self):
        data=base(); data["income_items"][0]["amount"]="12"; data["income_items"][0]["period"]="WEEKLY"
        self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"52.00")

    def test_05_one_time_monthly_separation(self):
        data=base(); data["start_cost_items"]=[item("move","START_MOVING","500",period="ONE_TIME")]
        output=calculate(data); self.assertEqual(result(output,"ONE_TIME_START_COSTS")["value"],"500.00"); self.assertEqual(result(output,"MONTHLY_COSTS_TOTAL")["value"],"0.00")

    def test_06_decimal_precision(self):
        data=base(); data["income_items"]= [item("a","INCOME_EMPLOYMENT","0.10",reliability="VERIFIED_REGULAR"),item("b","INCOME_REGULAR_CONTRACT","0.20",reliability="VERIFIED_REGULAR")]
        self.assertEqual(result(calculate(data),"MONTHLY_INCOME_TOTAL")["value"],"0.30")

    def test_07_zero_essential_cost_denominator(self):
        data=base(); data["reserve"]={"amount":"10","as_of_date":"test","currency":"EUR"}
        self.assertEqual(result(calculate(data),"RESERVE_COVERAGE_MONTHS")["status"],"OFFEN")

    def test_08_missing_required_cost_category(self):
        data=base(); data["essential_cost_items"]=data["essential_cost_items"][1:]
        self.assertIn("NECESSARY_COST_POSITION_MISSING",[x["condition"] for x in calculate(data)["blockers"]])

    def test_09_required_category_marked_not_relevant(self):
        output=calculate(base()); self.assertNotIn("NECESSARY_COST_POSITION_MISSING",[x["condition"] for x in output["blockers"]])

    def test_10_uncertain_income_separated(self):
        data=base(); data["income_items"].append(item("uncertain","INCOME_IRREGULAR","30",reliability="ESTIMATED")); output=calculate(data)
        self.assertEqual(result(output,"MONTHLY_INCOME_TOTAL")["value"],"100.00"); self.assertEqual(result(output,"UNCERTAIN_MONTHLY_INCOME")["value"],"30.00")

    def test_11_main_income_not_evidenced_blocker(self):
        data=base(); data["income_items"][0]["reliability_status"]="UNKNOWN"
        self.assertIn("MAIN_INCOME_NOT_EVIDENCED",[x["condition"] for x in calculate(data)["blockers"]])

    def test_12_negative_minimum_scenario_blocker(self):
        data=base(); data["minimum_scenario"]={"income_items":[item("mi","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[item("mc","COST_HOUSING_RENT","20",period="SCENARIO")],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        self.assertIn("MINIMUM_CASE_NEGATIVE",[x["condition"] for x in calculate(data)["blockers"]])

    def test_13_incomplete_stress_scenario(self):
        output=calculate(base()); self.assertEqual(output["scenarios"]["STRESS"]["status"],"OFFEN")

    def test_14_duplicate_item_id_rejected(self):
        data=base(); data["income_items"].append(copy.deepcopy(data["income_items"][0]));
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_15_unknown_category_rejected(self):
        data=base(); data["income_items"][0]["category_id"]="COST_UNKNOWN"
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_16_negative_user_amount_rejected(self):
        data=base(); data["income_items"][0]["amount"]="-1"
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_17_wrong_currency_rejected(self):
        data=base(); data["income_items"][0]["currency"]="USD"
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_18_missing_period_rejected(self):
        data=base(); del data["income_items"][0]["period"]
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_19_no_relocation_approval_output(self):
        output=json.dumps(calculate(base()),ensure_ascii=False)
        for forbidden in ("SAFE_TO_MOVE","APPROVED","RECOMMENDED","FINANCIALLY_SECURE"):
            self.assertNotIn(forbidden,output)

    def test_20_deterministic_repeated_calculation(self):
        data=base(); self.assertEqual(calculate(data),calculate(copy.deepcopy(data)))

    def test_21_category_taxonomy_contains_exactly_35_categories(self):
        categories=json.loads(Path(__file__).resolve().parents[1].joinpath("manifests/c01-budget-categories.json").read_text(encoding="utf-8"))["categories"]
        self.assertEqual(len(categories),35); self.assertNotIn("START_EMERGENCY_BUFFER",[x["id"] for x in categories])

    def test_22_contract_draft_engine_result_id_parity(self):
        expected=["REPORTED_MONTHLY_INCOME","UNCERTAIN_MONTHLY_INCOME","MONTHLY_INCOME_TOTAL","ESSENTIAL_MONTHLY_COSTS","OPTIONAL_MONTHLY_COSTS","MONTHLY_COSTS_TOTAL","MONTHLY_BALANCE","ONE_TIME_START_COSTS","LIQUID_RESERVE","RESERVE_COVERAGE_MONTHS","FIRST_MONTH_COSTS","STRESS_MONTH_INCOME","STRESS_MONTH_COSTS","STRESS_MONTH_BALANCE","MINIMUM_CASE_INCOME","MINIMUM_CASE_COSTS","MINIMUM_CASE_BALANCE","USER_DEFINED_RESERVE_TARGET","START_CAPITAL_NEED"]
        contract=json.loads(Path(__file__).resolve().parents[1].joinpath("manifests/c01-content-contract.json").read_text(encoding="utf-8")); draft=json.loads(Path(__file__).resolve().parents[1].joinpath("content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text(encoding="utf-8")); engine=[x["id"] for x in calculate(base())["results"]]
        self.assertEqual(contract["calculated_results"],expected); self.assertEqual(list(draft["calculated_results"]),expected); self.assertEqual(engine,expected)

    def test_23_unknown_scenario_category_rejected(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_UNKNOWN","10",period="SCENARIO")],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_24_wrong_scenario_currency_rejected(self):
        data=base(); scenario_item=item("si","INCOME_EMPLOYMENT","10",period="SCENARIO"); scenario_item["currency"]="USD"; data["stress_scenario"]={"income_items":[scenario_item],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_25_incomplete_scenario_missing_cost_remains_open(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        output=calculate(data); self.assertEqual(output["scenarios"]["STRESS"]["status"],"OFFEN"); self.assertIn("SCENARIO_NOT_COMPLETED",[x["condition"] for x in output["warnings"]])

    def test_26_scenario_open_evidence_remains_open(self):
        data=base(); data["stress_scenario"]={"income_items":[item("si","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[item("sc","COST_FOOD_BASIC","5",period="SCENARIO")],"assumptions":[],"open_conditions":[],"evidence_status":"OFFEN"}
        self.assertEqual(calculate(data)["scenarios"]["STRESS"]["status"],"OFFEN")

    def test_27_duplicate_id_across_base_and_scenario_rejected(self):
        data=base(); data["stress_scenario"]={"income_items":[item("income-1","INCOME_EMPLOYMENT","10",period="SCENARIO")],"cost_items":[item("sc","COST_FOOD_BASIC","5",period="SCENARIO")],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_28_start_emergency_buffer_rejected(self):
        data=base(); data["start_cost_items"]=[item("buffer","START_EMERGENCY_BUFFER","10",period="ONE_TIME")]
        with self.assertRaises(C01ValidationError): calculate(data)

    def test_29_unchecked_first_month_overlap_keeps_start_capital_open(self):
        data=base(); data["start_cost_items"]=[item("start","START_TRAVEL","100",period="ONE_TIME")]; data["first_month_costs"].update({"amount":"20","overlap_with_start_costs_checked":False}); data["user_defined_reserve_target"]="30"; output=calculate(data)
        self.assertIsNone(result(output,"START_CAPITAL_NEED")["value"]); self.assertIn("POTENTIAL_DOUBLE_COUNT",[x["condition"] for x in output["warnings"]])

    def test_30_checked_non_overlapping_first_month_costs_calculate(self):
        data=base(); data["start_cost_items"]=[item("start","START_TRAVEL","100",period="ONE_TIME")]; data["first_month_costs"].update({"amount":"20","overlap_with_start_costs_checked":True}); data["user_defined_reserve_target"]="30"
        self.assertEqual(result(calculate(data),"START_CAPITAL_NEED")["value"],"150.00")

    def test_31_calculated_results_and_rules_have_parity(self):
        root=Path(__file__).resolve().parents[1]; contract=json.loads((root/"manifests/c01-content-contract.json").read_text(encoding="utf-8")); self.assertEqual([x["id"] for x in contract["calculation_rules"]],contract["calculated_results"])

    def test_32_required_input_contract_is_structured(self):
        root=Path(__file__).resolve().parents[1]; contract=json.loads((root/"manifests/c01-content-contract.json").read_text(encoding="utf-8")); inputs={x["id"]:x for x in contract["required_inputs"]}; self.assertEqual(inputs["first_month_costs"]["type"],"NUTZEREINGABE_OBJECT"); self.assertEqual(inputs["stress_scenario"]["type"],"SCENARIO_OBJECT"); self.assertIn("income_items",inputs["stress_scenario"]["fields"])

    def test_33_every_external_source_has_check_date_and_update_class(self):
        root=Path(__file__).resolve().parents[1]; matrix=json.loads((root/"content/c01-source-matrix.json").read_text(encoding="utf-8")); self.assertTrue(matrix["external_references"]); self.assertTrue(all(x["check_date"] and x["update_class"] for x in matrix["external_references"]))

    def test_34_no_external_numeric_value_without_source(self):
        root=Path(__file__).resolve().parents[1]; matrix=json.loads((root/"content/c01-source-matrix.json").read_text(encoding="utf-8")); self.assertTrue(all(x.get("value") in (None, "") or x.get("source_reference") for x in matrix["external_references"]))

    def test_35_no_personal_data_in_user_document_requirements(self):
        root=Path(__file__).resolve().parents[1]; text=json.dumps(json.loads((root/"content/c01-source-matrix.json").read_text(encoding="utf-8")),ensure_ascii=False); self.assertNotIn("Kontonummer:",text); self.assertNotIn("Max Mustermann",text); self.assertNotIn(chr(64),text)

    def test_36_no_universal_minimum_or_relocation_approval_output(self):
        root=Path(__file__).resolve().parents[1]; draft=(root/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text(encoding="utf-8"); forbidden=("SAFE_TO_MOVE","READY_TO_PUBLISH","FINANCIALLY_SECURE","UNIVERSAL_MINIMUM"); self.assertTrue(all(x not in draft for x in forbidden))

    def test_37_versions_are_parity_across_all_c01_files(self):
        root=Path(__file__).resolve().parents[1]; c=json.loads((root/"manifests/c01-content-contract.json").read_text(encoding="utf-8")); d=json.loads((root/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text(encoding="utf-8")); s=json.loads((root/"manifests/c01-data-schema.json").read_text(encoding="utf-8")); self.assertEqual(c["content_contract_version"],"1.3.0"); self.assertEqual(c["calculation_ruleset_version"],"1.3.0"); self.assertEqual(d["calculation_ruleset_version"],"1.3.0"); self.assertEqual(c["data_schema_version"],s["schema_version"])

    def test_38_ten_part_anatomy_is_present(self):
        text=Path(__file__).resolve().parents[2].joinpath("docs/download-system/c01-redaktionsentwurf.md").read_text(encoding="utf-8"); labels=["Deckblatt","Dokumentstatus und Transparenz","Nutzen und Zielgruppe","Vorbereitung","Kurzanleitung","Hauptarbeitsbereich","Ergebnis- und Statusbereich","Warnsignale und Grenzen","Nächste Schritte","Quellen, Disclaimer und Versionsinformation"]; self.assertTrue(all(x in text for x in labels))

    def test_39_visible_status_values_match_standard(self):
        allowed={"GEKLÄRT","TEILWEISE_GEKLÄRT","OFFEN","OFFIZIELL_ZU_PRÜFEN","FACHLICH_ZU_PRÜFEN","AKTUELL_NICHT_TRAGFÄHIG"}; root=Path(__file__).resolve().parents[1]; c=json.loads((root/"manifests/c01-content-contract.json").read_text(encoding="utf-8")); self.assertEqual(set(c["result_status_values"]),allowed)

    def test_40_not_relevant_is_not_evidence_status(self):
        root=Path(__file__).resolve().parents[1]; schema=json.loads((root/"manifests/c01-data-schema.json").read_text(encoding="utf-8")); self.assertNotIn("NICHT_RELEVANT",schema["item_required_fields"]["evidence_status"]); data=base(); self.assertTrue(data["essential_cost_items"][0]["not_relevant"]); self.assertEqual(data["essential_cost_items"][0]["evidence_status"],"GEKLÄRT")

    def test_41_visible_results_never_use_incomplete(self):
        output=calculate(base()); allowed={"GEKLÄRT","TEILWEISE_GEKLÄRT","OFFEN","OFFIZIELL_ZU_PRÜFEN","FACHLICH_ZU_PRÜFEN","AKTUELL_NICHT_TRAGFÄHIG"}; self.assertTrue(all(x["status"] in allowed for x in output["results"])); self.assertNotIn("INCOMPLETE",[x["status"] for x in output["results"]])

    def test_42_calculation_reference_matches_ruleset(self):
        root=Path(__file__).resolve().parents[1]; d=json.loads((root/"content/c01-budget-und-sicherheitsarbeitsblatt.draft.json").read_text(encoding="utf-8")); self.assertEqual(d["calculation_reference"],"C01_CALCULATION_RULESET_1.3.0")

    def test_43_external_sources_have_affected_sections(self):
        root=Path(__file__).resolve().parents[1]; matrix=json.loads((root/"content/c01-source-matrix.json").read_text(encoding="utf-8")); self.assertTrue(all(x.get("affected_sections") for x in matrix["external_references"]))

    def test_44_eurostat_publication_date_is_not_invented(self):
        root=Path(__file__).resolve().parents[1]; matrix=json.loads((root/"content/c01-source-matrix.json").read_text(encoding="utf-8")); euro=next(x for x in matrix["external_references"] if x["source_id"]=="EXT-HICP-METHOD-001"); self.assertEqual(euro["publication_date"],"NOT_STATED_BY_PUBLISHER")

    def test_45_visible_tables_use_german_primary_labels(self):
        text=Path(__file__).resolve().parents[2].joinpath("docs/download-system/c01-redaktionsentwurf.md").read_text(encoding="utf-8"); self.assertIn("Zeitraum",text); self.assertIn("notwendige oder optionale Kosten",text); self.assertIn("einmalig",text); self.assertNotIn("| UNKNOWN |",text); self.assertNotIn("| ESSENTIAL oder OPTIONAL |",text)


    def test_41_visible_results_never_use_incomplete(self):
        output=calculate(base()); allowed={"GEKL\u00c4RT","TEILWEISE_GEKL\u00c4RT","OFFEN","OFFIZIELL_ZU_PR\u00dcFEN","FACHLICH_ZU_PR\u00dcFEN","AKTUELL_NICHT_TRAGF\u00c4HIG"}; self.assertTrue(all(x["status"] in allowed for x in output["results"])); self.assertNotIn("INCOMPLETE",[x["status"] for x in output["results"]])

if __name__ == "__main__":
    unittest.main(verbosity=2)
