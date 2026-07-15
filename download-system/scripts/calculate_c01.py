#!/usr/bin/env python3
"""Deterministic, data-only C01 calculation core.

The module uses Decimal for all monetary arithmetic and has no network,
shell, renderer, PDF, or source-file side effects.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any

DATA_ROLES = {"NUTZEREINGABE", "ORIENTIERUNGSWERT", "BERECHNETES_ERGEBNIS", "REDAKTIONELLE_EINORDNUNG", "OFFEN_ZU_PRÜFEN"}
EVIDENCE = {"GEKLÄRT", "TEILWEISE_GEKLÄRT", "OFFEN", "OFFIZIELL_ZU_PRÜFEN", "FACHLICH_ZU_PRÜFEN", "AKTUELL_NICHT_TRAGFÄHIG"}
RELIABILITY = {"VERIFIED_REGULAR", "PARTIALLY_VERIFIED", "ESTIMATED", "IRREGULAR", "UNKNOWN"}
PERIODS = {"MONTHLY", "ANNUAL", "WEEKLY", "ONE_TIME", "AS_OF_DATE", "SCENARIO"}
INCOME_CATEGORIES = {"INCOME_EMPLOYMENT", "INCOME_SELF_EMPLOYMENT", "INCOME_PENSION", "INCOME_REGULAR_CONTRACT", "INCOME_OTHER_REGULAR", "INCOME_IRREGULAR"}
ESSENTIAL_CATEGORIES = {"COST_HOUSING_RENT", "COST_HOUSING_SERVICE_CHARGES", "COST_ELECTRICITY", "COST_GAS_OR_HEATING", "COST_WATER", "COST_FOOD_BASIC", "COST_HEALTH_AND_INSURANCE", "COST_TRANSPORT_REQUIRED", "COST_INTERNET", "COST_MOBILE", "COST_CONTRACTUAL_OBLIGATIONS", "COST_OTHER_ESSENTIAL"}
OPTIONAL_CATEGORIES = {"COST_LEISURE", "COST_EATING_OUT", "COST_SUBSCRIPTIONS", "COST_TRAVEL_OPTIONAL", "COST_SHOPPING_OPTIONAL", "COST_OTHER_OPTIONAL"}
START_CATEGORIES = {"START_TRAVEL", "START_MOVING", "START_TEMPORARY_ACCOMMODATION", "START_RENT_DEPOSIT", "START_FIRST_RENT", "START_BASIC_FURNITURE", "START_HOUSEHOLD_SETUP", "START_UTILITY_ACTIVATION", "START_DOCUMENTS_AND_FEES", "START_TRANSPORT_SETUP", "START_OTHER"}
ALL_CATEGORIES = INCOME_CATEGORIES | ESSENTIAL_CATEGORIES | OPTIONAL_CATEGORIES | START_CATEGORIES
REQUIRED_GROUPS = {
    "Wohnen": {"COST_HOUSING_RENT", "COST_HOUSING_SERVICE_CHARGES"},
    "Energie/Versorgung": {"COST_ELECTRICITY", "COST_GAS_OR_HEATING", "COST_WATER"},
    "Grundnahrung": {"COST_FOOD_BASIC"},
    "Gesundheit/Absicherung": {"COST_HEALTH_AND_INSURANCE"},
    "notwendige Mobilität": {"COST_TRANSPORT_REQUIRED"},
    "Kommunikation": {"COST_INTERNET", "COST_MOBILE"},
    "vertragliche Verpflichtungen": {"COST_CONTRACTUAL_OBLIGATIONS"},
}
STATUS_CLEAR = "GEKL\u00c4RT"
STATUS_PARTIAL = "TEILWEISE_GEKL\u00c4RT"
STATUS_OPEN = "OFFEN"
STATUS_OFFICIAL = "OFFIZIELL_ZU_PR\u00dcFEN"
STATUS_TECHNICAL = "FACHLICH_ZU_PR\u00dcFEN"
STATUS_NOT_VIABLE = "AKTUELL_NICHT_TRAGF\u00c4HIG"
ZERO = Decimal("0")


class C01ValidationError(ValueError):
    """Input violates a controlled C01 boundary."""


def money(value: Any, field: str = "amount") -> Decimal:
    if value is None:
        raise C01ValidationError(f"{field}: missing amount")
    if isinstance(value, bool):
        raise C01ValidationError(f"{field}: boolean is not money")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise C01ValidationError(f"{field}: invalid decimal") from exc
    if not result.is_finite() or result < ZERO:
        raise C01ValidationError(f"{field}: negative or non-finite amount")
    return result


def normalize(amount: Decimal, period: str) -> Decimal:
    if period == "MONTHLY":
        return amount
    if period == "ANNUAL":
        return amount / Decimal("12")
    if period == "WEEKLY":
        return amount * Decimal("52") / Decimal("12")
    if period in {"ONE_TIME", "AS_OF_DATE", "SCENARIO"}:
        return amount
    raise C01ValidationError(f"period: unsupported {period}")


def _validate_item(item: dict[str, Any], known: set[str], ids: set[str]) -> None:
    required = {"id", "category_id", "label", "amount", "currency", "period", "data_type", "evidence_status", "reliability_status", "required_for_result", "not_relevant", "not_relevant_reason", "source_ref", "note"}
    missing = required - set(item)
    if missing:
        raise C01ValidationError(f"item missing fields: {sorted(missing)}")
    if not isinstance(item["id"], str) or not item["id"] or item["id"] in ids:
        raise C01ValidationError(f"duplicate or invalid item id: {item.get('id')}")
    ids.add(item["id"])
    if item["category_id"] not in known:
        raise C01ValidationError(f"unknown category: {item['category_id']}")
    if not isinstance(item["label"], str) or not item["label"].strip():
        raise C01ValidationError(f"empty label: {item['id']}")
    if item["currency"] != "EUR":
        raise C01ValidationError(f"wrong currency: {item['id']}")
    if item["period"] not in PERIODS:
        raise C01ValidationError(f"invalid period: {item['id']}")
    if item["data_type"] not in DATA_ROLES:
        raise C01ValidationError(f"invalid data type: {item['id']}")
    if item["evidence_status"] not in EVIDENCE:
        raise C01ValidationError(f"invalid evidence status: {item['id']}")
    if item["reliability_status"] not in RELIABILITY:
        raise C01ValidationError(f"invalid reliability: {item['id']}")
    if not isinstance(item["required_for_result"], bool) or not isinstance(item["not_relevant"], bool):
        raise C01ValidationError(f"boolean field invalid: {item['id']}")
    if item["not_relevant"] and (not item["not_relevant_reason"] or item["evidence_status"] not in EVIDENCE):
        raise C01ValidationError(f"not relevant item needs reason and valid evidence status: {item['id']}")
    if not item["not_relevant"] and item["amount"] is not None:
        money(item["amount"], item["id"])
    if not item["not_relevant"] and item["amount"] is None and item["required_for_result"]:
        # This is reported as incomplete by calculate, not an invented zero.
        return


def _item_value(item: dict[str, Any]) -> Decimal:
    if item["amount"] is None or item["not_relevant"]:
        return ZERO
    return normalize(money(item["amount"], item["id"]), item["period"])


def result_item(identifier: str, value: Decimal | None, unit: str, status: str, used: list[str], excluded: list[str], explanation: str) -> dict[str, Any]:
    return {"id": identifier, "value": None if value is None else str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)), "unit": unit, "status": status, "inputs_used": sorted(used), "excluded_inputs": sorted(excluded), "explanation": explanation}


def _validate_scenario(value: Any, name: str, ids: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise C01ValidationError(f"{name}: scenario must be an object")
    income = value.get("income_items", [])
    costs = value.get("cost_items", [])
    assumptions = value.get("assumptions", [])
    open_conditions = value.get("open_conditions", [])
    evidence_status = value.get("evidence_status", "OFFEN")
    if not isinstance(income, list) or not isinstance(costs, list) or not isinstance(assumptions, list) or not isinstance(open_conditions, list):
        raise C01ValidationError(f"{name}: arrays required")
    if evidence_status not in EVIDENCE:
        raise C01ValidationError(f"{name}: invalid evidence status")
    for item in income:
        _validate_item(item, INCOME_CATEGORIES, ids)
        if item["period"] != "SCENARIO":
            raise C01ValidationError(f"{name}: income period must be SCENARIO")
    for item in costs:
        _validate_item(item, ESSENTIAL_CATEGORIES | OPTIONAL_CATEGORIES, ids)
        if item["period"] != "SCENARIO":
            raise C01ValidationError(f"{name}: cost period must be SCENARIO")
    return value


def _scenario(value: dict[str, Any], name: str) -> dict[str, Any]:
    income = value.get("income_items", [])
    costs = value.get("cost_items", [])
    evidence_status = value.get("evidence_status", "OFFEN")
    complete = bool(income) and bool(costs) and evidence_status in {"GEKLÄRT", "TEILWEISE_GEKLÄRT"}
    return {"name": name, "income_items": income, "cost_items": costs, "assumptions": value.get("assumptions", []), "open_conditions": value.get("open_conditions", []), "evidence_status": evidence_status, "complete": complete}


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("portfolio_id") != "C01" or data.get("canonical_product_id") != "IMR-DL-C01":
        raise C01ValidationError("C01 identity mismatch")
    all_items: list[dict[str, Any]] = []
    groups = [("income_items", INCOME_CATEGORIES), ("essential_cost_items", ESSENTIAL_CATEGORIES), ("optional_cost_items", OPTIONAL_CATEGORIES), ("start_cost_items", START_CATEGORIES)]
    ids: set[str] = set()
    for key, allowed in groups:
        for item in data.get(key, []):
            _validate_item(item, allowed, ids)
            all_items.append(item)
    if not isinstance(data.get("reserve", {}), dict):
        raise C01ValidationError("reserve must be an object")
    scenario_inputs = {}
    for scenario_name in ("NORMAL", "STRESS", "MINIMUM"):
        key = f"{scenario_name.lower()}_scenario"
        scenario_inputs[scenario_name] = _validate_scenario(data.get(key, {}), scenario_name, ids)
    missing_categories = sorted({c for values in REQUIRED_GROUPS.values() for c in values if not any(i["category_id"] == c and (i["amount"] is not None or i["not_relevant"]) for i in data.get("essential_cost_items", []))})
    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    if missing_categories:
        blockers.append({"condition":"NECESSARY_COST_POSITION_MISSING","meaning":"A required cost category has no amount and is not marked NICHT_RELEVANT.","required_action":"Provide the value or record NICHT_RELEVANT with a reason.","affected_items":missing_categories})
    def total(items: list[dict[str, Any]], predicate=lambda i: True, exclude_one_time=False) -> tuple[Decimal, list[str], list[str]]:
        value, used, excluded = ZERO, [], []
        for item in items:
            if not predicate(item):
                continue
            if item["amount"] is None or item["not_relevant"]:
                continue
            if exclude_one_time and item["period"] == "ONE_TIME":
                excluded.append(item["id"]); continue
            value += _item_value(item); used.append(item["id"])
        return value, used, excluded
    income = data.get("income_items", [])
    reported, reported_used, _ = total(income)
    reliable, reliable_used, _ = total(income, lambda i: i["reliability_status"] == "VERIFIED_REGULAR")
    uncertain = reported - reliable
    if any(i["reliability_status"] != "VERIFIED_REGULAR" and i["amount"] is not None for i in income):
        warnings.append({"condition":"UNCERTAIN_INCOME","risk":"Some income is not verified as regular.","meaning":"Reported income and reliable income differ.","next_check":"Document reliability for each income item.","affected_items":[i["id"] for i in income if i["reliability_status"] != "VERIFIED_REGULAR"]})
    essential, essential_used, essential_excluded = total(data.get("essential_cost_items", []), exclude_one_time=True)
    optional, optional_used, optional_excluded = total(data.get("optional_cost_items", []), exclude_one_time=True)
    start, start_used, start_excluded = total(data.get("start_cost_items", []))
    monthly_total = essential + optional
    balance = reliable - monthly_total
    reserve_value = data.get("reserve", {}).get("amount")
    reserve = None if reserve_value is None else money(reserve_value, "reserve")
    if reserve is None or essential == ZERO:
        coverage = None
        coverage_status = "OFFEN_ZU_PRÜFEN"
    else:
        coverage = reserve / essential
        coverage_status = "GEKLÄRT"
    first_month = data.get("first_month_costs")
    if not isinstance(first_month, dict):
        raise C01ValidationError("first_month_costs must be a structured object")
    if first_month.get("currency") != "EUR" or first_month.get("scope") != "RECURRING_FIRST_MONTH_ONLY" or first_month.get("evidence_status") not in EVIDENCE:
        raise C01ValidationError("first_month_costs contract invalid")
    if not isinstance(first_month.get("overlap_with_start_costs_checked"), bool):
        raise C01ValidationError("first_month_costs overlap check required")
    target = data.get("user_defined_reserve_target")
    first_month_d = None if first_month.get("amount") is None else money(first_month["amount"], "first_month_costs")
    target_d = None if target is None else money(target, "user_defined_reserve_target")
    if first_month_d is not None and not first_month["overlap_with_start_costs_checked"]:
        warnings.append({"condition":"POTENTIAL_DOUBLE_COUNT","risk":"First-month recurring costs may overlap with one-time start costs.","meaning":"START_CAPITAL_NEED cannot safely combine the values yet.","next_check":"Confirm that first-month recurring costs are not already listed as ONE_TIME.","affected_items":["first_month_costs"]})
    scenarios = {name: _scenario(scenario_inputs[name], name) for name in ("NORMAL", "STRESS", "MINIMUM")}
    scenario_results: dict[str, dict[str, Any]] = {}
    for name, scenario in scenarios.items():
        if not scenario["complete"]:
            scenario_results[name] = {"status":"OFFEN","income":None,"costs":None,"balance":None,"income_items":[],"cost_items":[],"assumptions":scenario["assumptions"],"open_conditions":scenario["open_conditions"],"evidence_status":scenario["evidence_status"]}
            if name in {"STRESS", "MINIMUM"}:
                warnings.append({"condition":"SCENARIO_NOT_COMPLETED","risk":f"{name} scenario is incomplete.","meaning":"No scenario result is calculated.","next_check":"Enter scenario items and evidence status.","affected_items":[]})
            continue
        si, su, _ = total(scenario["income_items"])
        sc, scu, _ = total(scenario["cost_items"], exclude_one_time=True)
        scenario_results[name] = {"status":"GEKLÄRT","income":si,"costs":sc,"balance":si-sc,"income_items":su,"cost_items":scu,"assumptions":scenario["assumptions"],"open_conditions":scenario["open_conditions"],"evidence_status":scenario["evidence_status"]}
    if scenario_results["MINIMUM"]["balance"] is not None and scenario_results["MINIMUM"]["balance"] < ZERO:
        blockers.append({"condition":"MINIMUM_CASE_NEGATIVE","meaning":"MINIMUM_CASE_BALANCE is below zero.","required_action":"Review the stated minimum-case inputs and open conditions.","affected_items":scenario_results["MINIMUM"]["income_items"] + scenario_results["MINIMUM"]["cost_items"]})
    if not reliable and income:
        blockers.append({"condition":"MAIN_INCOME_NOT_EVIDENCED","meaning":"No income item is VERIFIED_REGULAR.","required_action":"Provide evidence or keep the result provisional.","affected_items":[i["id"] for i in income]})
    if not all_items or missing_categories:
        warnings.append({"condition":"INSUFFICIENT_DATA","risk":"Required calculation data is incomplete.","meaning":"Aggregates cannot be interpreted as a complete budget.","next_check":"Complete required values or mark them NICHT_RELEVANT.","affected_items":missing_categories})
    results = [
        result_item("REPORTED_MONTHLY_INCOME", reported, "EUR/month", "GEKLÄRT" if reported_used else "OFFEN", reported_used, [], "All reported income normalized to a monthly value."),
        result_item("UNCERTAIN_MONTHLY_INCOME", uncertain, "EUR/month", "GEKLÄRT" if reported_used else "OFFEN", reported_used, reliable_used, "Reported income not marked VERIFIED_REGULAR remains separate."),
        result_item("MONTHLY_INCOME_TOTAL", reliable, "EUR/month", "GEKLÄRT" if reliable_used else "OFFEN", reliable_used, [i["id"] for i in income if i["id"] not in reliable_used], "Only VERIFIED_REGULAR income is included."),
        result_item("ESSENTIAL_MONTHLY_COSTS", essential, "EUR/month", "OFFEN" if missing_categories else "GEKLÄRT", essential_used, essential_excluded, "Necessary monthly costs; one-time items are excluded."),
        result_item("OPTIONAL_MONTHLY_COSTS", optional, "EUR/month", "GEKLÄRT", optional_used, optional_excluded, "Optional monthly costs; one-time items are excluded."),
        result_item("MONTHLY_COSTS_TOTAL", monthly_total, "EUR/month", "OFFEN" if missing_categories else "GEKLÄRT", essential_used + optional_used, essential_excluded + optional_excluded, "Essential plus optional monthly costs."),
        result_item("MONTHLY_BALANCE", balance, "EUR/month", "OFFEN" if missing_categories else "GEKLÄRT", reliable_used + essential_used + optional_used, [], "Reliable monthly income minus monthly costs."),
        result_item("ONE_TIME_START_COSTS", start, "EUR", "GEKLÄRT" if start_used else "OFFEN", start_used, [], "One-time start costs are kept separate from monthly costs."),
        result_item("LIQUID_RESERVE", reserve, "EUR", "GEKLÄRT" if reserve is not None else "OFFEN", [], [], "Reserve at the user-stated as-of date."),
        result_item("RESERVE_COVERAGE_MONTHS", coverage, "months", "GEKLÄRT" if coverage is not None else "OFFEN", [], [], "Liquid reserve divided by essential monthly costs; zero denominator is open."),
        result_item("FIRST_MONTH_COSTS", first_month_d, "EUR", "GEKLÄRT" if first_month_d is not None else "OFFEN", [], [], "User-defined first-month cost input."),
        result_item("STRESS_MONTH_INCOME", scenario_results["STRESS"]["income"], "EUR/month", scenario_results["STRESS"]["status"], scenario_results["STRESS"]["income_items"], [], "Stress scenario income."),
        result_item("STRESS_MONTH_COSTS", scenario_results["STRESS"]["costs"], "EUR/month", scenario_results["STRESS"]["status"], scenario_results["STRESS"]["cost_items"], [], "Stress scenario costs."),
        result_item("STRESS_MONTH_BALANCE", scenario_results["STRESS"]["balance"], "EUR/month", scenario_results["STRESS"]["status"], scenario_results["STRESS"]["income_items"] + scenario_results["STRESS"]["cost_items"], [], "Stress scenario income minus stress scenario costs."),
        result_item("MINIMUM_CASE_INCOME", scenario_results["MINIMUM"]["income"], "EUR/month", scenario_results["MINIMUM"]["status"], scenario_results["MINIMUM"]["income_items"], [], "Minimum scenario income."),
        result_item("MINIMUM_CASE_COSTS", scenario_results["MINIMUM"]["costs"], "EUR/month", scenario_results["MINIMUM"]["status"], scenario_results["MINIMUM"]["cost_items"], [], "Minimum scenario costs."),
        result_item("MINIMUM_CASE_BALANCE", scenario_results["MINIMUM"]["balance"], "EUR/month", scenario_results["MINIMUM"]["status"], scenario_results["MINIMUM"]["income_items"] + scenario_results["MINIMUM"]["cost_items"], [], "Minimum scenario income minus minimum scenario costs."),
        result_item("USER_DEFINED_RESERVE_TARGET", target_d, "EUR", "GEKLÄRT" if target_d is not None else "OFFEN_ZU_PRÜFEN", [], [], "No automatic reserve threshold is introduced."),
    ]
    start_need = None if start_used == [] or first_month_d is None or target_d is None or not first_month["overlap_with_start_costs_checked"] else start + first_month_d + target_d
    results.append(result_item("START_CAPITAL_NEED", start_need, "EUR", "GEKLÄRT" if start_need is not None else "OFFEN_ZU_PRÜFEN", start_used, [], "One-time start costs plus first-month costs plus user-defined reserve target."))
    for item in results:
        if item["status"].startswith("GEKL"):
            item["status"] = STATUS_CLEAR
        elif item["status"].startswith("OFFEN_ZU"):
            item["status"] = STATUS_OPEN
    for scenario in scenario_results.values():
        if scenario["status"].startswith("GEKL"):
            scenario["status"] = STATUS_CLEAR
        elif scenario["status"].startswith("OFFEN_ZU"):
            scenario["status"] = STATUS_OPEN
    return {"result_version":"1.3.0","calculation_status":"INCOMPLETE" if blockers or missing_categories else "COMPLETE","results":results,"scenarios":{k:{**v, **({"income":str(v["income"]),"costs":str(v["costs"]),"balance":str(v["balance"])} if v["income"] is not None else {})} for k,v in scenario_results.items()},"warnings":warnings,"blockers":blockers,"release_controls":{"release_eligible":False,"pdf_build_allowed":False,"public_pdf_allowed":False,"website_integration_allowed":False,"deployment":False}}


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate the C01 budget core")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    output = calculate(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
