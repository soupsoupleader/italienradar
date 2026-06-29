document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("costForm");

  if (!form) {
    console.warn("Cost form not found on this page");
    return;
  }

  const requiredFields = ["city", "income", "rent", "food", "transport", "internet", "health", "leisure", "other", "buffer"];
  const allFieldsExist = requiredFields.every(id => document.getElementById(id));
  
  if (!allFieldsExist) {
    console.error("Some required form fields are missing");
    return;
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const city = document.getElementById("city").value;

    const income = getNumber("income");
    const rent = getNumber("rent");
    const food = getNumber("food");
    const transport = getNumber("transport");
    const internet = getNumber("internet");
    const health = getNumber("health");
    const leisure = getNumber("leisure");
    const other = getNumber("other");
    const buffer = getNumber("buffer");

    const incomeInput = document.getElementById("income");
    const incomeError = document.getElementById("incomeError");
    const formError = document.getElementById("formError");

    const cityFactors = {
      Napoli: 1,
      Bari: 1,
      Palermo: 1,
      Rom: 1.25,
      Mailand: 1.35,
      "Andere Region": 1
    };
    const cityFactor = cityFactors[city] || 1;

    if (income === 0) {
      if (incomeError) {
        incomeError.textContent = "Bitte geben Sie Ihr monatliches Einkommen ein.";
        incomeError.style.display = "block";
        incomeInput.focus();
      } else {
        alert("Bitte geben Sie Ihr monatliches Einkommen ein.");
        incomeInput.focus();
      }
      return;
    }

    const totalCosts = rent + food + transport + internet + health + leisure + other + buffer;
    const balance = income - totalCosts;
    const minimumIncome = Math.ceil(totalCosts * 1.2 * cityFactor);

    if (totalCosts === 0) {
      if (formError) {
        formError.textContent = "Bitte tragen Sie mindestens Ihre Miete oder andere laufende Kosten ein.";
        formError.style.display = "block";
      } else {
        alert("Bitte tragen Sie mindestens Ihre Miete oder andere laufende Kosten ein.");
      }
      return;
    }

    const extremeWarnings = [];
    if (rent > 5000) extremeWarnings.push("Miete ist ungewöhnlich hoch.");
    if (food > 2000) extremeWarnings.push("Essen & Lebensmittel sind ungewöhnlich hoch.");
    if (transport > 1500) extremeWarnings.push("Transportkosten sind ungewöhnlich hoch.");
    if (internet > 300) extremeWarnings.push("Handy & Internet sind ungewöhnlich hoch.");
    if (health > 2000) extremeWarnings.push("Gesundheitskosten sind ungewöhnlich hoch.");
    if (leisure > 1500) extremeWarnings.push("Freizeitkosten sind ungewöhnlich hoch.");
    if (other > 2000) extremeWarnings.push("Sonstige Kosten sind ungewöhnlich hoch.");

    if (extremeWarnings.length) {
      if (formError) {
        formError.textContent = "Achtung: " + extremeWarnings[0] + " Bitte prüfen Sie Ihre Angaben.";
        formError.style.display = "block";
      } else {
        alert("Achtung: " + extremeWarnings[0] + " Bitte prüfen Sie Ihre Angaben.");
      }
    }

    showResult({
      city,
      cityFactor,
      income,
      totalCosts,
      balance,
      minimumIncome
    });
  });

  form.addEventListener("reset", function () {
    const resultBox = document.getElementById("resultBox");
    if (resultBox) {
      resultBox.classList.add("hidden");
    }
    // Clear inline errors
    const incomeError = document.getElementById("incomeError");
    const formError = document.getElementById("formError");
    if (incomeError) { incomeError.style.display = "none"; incomeError.textContent = ""; }
    if (formError) { formError.style.display = "none"; formError.textContent = ""; }
  });
});

function getNumber(id) {
  const value = document.getElementById(id).value;
  return Number(value) || 0;
}

function formatEuro(value) {
  return new Intl.NumberFormat("de-DE", {
    style: "currency",
    currency: "EUR",
    maximumFractionDigits: 0
  }).format(value);
}

function showResult(data) {
  const resultBox = document.getElementById("resultBox");
  const resultTitle = document.getElementById("resultTitle");
  const totalCosts = document.getElementById("totalCosts");
  const incomeResult = document.getElementById("incomeResult");
  const balanceResult = document.getElementById("balanceResult");
  const minimumIncome = document.getElementById("minimumIncome");
  const riskBadge = document.getElementById("riskBadge");
  const resultText = document.getElementById("resultText");

  // Validate all result elements exist
  if (!resultBox || !resultTitle || !totalCosts || !incomeResult || !balanceResult || !minimumIncome || !riskBadge || !resultText) {
    console.error("Some result elements are missing from the DOM");
    return;
  }

  resultBox.classList.remove("hidden");

  resultTitle.textContent = `Dein Ergebnis für ${data.city}`;
  totalCosts.textContent = formatEuro(data.totalCosts);
  incomeResult.textContent = formatEuro(data.income);
  balanceResult.textContent = formatEuro(data.balance);
  minimumIncome.textContent = formatEuro(data.minimumIncome);

  riskBadge.className = "risk-badge";

  if (data.balance >= 300) {
    riskBadge.textContent = "GRÜN — grundsätzlich machbar";
    riskBadge.classList.add("risk-green");

    resultText.textContent =
      "Dein Plan wirkt grundsätzlich machbar. Du hast nach deinen Angaben genug Spielraum. Trotzdem solltest du vor einem echten Umzug mindestens 2–3 Monatskosten als Puffer aufbauen und deine Einnahmen stabilisieren.";
  } else if (data.balance >= 0) {
    riskBadge.textContent = "GELB — knapp kalkuliert";
    riskBadge.classList.add("risk-yellow");

    resultText.textContent =
      "Dein Plan ist nicht unmöglich, aber knapp. Kleine Preissteigerungen, Kaution, Krankheit, Technikprobleme oder Einnahmeausfälle könnten dich schnell unter Druck setzen. Baue mehr Puffer auf oder senke Fixkosten.";
  } else {
    riskBadge.textContent = "ROT — aktuell zu riskant";
    riskBadge.classList.add("risk-red");

    resultText.textContent =
      "Dein Plan ist mit diesen Zahlen aktuell zu riskant. Deine monatlichen Kosten liegen über deinem Einkommen. Du brauchst entweder mehr Einkommen, niedrigere Fixkosten, einen sicheren Übergangsplan oder mehr Rücklagen.";
  }

  resultBox.scrollIntoView({
    behavior: "smooth",
    block: "start"
  });

  const incomeError = document.getElementById("incomeError");
  const formError = document.getElementById("formError");
  if (incomeError) { incomeError.style.display = "none"; incomeError.textContent = ""; }
  if (formError) { formError.style.display = "none"; formError.textContent = ""; }
}