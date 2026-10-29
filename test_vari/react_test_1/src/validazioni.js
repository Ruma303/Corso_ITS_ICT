// Validazione form
function validaForm(formDati) {
    const err = {};

    // Corretto da "nome" a "name"
    if (!formDati.name || formDati.name.trim().length < 3) {
        err.name = "Nome troppo corto. Almeno 3 caratteri";
    }

    if (
        !formDati.email ||
        !formDati.email.includes("@") ||
        !formDati.email.includes(".")
    ) {
        err.email = "Email non valida";
    }

    // Corretto da "form.data" a "err.birthdate"
    if (!formDati.birthdate) {
        err.birthdate = "Inserisci una data di nascita";
    }

    if (new Date(formDati.birthdate).getTime() > Date.now()) {
        err.birthdate =
            "Non puoi inserire una data di nascita nel futuro";
    }

    if (!formDati.genre || formDati.genre.trim() === "") {
        err.genre = "Indicare un genere";
    }

    return err;
}

export { validaForm };
