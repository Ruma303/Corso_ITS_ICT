// Data di oggi nel formato YYYY-MM-DD, nel fuso orario LOCALE
// (toISOString() userebbe UTC e tra mezzanotte e le 2 darebbe "ieri" in Italia)
export const oggiISO = () => new Date().toLocaleDateString("sv-SE");

// "2026-07-01" -> "01/07/2026"
export const formattaData = (iso: string) => iso.split("-").reverse().join("/");