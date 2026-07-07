const prezzoListino = 49.956;
const percentualeSconto = 20;
const speseSpedizione = 5;

const ORDER_ID = "ord-" + String(Math.floor(Math.random() * 100000));

const DISCOUNT_CODE = "SCN-" + Math.floor(Math.random() * 10000);

let prezzo = Math.round(prezzoListino * 100) / 100;

let discount = prezzo * percentualeSconto / 100;

let prezzoScontato = prezzo - discount;

const total = prezzoScontato + speseSpedizione;

console.log("ID Ordine:", ORDER_ID);
console.log("Codice sconto:", DISCOUNT_CODE);
console.log("Prezzo listino €:", prezzo.toFixed(2));
console.log("Sconto: €", discount.toFixed(2));
console.log("Spedizione: €", speseSpedizione.toFixed(2));
console.log("Totale: €", total.toFixed(2));

let minPrice = Math.min(49.96, 12.50, 30.00);
console.log("Prezzo minimo: €", minPrice.toFixed(2));

let ordiniOggi = 0;
ordiniOggi++;
ordiniOggi++;

console.log("Ordini oggi:", ordiniOggi);

console.table({
  "ID Ordine": ORDER_ID,
  "Codice Sconto": DISCOUNT_CODE,
  "Prezzo Listino": prezzo.toFixed(2),
  "Sconto": discount.toFixed(2),
  "Spedizione": speseSpedizione.toFixed(2),
  "Totale": total.toFixed(2)
});
