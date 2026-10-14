import { useState } from "react";
import type { FormEvent, ChangeEvent } from "react";
import type Persona from "../types/Persona";

interface FormState {
  nome: string;
  cognome: string;
  eta: string;
  sesso: string;
}

interface UserSearchProps {
  persone: Persona[];
  onSearch: (risultati: Persona[]) => void;
  onReset: () => void;
}

export default function UserSearch({
  persone,
  onSearch,
  onReset,
}: UserSearchProps) {

  const emptyForm: FormState = { nome: '', cognome: '', eta: '', sesso: '' };
  const [form, setForm] = useState<FormState>(emptyForm);
  
  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    onSearch(risultatiFiltrati(persone, form));
  }

  function handleReset() {
    setForm({ nome: '', cognome: '', eta: '', sesso: '' });
    onReset();
    console.log("Form reset effettuato");
  }

  function handleChange(event: ChangeEvent<HTMLInputElement>) {    
    // questa funzione si attiva su ogni campo di ogni tipo
    // per indicare quale proprietà deve aggiornare di form
    // va indicata la proprietà dinamicamente usando:
    const { name, value } = event.target;
    setForm(prev => ({...prev,[name]: value}));
  }
  
  return (
    <>
      <h2>Form di ricerca</h2>
      <form onSubmit={handleSubmit} onReset={handleReset}>
        <label htmlFor="nameInput">Nome:</label>
        <input
          type="text"
          id="nameInput"
          name="nome"
          placeholder="Inserisci il tuo nome qui ..."
          maxLength={20}
          value={form.nome}
          onChange={handleChange}
        />

        <label htmlFor="cognomeInput">Cognome:</label>
        <input
          type="text"
          id="cognomeInput"
          name="cognome"
          placeholder="Inserisci il tuo cognome qui..."
          maxLength={30}
          value={form.cognome}
          onChange={handleChange}
        />

        <label htmlFor="ageInput">Età:</label>
        <input
          type="number"
          id="ageInput"
          name="eta"
          placeholder="Inserisci la tua età tra 18 e 100"
          min="18"
          max="100"
          value={form.eta}
          onChange={handleChange}
        />

        <fieldset>
          <legend>Sesso:</legend>
          <div id="radios">
            <div className="genderRadios">
              <label htmlFor="genderInputM">Maschio:</label>
              <input
                type="radio"
                id="genderInputM"
                name="sesso"
                checked={form.sesso === "male"}
                onChange={handleChange}
                value="male"
              />
            </div>
            <div className="genderRadios">
              <label htmlFor="genderInputF">Femmina:</label>
              <input
                type="radio"
                id="genderInputF"
                name="sesso"
                checked={form.sesso === "female"}
                onChange={handleChange}
                value="female"
              />
            </div>
          </div>
        </fieldset>

        <div id="buttons">
          <button type="submit">Invia</button>
          <button type="reset">Reset</button>
        </div>
      </form>
    </>
  );
}

function risultatiFiltrati(persone: Persona[], filtri: FormState): Persona[] {
  return persone.filter((person) => {
    const matchNome =
      !filtri.nome || person.nome.toLowerCase().includes(filtri.nome);
    const matchCognome =
      !filtri.cognome || person.cognome.toLowerCase().includes(filtri.cognome);
    const matchEta = !filtri.eta || person.eta === Number(filtri.eta);
    const matchSesso =
      !filtri.sesso || person.sesso.toLowerCase() === filtri.sesso;

    return matchNome && matchCognome && matchEta && matchSesso;
  });
}
