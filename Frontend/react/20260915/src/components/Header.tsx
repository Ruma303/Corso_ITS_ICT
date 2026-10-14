export default function Header({user}) {;

  return (
    <header>
      <h1>Sportbook</h1>
      <h2>Ciao {user.nome}</h2>
      <h3>Numero: {user.numero}</h3>
      <p>Età: {user.eta}</p>
      <p>Numero fortunato: {user.numero * 2.3}</p>
    </header>
  );
  
}