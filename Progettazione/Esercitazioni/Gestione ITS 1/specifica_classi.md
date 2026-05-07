# Specifica della classe CodiceFiscale

CodiceFiscale: String ~ /^[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]$/i





# Approfondimenti Regex Codice Fiscale
^
[A-Z]{6}          → cognome (3) + nome (3)
\d{2}             → anno nascita
[ABCDEHLMPRST]    → mese (solo queste 12 lettere, una per mese)
\d{2}             → giorno/sesso (01-31 o 41-71)
[A-Z]             → lettera del codice comune (es. F=Roma, L=Milano)
\d{3}             → cifre del codice comune
[A-Z]             → check digit
$
