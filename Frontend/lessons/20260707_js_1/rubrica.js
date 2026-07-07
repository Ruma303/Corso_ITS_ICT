let nomeSporco = " mario ", email = "mario@example.com";
let telefono = "", note = null;

let nomeNormalizzato = nomeSporco.trim();
nomeNormalizzato = nomeNormalizzato[0].toUpperCase() + nomeNormalizzato.slice(1).toLowerCase()

let isMailValid = false;
if (email.includes("@") && email.split("@").length == 2) {
  isMailValid = true;
}

let telNormalizzato = telefono || "non fornito";

let noteNormalizzate = note ?? "nessuna nota";

let campi = 0
if (nomeSporco !== "") campi++;
if (email) campi++;
if (telefono !== "") campi++;

let stato = (campi >= 2) ? "completo" : "incompleto";

let haNote = Boolean(noteNormalizzate);

let riepilogo = `
Stato utente: ${stato}

Nome : ${nomeNormalizzato},
Email : ${email},
Telefono : ${telNormalizzato},
Note : ${noteNormalizzate},
`
console.log(riepilogo)
