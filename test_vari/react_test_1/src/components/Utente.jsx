export default function Utente(props) {
  const {
    name,
    email,
    birthdate,
    adult,
    genre,
    bio,
    age
  } = props.utente;

  return (
    <div>
      <h3>Dati Utente Creato:</h3>
      <p><strong>Nome:</strong> {name}</p>
      <p><strong>Email:</strong> {email}</p>
      <p><strong>Data nascita:</strong> {birthdate}</p>
      <p><strong>Età:</strong> {age}</p>
      <p><strong>Adulto:</strong> {adult ? 'Sì' : 'No'}</p>
      <p><strong>Genere:</strong> {genre}</p>
      <p><strong>Bio:</strong> {bio}</p>
    </div>
  );
}