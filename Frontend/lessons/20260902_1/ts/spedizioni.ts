type StatoSpedizione =
    | "in-transito"
    | "giacenza"
    | "consegnato"
    | "fallito";

type Spedizione = {
    id: string;
    destinatario: string;
    citta: string;
    stato: StatoSpedizione;
};

const spedizioni: Spedizione[] = [
    {
        id: "1",
        destinatario: "Tizio 1",
        citta: "Roma",
        stato: "in-transito",
    },
    {
        id: "2",
        destinatario: "Tizio 2",
        citta: "Genova",
        stato: "fallito",
    },
    {
        id: "3",
        destinatario: "Tizio 3",
        citta: "Palermo",
        stato: "consegnato",
    },
    {
        id: "4",
        destinatario: "Tizio 4",
        citta: "Milano",
        stato: "giacenza",
    },
];

function descriviSpedizione(s: Spedizione): string {
    if (s.stato === "in-transito") {
        return "Spedizione in transito";
    } else if (s.stato === "giacenza") {
        return "Spedizione in giacenza";
    } else if (s.stato === "consegnato") {
        return "Spedizione consegnata";
    } else if (s.stato === "fallito") {
        return "Spedizione fallita";
    } else {
        return "Stato sconosciuto";
    }
}

function spedizioniInGiacenza(
    spedizioni: Spedizione[],
): Spedizione[] {
    const risultato: Spedizione[] = [];

    for (const sp of spedizioni) {
        if (sp.stato === "giacenza") {
            risultato.push(sp);
        }
    }

    return risultato;
}

const inGiacenza = spedizioniInGiacenza(spedizioni);
console.log(inGiacenza);

const testSpedizione = spedizioni[2]!; // Uso asserzione !
console.log(descriviSpedizione(testSpedizione));

// Test errati
// testSpedizione.stato = "in transit";
// testSpedizione.stato = "Consegnato";

// Test corretti
testSpedizione.stato = "in-transito";
testSpedizione.stato = "consegnato";