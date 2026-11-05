
import { useState } from 'react';
import Input from './Input';

const formStruct = {
  titolo: "",
  autore: "",
  annoPubblicazione: null,
  disponibile: null,
  prezzo: null,
  quantita: null
};

const inputConfig = [
  {
    id: "titolo",
    name: "titolo",
    label: "Titolo",
    type: "text",
    placeholder: "Cerca per titolo..."
  },
  {
    id: "autore",
    name: "autore",
    label: "Autore",
    type: "text",
    placeholder: "Cerca per autore..."
  },
  {
    id: "annoPubblicazione",
    name: "annoPubblicazione",
    label: "Anno pubblicazione",
    type: "number",
    min: 0
  },
  {
    id: "prezzo",
    name: "prezzo",
    label: "Prezzo massimo",
    type: "number",
    min: 0,
    step: "0.01"
  },
  {
    id: "quantita",
    name: "quantita",
    label: "Quantità minima",
    type: "number",
    min: 0
  }
];

function valida(form) {
  const errori = {};
  if (!form.titolo === "") errori["titolo"] = "Il titolo non può essere vuoto";
  if (!form.autore === "") errori["autore"] = "L'autore non può essere vuoto";
  return errori;
}

export default function RicercaLibri({ onFiltri, children }) {
  const [form, setForm] = useState(formStruct);

  function resetForm() {
    setForm(formStruct);
    onFiltri(formStruct);
  }

  function handleSubmit(e) {
    e.preventDefault();
    const validati = valida(form)

    onFiltri(validati);
  }

  function handleChange(e) {
    const { name, value, type, checked } = e.target;

    let val = value;

    if (type === "checkbox") {
      val = checked;
    } else if (type === "number") {
      val = value === "" ? null : Number(value);
    }

    setForm(prev => ({
      ...prev,
      [name]: val
    }));
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>{children}</h2>

      {inputConfig.map(input => (
        <Input
          key={input.id}
          {...input}
          value={form[input.name] ?? ""}
          onChange={handleChange}
        />
      ))}

      <section>
        <button type="submit">Cerca</button>
        <button type="button" onClick={resetForm}>
          Resetta Form
        </button>
      </section>
    </form>
  );
}
