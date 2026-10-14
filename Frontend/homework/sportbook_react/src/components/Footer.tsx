import linkedin from "../assets/linkedin.png";

const anno = new Date().getFullYear();

export default function Footer() {
  return (
    <footer id="contatti" className="bg-dark text-white py-4">
      <div className="container text-center">
        <p className="mb-2">
          Email:{" "}
          <a className="link-light" href="mailto:info@sportbook.it">
            Scrivici
          </a>
        </p>
        <a href="https://www.linkedin.com" target="_blank" rel="noreferrer">
          <img src={linkedin} alt="LinkedIn" width={32} height={32} />
        </a>
        <p className="small text-secondary mt-3 mb-0">
          &copy; {anno} SportBook. Tutti i diritti riservati.
        </p>
      </div>
    </footer>
  );
}
