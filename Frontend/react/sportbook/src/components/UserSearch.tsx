import { useState } from "react";
import type { FormEvent, ChangeEvent, ReactNode } from "react";
import type Persona from "../types/Persona";
import useSearchPersone from "../hooks/useSearchPersone";
import type { FiltriRicerca } from "../hooks/useSearchPersone";

interface FormState extends FiltriRicerca {
    consenso: boolean;
}

interface UserSearchProps {
    children: ReactNode;
    onSearch: (risultati: Persona[]) => void;
    onReset: () => void;
}

type FormErrors = Partial<Record<keyof FormState, string>>;

export default function UserSearch({ children, onSearch, onReset }: UserSearchProps) {
    const emptyForm: FormState = {
        nome: "",
        cognome: "",
        eta: "",
        sesso: "",
        consenso: false,
    };
    const [form, setForm] = useState<FormState>(emptyForm);
    const [errors, setErrors] = useState<FormErrors>({});
    const { cerca, searching, searchError } = useSearchPersone();

    function validate(data: FormState): FormErrors {
        const newErrors: FormErrors = {};

        if (data.nome.trim() === "") {
            newErrors.nome = "Il nome è obbligatorio";
        }

        if (data.cognome.trim() === "") {
            newErrors.cognome = "Il cognome è obbligatorio";
        }

        if (data.eta !== "") {
            const etaNum = Number(data.eta);
            if (Number.isNaN(etaNum) || etaNum < 18 || etaNum > 100) {
                newErrors.eta =
                    "L'età deve essere un numero tra 18 e 100";
            }
        }

        if (data.sesso === "") {
            newErrors.sesso = "Seleziona il sesso";
        }

        if (!data.consenso) {
            newErrors.consenso =
                "Devi accettare il trattamento dei dati";
        }

        return newErrors;
    }

    async function handleSubmit(e: FormEvent<HTMLFormElement>) {
        e.preventDefault();

        const validationErrors = validate(form);
        setErrors(validationErrors);

        if (Object.keys(validationErrors).length > 0) {
            return; // blocca la ricerca se ci sono errori
        }

        try {
            const risultati = await cerca(form);
            onSearch(risultati);
        } catch {
            // l'errore è già esposto tramite searchError, qui non serve altro
        }
    }

    function handleReset() {
        setForm(emptyForm);
        onReset();
        setErrors({});
        console.log("Form reset effettuato");
    }

    function handleChange(event: ChangeEvent<HTMLInputElement>) {
        // questa funzione si attiva su ogni campo di ogni tipo
        // per indicare quale proprietà deve aggiornare di form
        // va indicata la proprietà dinamicamente usando:
        const { name, value, type, checked } = event.target;

        // Se è una checkbox, va recuperato il booleano dal campo checked
        // Altrimenti, da tutti gli altri campi recuperare value
        let val = type === "checkbox" ? checked : value;

        setForm((prev) => ({
            ...prev,
            [name]: val, // Aggiornamento dinamico della chiave
        }));

        // Rimuove l'errore del campo appena modificato, se presente
        setErrors((prev) => {
            if (!prev[name as keyof FormState]) return prev;
            const { [name as keyof FormState]: _, ...rest } = prev;
            return rest;
        });
    }

    return (
        <>
            <h2 className="mb-4">{children}</h2>
            <small className="alert alert-info">Il form cerca persone confrontando tutti i campi simultaneamente</small>

            <form
                onSubmit={handleSubmit}
                onReset={handleReset}
                noValidate
                className="mt-4"
            >
                <div className="row g-3 mb-3">
                    <div className="col-md-6">
                        <label
                            htmlFor="nameInput"
                            className="form-label"
                        >
                            Nome*:
                        </label>
                        <input
                            type="text"
                            id="nameInput"
                            name="nome"
                            placeholder="Inserisci il tuo nome qui ..."
                            maxLength={20}
                            value={form.nome}
                            onChange={handleChange}
                            className={`form-control ${errors.nome ? "is-invalid" : ""}`}
                            aria-invalid={
                                errors.nome ? true : undefined
                            }
                            aria-describedby={
                                errors.nome
                                    ? "nameInput-error"
                                    : undefined
                            }
                        />
                        {errors.nome && (
                            <div
                                id="nameInput-error"
                                className="invalid-feedback d-block"
                            >
                                {errors.nome}
                            </div>
                        )}
                    </div>

                    <div className="col-md-6">
                        <label
                            htmlFor="cognomeInput"
                            className="form-label"
                        >
                            Cognome*:
                        </label>
                        <input
                            type="text"
                            id="cognomeInput"
                            name="cognome"
                            placeholder="Inserisci il tuo cognome qui..."
                            maxLength={30}
                            value={form.cognome}
                            onChange={handleChange}
                            className={`form-control ${errors.cognome ? "is-invalid" : ""}`}
                            aria-invalid={
                                errors.cognome ? true : undefined
                            }
                            aria-describedby={
                                errors.cognome
                                    ? "cognomeInput-error"
                                    : undefined
                            }
                        />
                        {errors.cognome && (
                            <div
                                id="cognomeInput-error"
                                className="invalid-feedback d-block"
                            >
                                {errors.cognome}
                            </div>
                        )}
                    </div>
                </div>

                <div className="row g-3 mb-3">
                    <div className="col-md-6">
                        <label
                            htmlFor="ageInput"
                            className="form-label"
                        >
                            Età:
                        </label>
                        <input
                            type="number"
                            id="ageInput"
                            name="eta"
                            placeholder="Inserisci la tua età tra 18 e 100"
                            min="18"
                            max="100"
                            value={form.eta}
                            onChange={handleChange}
                            className={`form-control ${errors.eta ? "is-invalid" : ""}`}
                            aria-invalid={
                                errors.eta ? true : undefined
                            }
                            aria-describedby={
                                errors.eta
                                    ? "ageInput-error"
                                    : undefined
                            }
                        />
                        {errors.eta && (
                            <div
                                id="ageInput-error"
                                className="invalid-feedback d-block"
                            >
                                {errors.eta}
                            </div>
                        )}
                    </div>

                    <div className="col-md-6">
                        <fieldset className="border-0 p-0 m-0">
                            <legend className="col-form-label pt-0 fs-6">
                                Sesso*:
                            </legend>
                            <div
                                id="radios"
                                aria-describedby={
                                    errors.sesso
                                        ? "sesso-error"
                                        : undefined
                                }
                            >
                                <div className="genderRadios form-check form-check-inline">
                                    <input
                                        type="radio"
                                        id="genderInputM"
                                        name="sesso"
                                        checked={
                                            form.sesso === "male"
                                        }
                                        onChange={handleChange}
                                        value="male"
                                        className={`form-check-input ${errors.sesso ? "is-invalid" : ""}`}
                                    />
                                    <label
                                        htmlFor="genderInputM"
                                        className="form-check-label ms-2"
                                    >
                                        Maschio
                                    </label>
                                </div>
                                <div className="genderRadios form-check form-check-inline">
                                    <input
                                        type="radio"
                                        id="genderInputF"
                                        name="sesso"
                                        checked={
                                            form.sesso === "female"
                                        }
                                        onChange={handleChange}
                                        value="female"
                                        className={`form-check-input ${errors.sesso ? "is-invalid" : ""}`}
                                    />
                                    <label
                                        htmlFor="genderInputF"
                                        className="form-check-label ms-2"
                                    >
                                        Femmina
                                    </label>
                                </div>
                            </div>
                            {errors.sesso && (
                                <div
                                    id="sesso-error"
                                    className="invalid-feedback d-block"
                                >
                                    {errors.sesso}
                                </div>
                            )}
                        </fieldset>
                    </div>
                </div>

                <fieldset className="border-0 p-0 m-0 mb-4">
                    <legend className="col-form-label pt-0 fs-6">
                        Termini e Condizioni*
                    </legend>
                    <div className="form-check d-flex gap-2">
                        <input
                            type="checkbox"
                            id="agreementInput"
                            name="consenso"
                            checked={form.consenso === true}
                            onChange={handleChange}
                            className={`form-check-input ${errors.consenso ? "is-invalid" : ""}`}
                            aria-invalid={
                                errors.consenso ? true : undefined
                            }
                            aria-describedby={
                                errors.consenso
                                    ? "agreement-error"
                                    : undefined
                            }
                        />
                        <label
                            htmlFor="agreementInput"
                            className="form-check-label"
                        >
                            Accetto il trattamento dei dati
                        </label>
                    </div>
                    {errors.consenso && (
                        <div
                            id="agreement-error"
                            className="invalid-feedback d-block"
                        >
                            {errors.consenso}
                        </div>
                    )}
                </fieldset>
                {searchError && (
                    <div className="alert alert-danger" role="alert">
                        {searchError}
                    </div>
                )}
                <small className="text-danger">*Campi obbligatori</small>

                <div id="buttons" className="d-flex gap-2">
                    <button type="submit" className="btn btn-primary" disabled={searching}>
                        {searching ? "Ricerca in corso..." : "Invia"}
                    </button>
                    <button type="reset" className="btn btn-secondary" disabled={searching}>
                        Reset
                    </button>
                </div>
            </form>
        </>
    );
}
