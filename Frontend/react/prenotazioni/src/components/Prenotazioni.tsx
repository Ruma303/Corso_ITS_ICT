export default function Prenotazioni({ prenotazioni, removePrenotazione}) {  
  return (
    <section>
      <h2>Prenotazioni</h2>
      {prenotazioni.length === 0 && <p>Nessuna prenotazione</p>}
      <ul>
        {prenotazioni.map((p) => (
          <li key={p.id}>
            {p.campo} - {p.ora.toLocaleTimeString()}
            <button onClick={() => removePrenotazione(p.id)}>Rimuovi</button>
          </li>
        ))}
      </ul>
    </section>
  );
}