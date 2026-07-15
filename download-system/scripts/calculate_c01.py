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
EVIDENCE = {"GEKLÄRT", "TEILWEISE_GEKLÄRT", "OFFEN", "OFFIZIELL_ZU_PRÜFEN", "FACHLICH_ZU_PRÜFEN", "AKTUELL_NICHT_TRAGFÄHIG", "NICHT_RELEVANT"}
RELIABILITY = {"VERIFIED_REGULAR", "PARTIALLY_VERIFIED", "ESTIMATED", "IRREGULAR", "UNKNOWN"}
PERIODS = {"MONTHLY", "ANNUAL", "WEEKLY", "ONE_TIME", "AS_OF_DATE", "SCENARIO"}
INCOME_CATEGORIES = {"INCOME_EMPLOYMENT", "INCOME_SELF_EMPLOYMENT", "INCOME_PENSION", "INCOME_REGULAR_CONTRACT", "INCOME_OTHER_REGULAR", "INCOME_IRREGULAR"}
ESSENTIAL_CATEGORIES = {"COST_HOUSING_RENT", "COST_HOUSING_SERVICE_CHARGES", "COST_ELECTRICITY", "COST_GAS_OR_HEATING", "COST_WATER", "COST_FOOD_BASIC", "COST_HEALTH_AND_INSURANCE", "COST_TRANSPORT_REQUIRED", "COST_INTERNET", "COST_MOBILE", "COST_CONTRACTUAL_OBLIGATIONS", "COST_OTHER_ESSENTIAL"}
OPTIONAL_CATEGORIES = {"COST_LEISURE", "COST_EATING_OUT", "COST_SUBSCRIPTIONS", "COST_TRAVEL_OPTIONAL", "COST_SHOPPING_OPTIONAL", "COST_OTHER_OPTIONAL"}
START_CATEGORIES = {"START_TRAVEL", "START_MOVING", "START_TEMPORARY_ACCOMMODATION", "START_RENT_DEPOSIT", "START_FIRST_RENT", "START_BASIC_FURNITURE", "START_HOUSEHOLD_SETUP", "START_UTILITY_ACTIVATION", "START_DOCUMENTS_AND_FEES", "START_TRANSPORT_SETUP", "START_EMERGENCY_BUFFER", "START_OTHER"}
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
    if item["not_relevant"] and (not item["not_relevant_reason"] or item["evidence_status"] != "NICHT_RELEVANT"):
        raise C01ValidationError(f"not relevant item needs reason/status: {item['id']}")
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


