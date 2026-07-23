const prezzo = 50, sconto = 20;

let riduzioneScontata = Math.floor((sconto * 100) / prezzo);

let prezzoFinale = prezzo - riduzioneScontata;

console.log(`
Prezzo ridotto: ${riduzioneScontata}
Prezzo finale: ${prezzoFinale}`)

if (prezzoFinale < 50) {
  console.log("Ottimo affare!")
} else {
  console.log("Prezzo normale")
}

let spesa = ["pane", "latte", "uova"]
spesa.push("formaggio")
console.log(`La lista della spesa contiene ${spesa.length} elementi`)
for (const item of spesa) {
  console.log(item)
}


let nome = "Michela", voto = 27, assenze = 10;
if (voto >= 18 && assenze < 5) {
  console.log(`Brava ${nome}, sei promossa`);
} else {
  console.log(`${nome} che cazzo però`);
}
