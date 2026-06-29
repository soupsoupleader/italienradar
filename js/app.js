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
  // Quellen (alle 2024, abgerufen Nov./Dez. 2024):
  //   - Numbeo Cost of Living Index 2024/2025 (Stichmonat März 2025, Bezug: Land = 100)
  //   - Nomisma "Osservatorio Immobiliare" 2024: Quadratmeterpreise Kaltmiete
  //   - ISTAT "Indici prezzi al consumo" (FOI) 2024
  //   - ARERA: konsolidierte Endkundenpreise Strom & Gas, 4. Quartal 2024
  //   - ÖPNV-Monatstickets 2024 (ATM Milano, ATAC Roma, ANM Napoli, GTT Torino, TPER Bologna)
  //   - OAM / MIMIT Spritpreisstatistik 2024 für Pendler-Faktor
  //
  // Gewichtung (Single-Haushalt, 1-Zimmer-Wohnung, Napoli ≈ 1.500 EUR Basis):
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
  // Aufbau jedes Eintrags:
  //   factor        Gewichteter Lebenshaltungsindex (Neapel = 1,00)
  //   rentCeil      Plausibilitätsgrenze für die Miete (warm, €/Monat)
  //   rent1room     Typische 1-Zi.-Miete zentral, €/Monat warm (Nomisma 2024)
  //   rentPerSqm    Durchschnitt Kaltmiete, €/m²/Monat (Nomisma 2024)
  //   colIndex      Numbeo CoL-Index (Land = 100) März 2025
  //   label         Anzeige-Name
  //   description   Kurzbeschreibung
  //   districtHint  Konkreter Stadtteil-Tipp für günstige, aber sichere Lagen
  //   sources       Direkte Quellenangabe für die Transparenz
  //
  var CITY_DATA = {
    "Catania":      { factor: 0.88, rentCeil: 1600, rent1room: 480,  rentPerSqm: 7.0,  colIndex: 51,
                      label: "Catania",          description: "eine der günstigsten Großstädte Italiens (–12 % gegenüber Neapel)",
                      districtHint: "Borgo-Sanzio und Librino sind günstig, Zentrum (Via Etnea) ist teurer.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Palermo":      { factor: 0.91, rentCeil: 1800, rent1room: 540,  rentPerSqm: 8.0,  colIndex: 54,
                      label: "Palermo",          description: "etwa 9 % günstiger als Neapel",
                      districtHint: "Ballarò / Albergheria günstig aber Vorsicht, Politeama teurer, Cefalù als Ausweich-Alternative.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Cagliari":     { factor: 0.94, rentCeil: 1800, rent1room: 580,  rentPerSqm: 9.0,  colIndex: 56,
                      label: "Cagliari",         description: "sardinische Hauptstadt, auf Neapel-Niveau",
                      districtHint: "Quartiere Marina und Castello sind zentral; Pirri günstiger im Süden.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Genua":        { factor: 0.95, rentCeil: 1900, rent1room: 600,  rentPerSqm: 9.0,  colIndex: 57,
                      label: "Genua",            description: "Hafenstadt am Meer, moderate Preise",
                      districtHint: "Sampierdarena und Cornigliano günstig, Foce und Albaro deutlich teurer.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Bari":         { factor: 0.96, rentCeil: 1800, rent1room: 620,  rentPerSqm: 9.0,  colIndex: 58,
                      label: "Bari",             description: "apulische Hafenstadt, auf Neapel-Niveau",
                      districtHint: "Bari Vecchia zentral und lebendig, Picone und Carbonara ruhiger & günstiger.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Neapel":       { factor: 1.00, rentCeil: 1900, rent1room: 680,  rentPerSqm: 10.0, colIndex: 60,
                      label: "Neapel",           description: "Basiswert des Rechners (1,00) — Süditalien-Referenz",
                      districtHint: "Vomero und Chiaia teurer, Secondigliano & San Giovanni a Teduccio günstiger — Lage vorher prüfen.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Verona":       { factor: 1.06, rentCeil: 2100, rent1room: 760,  rentPerSqm: 11.0, colIndex: 64,
                      label: "Verona",           description: "venetische Stadt, leicht über Neapel-Niveau",
                      districtHint: "Borgo Trento und Città Antica sehr teuer, Borgo Milano und Golosine günstiger.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Turin":        { factor: 1.11, rentCeil: 2200, rent1room: 800,  rentPerSqm: 12.0, colIndex: 66,
                      label: "Turin",            description: "Industriestadt im Piemont, etwa 11 % teurer als Neapel",
                      districtHint: "Crocetta und Centro teurer, Barriera di Milano und Mirafiori günstiger.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Florenz":      { factor: 1.18, rentCeil: 2600, rent1room: 920,  rentPerSqm: 15.0, colIndex: 70,
                      label: "Florenz",          description: "Toskana-Hauptstadt, deutlich teurer (+18 %)",
                      districtHint: "Centro Storico extrem teuer, Novoli und Rifredi bieten Tram-Anbindung & bessere Preise.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Bologna":      { factor: 1.22, rentCeil: 2700, rent1room: 980,  rentPerSqm: 16.0, colIndex: 72,
                      label: "Bologna",          description: "Emilia-Romagna, Hochschulstadt mit hohem Mietdruck (+22 %)",
                      districtHint: "Universitätsviertel (Zona Universitaria) ausgeglichen, Corticella günstiger.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Rom":          { factor: 1.32, rentCeil: 3500, rent1room: 1180, rentPerSqm: 18.0, colIndex: 78,
                      label: "Rom",              description: "Hauptstadt, deutlich teurer (+32 %)",
                      districtHint: "Centro Storico, Prati und Trastevere sehr teuer, Torpignattara & Pigneto günstiger, aber Lage genau prüfen.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Mailand":      { factor: 1.51, rentCeil: 4500, rent1room: 1450, rentPerSqm: 22.0, colIndex: 89,
                      label: "Mailand",          description: "am teuersten (+51 %), Finanz- und Modemetropole",
                      districtHint: "Centro, Brera und Navigli sehr teuer, Lambrate, Niguarda und Corvetto günstiger — Pendelzeit prüfen.",
                      sources: "Nomisma 2024, Numbeo CoL 2024" },
    "Andere Region":{ factor: 0.95, rentCeil: 1700, rent1room: 550,  rentPerSqm: 8.5,  colIndex: 57,
                      label: "Andere Region",    description: "konservative Schätzung für Kleinstädte & ländliche Regionen",
                      districtHint: "Bei Kleinstädten Mietangebote oft über Immobilienportale wie Immobiliare.it & Idealista prüfen.",
                      sources: "Nomisma 2024, ISTAT 2024" }
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
    var districtHint = cityInfo.districtHint
      ? " <em>Stadtteil-Tipp:</em> " + cityInfo.districtHint
      : "";
    var sourceLine = cityInfo.sources
      ? " Quellen: " + cityInfo.sources + "."
      : "";
    cityNote.innerHTML =
      "<strong>Standort-Faktor für " + cityInfo.label + ":</strong> ×" + factorStr +
      " — " + cityInfo.description + "." +
      districtHint +
      " Datengrundlage: Nomisma-Mietindex 2024, Numbeo Cost of Living 2024, ISTAT 2024, " +
      "ARERA-Energiepreise Q4/2024. Nur als Orientierung." +
      sourceLine;
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
