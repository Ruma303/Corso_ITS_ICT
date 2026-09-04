type esiti = "promosso" | "rimandato" | "bocciato" ;

class Studente {
  static totaleIscritti: number = 0;

  readonly #matricola: string;
  #nome!: string;
  #voto!: number;

  public constructor(matricola: string, nome: string, voto: number) {
    Studente.totaleIscritti++;
    this.#matricola = matricola;
    this.nome = nome;
    this.voto = voto;
  }

  get matricola(): string {
    return this.#matricola;
  }

  get nome(): string {
    return this.#nome;
  }

  set nome(nuovoNome: string) {
    const nomePulito = nuovoNome.trim();
    if (nomePulito === "") {
      throw new Error("Il nome non può essere vuoto.");
    }
    this.#nome = nomePulito;
  }

  get voto(): number {
    return this.#voto;
  }

  set voto(nuovoVoto: number) {
    if (Number.isNaN(nuovoVoto)) {
      throw new Error("Il voto deve essere un numero valido.");
    }

    if (nuovoVoto < 0) {
      this.#voto = 0;
    } else if (nuovoVoto > 10) {
      this.#voto = 10;
    } else {
      this.#voto = nuovoVoto;
    }
  }

  esito(): esiti {
    if (this.#voto >= 6) return "promosso";
    if (this.#voto >= 4) return "rimandato";
    return "bocciato";
  }

  descrivi(): string {
    return `${this.#nome} (mat. ${this.#matricola}) — voto ${this.#voto}/10: ${this.esito()}`;
  }
}


// TEST
const s1 = new Studente("m1", "Mario", 12);
console.log(s1.descrivi());
s1.voto = -3;
console.log(s1.descrivi());

const s2 = new Studente("m2", "  Luigi  ", 5);
console.log(s2.descrivi());

console.log(`Totale iscritti: ${Studente.totaleIscritti}`);

try {
  new Studente("m3", "Anna", Number("abc"));
} catch (error) {
  if (error instanceof Error) {
    console.log(`Errore catturato con successo: ${error.message}`);
  }
}