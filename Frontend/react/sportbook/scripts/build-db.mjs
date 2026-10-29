// scripts/build-db.mjs
import { readFile, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const sorgente = path.join(__dirname, "..", "src", "data", "persone.json");
const destinazione = path.join(__dirname, "..", "db.json");

const raw = await readFile(sorgente, "utf-8");
const persone = JSON.parse(raw);

const personeConId = persone.map((persona, index) => ({
  id: index + 1,
  ...persona,
}));

const db = { persone: personeConId };

await writeFile(destinazione, JSON.stringify(db, null, 2), "utf-8");
console.log(`db.json generato con ${personeConId.length} persone.`);