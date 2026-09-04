const form = document.getElementById("form");
const resetBtn = document.querySelector('button[type="reset"]');
const resultSection = document.getElementById("result-section");
const tbody = document.getElementById("tbody-result");

let risultati = [];

// 1. Caricamento dati JSON
const caricaDati = async () => {
  console.log("Caricamento dati...")
  try {
    const response = await fetch("persone.json");
    if (!response.ok) throw new Error("Errore nella richiesta");

    const data = await response.json();
    if (!Array.isArray(data) || data.length === 0) {
      throw new Error("Non sono presenti dati in persone.json");
    }

    risultati = data.filter(validaDati);

  } catch (e) {
    console.error("Errore nel caricamento dei dati:", e);
  }
};

// 2. Validazione dati JSON (Proprietà dell'oggetto)
function validaDati(person) {
  if (!person || typeof person !== "object") return false;

  const { nome, cognome, eta, sesso } = person;

  const isNomeValid = typeof nome === "string" && nome.trim() !== "";
  const isCognomeValid = typeof cognome === "string" && cognome.trim() !== "";
  const isEtaValid = typeof eta === "number" && eta >= 18 && eta <= 100;
  const isSessoValid = typeof sesso === "string" && ["male", "female"].includes(sesso.toLowerCase().trim());

  return isNomeValid && isCognomeValid && isEtaValid && isSessoValid;
}

// 3. Recupero da Form
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(form);

  const filtri = {
    nome: formData.get("nome")?.toString().trim().toLowerCase() || "",
    cognome: formData.get("cognome")?.toString().trim().toLowerCase() || "",
    eta: formData.get("eta") ? Number(formData.get("eta")) : null,
    sesso: formData.get("sesso")?.toString().trim().toLowerCase() || ""
  };

  const trovati = risultatiFiltrati(filtri);
  creaRisultati(trovati);
});

// 4. Filtrare i dati JSON validati con i criteri del Form
const risultatiFiltrati = (filtri) => {
  return risultati.filter((person) => {
    // Se il filtro è vuoto, la condizione è sempre true (non applica il filtro)
    const matchNome = !filtri.nome || person.nome.toLowerCase().includes(filtri.nome);
    const matchCognome = !filtri.cognome || person.cognome.toLowerCase().includes(filtri.cognome);
    const matchEta = filtri.eta === null || person.eta === filtri.eta;
    const matchSesso = !filtri.sesso || person.sesso.toLowerCase() === filtri.sesso;

    return matchNome && matchCognome && matchEta && matchSesso;
  });
};

// 5. Rendering risultati in HTML
function creaRisultati(data) {

  tbody.replaceChildren();

  data.forEach((obj) => {
    const row = document.createElement("tr");

    const tdNome = document.createElement("td");
    const tdCognome = document.createElement("td");
    const tdEta = document.createElement("td");
    const tdSesso = document.createElement("td");
    const tdTelefono = document.createElement("td");

    tdNome.textContent = obj.nome ?? "";
    tdCognome.textContent = obj.cognome ?? "";
    tdEta.textContent = obj.eta ?? "";

    const sesso = ((obj.sesso === "male") ? "Maschio" : "Femmina") ?? ""
    tdSesso.textContent = sesso;

    tdTelefono.textContent = obj.telefono ?? "";

    row.append(tdNome, tdCognome, tdEta, tdSesso, tdTelefono);
    tbody.appendChild(row);
  });

  if (resultSection) {
    resultSection.classList.remove("hidden");
  }
}

// 6. Reset del form
resetBtn.addEventListener("click", () => {
  tbody.replaceChildren();

  if (resultSection) {
    resultSection.classList.add("hidden");
  }

  console.log("Form reset effettuato");
});


// Inizio esecuzione
caricaDati();