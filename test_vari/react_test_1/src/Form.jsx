import { useState } from 'react';
import { validaForm } from './validazioni';

export default function Form({ children, createUtente }) {
  const formIniziale = {
    name: '',
    email: '',
    birthdate: '',
    adult: false,
    genre: '',
    bio: '',
    age: 0
  };
  const [form, setForm] = useState(formIniziale);
  const [errori, setErrori] = useState({});


  // Funzione per calcolare l'età e aggiornare sia age che restituire se è maggiorenne
  const checkAge = (birthDateString) => {
    if (!birthDateString) return { age: 0, isAdult: false };

    const birthDate = new Date(birthDateString);
    const today = new Date();

    let calculatedAge = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      calculatedAge--;
    }

    return { age: calculatedAge, isAdult: calculatedAge >= 18 };
  };

  function handleChange(e) {
    const { name, type, value, checked } = e.target;
    const val = type === 'checkbox' ? checked : value;

    setForm(prev => {
      const updatedForm = {
        ...prev,
        [name]: val
      };

      // Se cambia la data di nascita, aggiorniamo sia age che adult tramite checkAge
      if (name === 'birthdate') {
        const { age, isAdult } = checkAge(val);
        updatedForm.age = age;
        updatedForm.adult = isAdult;
      }

      return updatedForm;
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Dati inviati:", form);

    // Validazioni
    const errori = validaForm(form);
    setErrori(errori)

    // Se ci sono chiavi nell'oggetto errori, blocca l'invio
    if (Object.keys(errori) != 0) return;

    // Altrimenti, crea utente
    alert(`Account creato con successo per ${form.name}!\nMaggiorenne: ${form.adult ? 'Sì' : 'No'}\nEtà: ${form.age}`);
    createUtente(form); // Invia l'oggetto utente al componente superiore App
    setForm(formIniziale); // Svuotare i campi del form
    setErrori({}); // Pulisce gli errori
  }

  return (
    <>
      <h1>{children}</h1>
      <form onSubmit={handleSubmit}>

        <div>
          <label htmlFor="name-input">Inserisci il tuo nome: </label>
          <input
            id="name-input"
            type="text"
            name="name"
            value={form.name}
            onChange={handleChange}
          />
          {errori.name && <p className="errore" role="alert">{errori.name}</p>}
        </div>

        <div>
          <label htmlFor="email-input">Inserisci la tua email: </label>
          <input
            id="email-input"
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            aria-invalid={errori.email ? true : false}
            aria-describedby={errori.email ? 'errori email' : undefined}
          />
          {errori.email && <p className="errore" role="alert">{errori.email}</p>}
        </div>

        <div>
          <label htmlFor="birthdate-input">Inserisci la tua data di nascita: </label>
          <input
            id="birthdate-input"
            type="date"
            name="birthdate"
            value={form.birthdate}
            onChange={handleChange}
          />
          {errori.birthdate && <p className="errore" role="alert">{errori.birthdate}</p>}
        </div>

        <div>
          <label>Inserisci il tuo genere: </label>
          <label>
            <input
              type="radio"
              name="genre"
              value="Maschio"
              checked={form.genre === "Maschio"}
              onChange={handleChange}
            /> Maschio
          </label>
          <label>
            <input
              type="radio"
              name="genre"
              value="Femmina"
              checked={form.genre === "Femmina"}
              onChange={handleChange}
            /> Femmina
          </label>
          {errori.genre && <p className='errore' role="alert">{errori.genre}</p>}
        </div>

        <div>
          <label htmlFor="bio-input">Inserisci la tua bio: </label>
          <textarea
            id="bio-input"
            name="bio"
            value={form.bio}
            onChange={handleChange}
            rows="5"
            cols="20"
          ></textarea>
        </div>

        <button type="submit">Crea account</button>
      </form>
    </>
  );
}