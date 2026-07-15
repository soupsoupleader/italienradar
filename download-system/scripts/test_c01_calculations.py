#!/usr/bin/env python3
"""Twenty executable regression tests for calculate_c01.py."""
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
    return {"id":identifier,"category_id":category,"label":category,"amount":amount,"currency":"EUR","period":period,"data_type":"NUTZEREINGABE","evidence_status":"NICHT_RELEVANT" if not_relevant else evidence,"reliability_status":reliability,"required_for_result":True,"not_relevant":not_relevant,"not_relevant_reason":"Für diesen Test nicht relevant." if not_relevant else None,"source_ref":None,"note":None}


def base() -> dict:
    data = {"portfolio_id":"C01","canonical_product_id":"IMR-DL-C01","income_items":[item("income-1","INCOME_EMPLOYMENT","100",reliability="VERIFIED_REGULAR")],"essential_cost_items":[item(f"essential-{i}", category, None, not_relevant=True) for i, category in enumerate(ESSENTIAL)],"optional_cost_items":[],"start_cost_items":[],"reserve":{"amount":None,"as_of_date":None,"currency":"EUR"},"first_month_costs":None,"user_defined_reserve_target":None,"normal_scenario":{},"stress_scenario":{},"minimum_scenario":{}}
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
        self.assertEqual(result(calculate(data),"RESERVE_COVERAGE_MONTHS")["status"],"OFFEN_ZU_PRÜFEN")

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
        data=base(); data["minimum_scenario"]={"income_items":[item("mi","INCOME_EMPLOYMENT","10")],"cost_items":[item("mc","COST_HOUSING_RENT","20")],"assumptions":[],"open_conditions":[],"evidence_status":"GEKLÄRT"}
        self.assertIn("MINIMUM_CASE_NEGATIVE",[x["condition"] for x in calculate(data)["blockers"]])

    def test_13_incomplete_stress_scenario(self):
        output=calculate(base()); self.assertEqual(output["scenarios"]["STRESS"]["status"],"OFFEN_ZU_PRÜFEN")

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