def _scenario(data: dict[str, Any], name: str) -> dict[str, Any]:
    value = data.get(f"{name.lower()}_scenario") or {}
    income = value.get("income_items", [])
    costs = value.get("cost_items", [])
    return {"name": name, "income_items": income, "cost_items": costs, "assumptions": value.get("assumptions", []), "open_conditions": value.get("open_conditions", []), "evidence_status": value.get("evidence_status", "OFFEN"), "complete": bool(income or costs) and bool(value.get("evidence_status"))}


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
    target = data.get("user_defined_reserve_target")
    first_month_d = None if first_month is None else money(first_month, "first_month_costs")
    target_d = None if target is None else money(target, "user_defined_reserve_target")
    scenarios = {name: _scenario(data, name) for name in ("NORMAL", "STRESS", "MINIMUM")}
    scenario_results: dict[str, dict[str, Any]] = {}
    for name, scenario in scenarios.items():
        if not scenario["complete"]:
            scenario_results[name] = {"status":"OFFEN_ZU_PRÜFEN","income":None,"costs":None,"balance":None,"income_items":[],"cost_items":[],"assumptions":scenario["assumptions"],"open_conditions":scenario["open_conditions"],"evidence_status":scenario["evidence_status"]}
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
        result_item("REPORTED_MONTHLY_INCOME", reported, "EUR/month", "GEKLÄRT" if reported_used else "OFFEN_ZU_PRÜFEN", reported_used, [], "All reported income normalized to a monthly value."),
        result_item("UNCERTAIN_MONTHLY_INCOME", uncertain, "EUR/month", "GEKLÄRT" if reported_used else "OFFEN_ZU_PRÜFEN", reported_used, reliable_used, "Reported income not marked VERIFIED_REGULAR remains separate."),
        result_item("MONTHLY_INCOME_TOTAL", reliable, "EUR/month", "GEKLÄRT" if reliable_used else "OFFEN_ZU_PRÜFEN", reliable_used, [i["id"] for i in income if i["id"] not in reliable_used], "Only VERIFIED_REGULAR income is included."),
        result_item("ESSENTIAL_MONTHLY_COSTS", essential, "EUR/month", "INCOMPLETE" if missing_categories else "GEKLÄRT", essential_used, essential_excluded, "Necessary monthly costs; one-time items are excluded."),
        result_item("OPTIONAL_MONTHLY_COSTS", optional, "EUR/month", "GEKLÄRT", optional_used, optional_excluded, "Optional monthly costs; one-time items are excluded."),
        result_item("MONTHLY_COSTS_TOTAL", monthly_total, "EUR/month", "INCOMPLETE" if missing_categories else "GEKLÄRT", essential_used + optional_used, essential_excluded + optional_excluded, "Essential plus optional monthly costs."),
        result_item("MONTHLY_BALANCE", balance, "EUR/month", "INCOMPLETE" if missing_categories else "GEKLÄRT", reliable_used + essential_used + optional_used, [], "Reliable monthly income minus monthly costs."),
        result_item("ONE_TIME_START_COSTS", start, "EUR", "GEKLÄRT" if start_used else "OFFEN_ZU_PRÜFEN", start_used, [], "One-time start costs are kept separate from monthly costs."),
        result_item("LIQUID_RESERVE", reserve, "EUR", "GEKLÄRT" if reserve is not None else "OFFEN_ZU_PRÜFEN", [], [], "Reserve at the user-stated as-of date."),
        result_item("RESERVE_COVERAGE_MONTHS", coverage, "months", coverage_status, [], [], "Liquid reserve divided by essential monthly costs; zero denominator is open."),
        result_item("FIRST_MONTH_COSTS", first_month_d, "EUR", "GEKLÄRT" if first_month_d is not None else "OFFEN_ZU_PRÜFEN", [], [], "User-defined first-month cost input."),
        result_item("STRESS_MONTH_BALANCE", scenario_results["STRESS"]["balance"], "EUR/month", scenario_results["STRESS"]["status"], scenario_results["STRESS"]["income_items"] + scenario_results["STRESS"]["cost_items"], [], "Stress scenario income minus stress scenario costs."),
        result_item("MINIMUM_CASE_BALANCE", scenario_results["MINIMUM"]["balance"], "EUR/month", scenario_results["MINIMUM"]["status"], scenario_results["MINIMUM"]["income_items"] + scenario_results["MINIMUM"]["cost_items"], [], "Minimum scenario income minus minimum scenario costs."),
        result_item("USER_DEFINED_RESERVE_TARGET", target_d, "EUR", "GEKLÄRT" if target_d is not None else "OFFEN_ZU_PRÜFEN", [], [], "No automatic reserve threshold is introduced."),
    ]
    start_need = None if start_used == [] or first_month_d is None or target_d is None else start + first_month_d + target_d
    results.append(result_item("START_CAPITAL_NEED", start_need, "EUR", "GEKLÄRT" if start_need is not None else "OFFEN_ZU_PRÜFEN", start_used, [], "One-time start costs plus first-month costs plus user-defined reserve target."))
    return {"result_version":"1.1.0","calculation_status":"INCOMPLETE" if blockers or missing_categories else "COMPLETE","results":results,"scenarios":{k:{**v, **({"income":str(v["income"]),"costs":str(v["costs"]),"balance":str(v["balance"])} if v["income"] is not None else {})} for k,v in scenario_results.items()},"warnings":warnings,"blockers":blockers,"release_controls":{"release_eligible":False,"pdf_build_allowed":False,"public_pdf_allowed":False,"website_integration_allowed":False,"deployment":False}}


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
