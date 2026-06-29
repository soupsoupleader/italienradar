/* ==========================================================================
   Italia Money Radar — Kostenrechner
   Verarbeitet Formulareingaben lokal im Browser, keine externen Calls.
   Saubere UTF-8-Kodierung.
   ========================================================================== */

(function () {
  "use strict";

  // -----------------------------------------------------------------------
  // Stadt-/Regionsfaktoren — empirisches gewichtetes Modell
  // -----------------------------------------------------------------------
  // Berechnungsmethode: Gewichteter Mittelwert aus realen Lebenshaltungsdaten.
  //
  // Quellen (alle 2024):
  //   - Numbeo Cost of Living Index 2024/2025 (März 2025)
  //   - Osservatorio Immobiliare Nomisma: Quadratmeterpreise Kaltmiete 2024
  //   - ISTAT Indici prezzi al consumo 2024
  //   - Tarife öffentlicher Nahverkehr (Trenitalia, ATM Milano, ANM Napoli)
  //   - ARERA Energia: konsolidierte Endkundenpreise 2024
  //
  // Gewichtung (Single-Haushalt, 1-Zimmer-Wohnung, ~1.500 EUR Basis):
  //   Miete          40 %
  //   Lebensmittel   20 %
  //   Freizeit       20 %
  //   Transport      10 %
  //   Energie        10 %
  //
  // Hinweis: Faktoren sind als Orientierung zu verstehen, nicht als
  // exakte Prognose. Mieten schwanken innerhalb derselben Stadt je nach
  // Stadtteil erheblich (z. B. Mailand Centro vs. Peripherie: Faktor 1,5).
  //
  var CITY_DATA = {
    "Palermo":      { factor: 0.91, label: "Palermo",          rentCeil: 1800, description: "etwa 9 % günstiger als Neapel" },
    "Bari":         { factor: 0.96, label: "Bari",             rentCeil: 1800, description: "auf Neapel-Niveau" },
    "Neapel":       { factor: 1.00, label: "Neapel",           rentCeil: 1900, description: "Basiswert des Rechners (1,00)" },
    "Rom":          { factor: 1.32, label: "Rom",              rentCeil: 3500, description: "deutlich teurer (+32 %)" },
    "Mailand":      { factor: 1.51, label: "Mailand",          rentCeil: 4500, description: "am teuersten (+51 %)" },
    "Andere Region":{ factor: 0.95, label: "Andere Region",    rentCeil: 1700, description: "konservative Schätzung für Kleinstädte" }
  };

  // Allgemeine Plausibilitätsgrenzen (zusätzlich zu den miet-spezifischen)
  var PLAUSIBILITY_LIMITS = {
    food: 2000,
    transport: 1500,
    internet: 300,
    health: 2000,
    leisure: 1500,
    other: 2000,
    buffer: 5000
  };

  var FIELD_LABELS = {
    rent: "Miete",
    food: "Essen & Lebensmittel",
    transport: "Transport",
    internet: "Handy & Internet",
    health: "Gesundheit / Versicherung",
    leisure: "Freizeit",
    other: "Sonstige Kosten",
    buffer: "Sicherheitspuffer"
  };

  function $(id) { return document.getElementById(id); }

  function getNumber(id) {
    var el = $(id);
    if (!el) return 0;
    var v = parseFloat(String(el.value).replace(",", "."));
    return isNaN(v) || v < 0 ? 0 : v;
  }

  function formatEuro(value) {
    try {
      return new Intl.NumberFormat("de-DE", {
        style: "currency",
        currency: "EUR",
        maximumFractionDigits: 0
      }).format(value);
    } catch (e) {
      return Math.round(value).toString() + " €";
    }
  }

  function showError(targetEl, message) {
    if (!targetEl) {
      // Fallback, falls Element fehlt
      console.warn("Fehler:", message);
      return;
    }
    targetEl.textContent = message;
    targetEl.style.display = "block";
    targetEl.setAttribute("aria-live", "polite");
  }

  function clearError(targetEl) {
    if (!targetEl) return;
    targetEl.textContent = "";
    targetEl.style.display = "none";
  }

  function clearAllErrors() {
    clearError($("incomeError"));
    clearError($("formError"));
    var inputs = document.querySelectorAll(".cost-form input, .cost-form select");
    inputs.forEach(function (i) {
      i.removeAttribute("aria-invalid");
      i.classList.remove("input-error");
    });
  }

  function setInvalid(inputEl) {
    if (!inputEl) return;
    inputEl.setAttribute("aria-invalid", "true");
    inputEl.classList.add("input-error");
  }

  function validateAndCollect() {
    var errors = [];
    var values = {};

    var incomeEl = $("income");
    var income = getNumber("income");
    if (!incomeEl.value || income <= 0) {
      errors.push({
        field: "income",
        message: "Bitte gib ein monatliches Einkommen größer als 0 ein."
      });
      setInvalid(incomeEl);
    }
    values.income = income;

    // Kostenfelder einsammeln
    var costFields = ["rent", "food", "transport", "internet", "health", "leisure", "other", "buffer"];
    var totalCosts = 0;
    var warnings = [];

    costFields.forEach(function (id) {
      var v = getNumber(id);
      values[id] = v;
      totalCosts += v;
      // Miete wird stadt-spezifisch geprüft, alles andere hat fixe Grenzen
      if (id === "rent") {
        var cityInfo = CITY_DATA[city] || CITY_DATA["Andere Region"];
        if (v > cityInfo.rentCeil) {
          warnings.push(
            FIELD_LABELS[id] + " wirkt für " + cityInfo.label + " ungewöhnlich hoch " +
            "(über " + formatEuro(cityInfo.rentCeil) + " / Monat, inkl. Nebenkosten)."
          );
        }
      } else if (PLAUSIBILITY_LIMITS[id] && v > PLAUSIBILITY_LIMITS[id]) {
        warnings.push(FIELD_LABELS[id] + " wirkt ungewöhnlich hoch (über " + formatEuro(PLAUSIBILITY_LIMITS[id]) + ").");
      }
    });

    values.totalCosts = totalCosts;
    values.warnings = warnings;

    if (totalCosts === 0 && income > 0) {
      errors.push({
        field: "form",
        message: "Bitte trage mindestens deine Miete oder laufende Kosten ein."
      });
    }

    return { ok: errors.length === 0, errors: errors, values: values };
  }

  function getCity() {
    var cityEl = $("city");
    return cityEl ? cityEl.value : "Andere Region";
  }

  function getCityFactor(city) {
    if (Object.prototype.hasOwnProperty.call(CITY_DATA, city)) {
      return CITY_DATA[city].factor;
    }
    return CITY_DATA["Andere Region"].factor;
  }

  function getCityInfo(city) {
    return CITY_DATA[city] || CITY_DATA["Andere Region"];
  }

  function showResult(data) {
    var resultBox = $("resultBox");
    var resultTitle = $("resultTitle");
    var totalCostsEl = $("totalCosts");
    var incomeResult = $("incomeResult");
    var balanceResult = $("balanceResult");
    var minimumIncome = $("minimumIncome");
    var riskBadge = $("riskBadge");
    var resultText = $("resultText");

    if (!resultBox || !resultTitle || !totalCostsEl || !incomeResult ||
        !balanceResult || !minimumIncome || !riskBadge || !resultText) {
      console.error("Ergebnis-Elemente fehlen im DOM.");
      return;
    }

    resultBox.classList.remove("hidden");
    resultBox.setAttribute("aria-live", "polite");

    // Stadtfaktor-Hinweis im Titel
    var cityLabel = data.city;
    if (data.cityFactor && data.cityFactor !== 1) {
      cityLabel += " (Faktor ×" + data.cityFactor.toFixed(2).replace(".", ",") + ")";
    }
    resultTitle.textContent = "Dein Ergebnis für " + cityLabel;

    totalCostsEl.textContent = formatEuro(data.totalCosts);
    incomeResult.textContent = formatEuro(data.income);
    balanceResult.textContent = formatEuro(data.balance);
    minimumIncome.textContent = formatEuro(data.minimumIncome);

    // Risiko-Badge zurücksetzen
    riskBadge.className = "risk-badge";

    var balance = data.balance;
    var badgeText, badgeClass, descriptionText;

    if (balance >= 300) {
      badgeText = "GRÜN — grundsätzlich machbar";
      badgeClass = "risk-green";
      descriptionText =
        "Dein Plan wirkt grundsätzlich machbar. Du hast nach deinen Angaben genug Spielraum. " +
        "Trotzdem solltest du vor einem echten Umzug mindestens 2–3 Monatskosten als Puffer " +
        "aufbauen und deine Einnahmen stabilisieren.";
    } else if (balance >= 0) {
      badgeText = "GELB — knapp kalkuliert";
      badgeClass = "risk-yellow";
      descriptionText =
        "Dein Plan ist nicht unmöglich, aber knapp. Kleine Preissteigerungen, Kaution, " +
        "Krankheit, Technikprobleme oder Einnahmeausfälle könnten dich schnell unter Druck " +
        "setzen. Baue mehr Puffer auf oder senke Fixkosten.";
    } else {
      badgeText = "ROT — aktuell zu riskant";
      badgeClass = "risk-red";
      descriptionText =
        "Dein Plan ist mit diesen Zahlen aktuell zu riskant. Deine monatlichen Kosten liegen " +
        "über deinem Einkommen. Du brauchst entweder mehr Einkommen, niedrigere Fixkosten, " +
        "einen sicheren Übergangsplan oder mehr Rücklagen.";
    }

    riskBadge.textContent = badgeText;
    riskBadge.classList.add(badgeClass);
    resultText.textContent = descriptionText;

    // Standort-Hinweis anhängen — immer, mit konkreter Faktor-Erklärung
    var cityInfo = getCityInfo(data.city);
    var oldNote = resultBox.querySelector(".city-note");
    if (oldNote) oldNote.remove();

    var cityNote = document.createElement("div");
    cityNote.className = "city-note";
    var factorStr = cityInfo.factor.toFixed(2).replace(".", ",");
    cityNote.innerHTML =
      "<strong>Standort-Faktor für " + cityInfo.label + ":</strong> ×" + factorStr +
      " — " + cityInfo.description + ". " +
      "Berechnungsmethode: gewichteter Mittelwert aus Mieten (40 %), Lebensmittel (20 %), " +
      "Freizeit (20 %), Transport (10 %) und Energie (10 %). " +
      "Quellen: Numbeo Cost of Living Index 2024, Osservatorio Immobiliare Nomisma 2024, " +
      "ISTAT Verbraucherpreise 2024. Nur als Orientierung.";
    resultBox.querySelector(".result-text").insertAdjacentElement("afterend", cityNote);

    // Warnungen anhängen
    if (data.warnings && data.warnings.length > 0) {
      var warnBox = document.createElement("div");
      warnBox.className = "warning-box";
      warnBox.setAttribute("role", "status");
      var warnList = document.createElement("ul");
      data.warnings.forEach(function (w) {
        var li = document.createElement("li");
        li.textContent = w;
        warnList.appendChild(li);
      });
      warnBox.innerHTML = "<strong>Bitte prüfen:</strong>";
      warnBox.appendChild(warnList);
      var oldWarn = resultBox.querySelector(".warning-box");
      if (oldWarn) oldWarn.remove();
      resultBox.appendChild(warnBox);
    } else {
      var oldWarn = resultBox.querySelector(".warning-box");
      if (oldWarn) oldWarn.remove();
    }

    // Sanftes Scrollen
    try {
      resultBox.scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (e) {
      resultBox.scrollIntoView();
    }
  }

  function init() {
    var form = $("costForm");
    if (!form) {
      // Kein Rechner auf dieser Seite — Skript sauber beenden
      return;
    }

    // Live-Validierung: Fehler verschwinden, sobald der Nutzer tippt
    var incomeEl = $("income");
    if (incomeEl) {
      incomeEl.addEventListener("input", function () {
        if (incomeEl.value && parseFloat(incomeEl.value) > 0) {
          clearError($("incomeError"));
          incomeEl.removeAttribute("aria-invalid");
          incomeEl.classList.remove("input-error");
        }
      });
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      clearAllErrors();

      var result = validateAndCollect();
      var incomeError = $("incomeError");
      var formError = $("formError");

      if (!result.ok) {
        // Ersten Fehler anzeigen, der Rest bleibt im errors-Array für später
        var first = result.errors[0];
        if (first.field === "income") {
          showError(incomeError, first.message);
          if (incomeEl) incomeEl.focus();
        } else if (first.field === "form") {
          showError(formError, first.message);
        }
        // Ergebnis-Box verstecken, wenn Validierung fehlschlägt
        var resultBox = $("resultBox");
        if (resultBox) resultBox.classList.add("hidden");
        return;
      }

      // Warnungen im formError-Bereich anzeigen, aber Berechnung trotzdem ausführen
      if (result.values.warnings && result.values.warnings.length > 0) {
        showError(formError, "Hinweis: " + result.values.warnings[0] +
          " (Berechnung wird trotzdem durchgeführt.)");
      }

      var city = getCity();
      var cityFactor = getCityFactor(city);
      var totalCosts = result.values.totalCosts;
      var balance = result.values.income - totalCosts;
      var minimumIncome = Math.ceil(totalCosts * 1.2 * cityFactor);

      showResult({
        city: city,
        cityFactor: cityFactor,
        income: result.values.income,
        totalCosts: totalCosts,
        balance: balance,
        minimumIncome: minimumIncome,
        warnings: result.values.warnings
      });
    });

    // Stadt-Wechsel: Hinweis aktualisieren, ohne Ergebnis neu zu rendern
    var citySelect = $("city");
    if (citySelect) {
      citySelect.addEventListener("change", function () {
        var info = getCityInfo(citySelect.value);
        // Kein Live-Refresh — Eingaben werden beim nächsten Submit verarbeitet.
        // Nur visuelles Feedback, dass Stadt erfasst wurde:
        citySelect.setAttribute("data-factor", info.factor.toFixed(2));
      });
    }

    form.addEventListener("reset", function () {
      var resultBox = $("resultBox");
      if (resultBox) {
        resultBox.classList.add("hidden");
      }
      clearAllErrors();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
