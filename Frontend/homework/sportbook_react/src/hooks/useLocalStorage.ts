import { useEffect, useState } from "react";

/**
 * Come useState, ma il valore viene salvato in localStorage
 * e ripristinato al primo render (es. dopo un refresh della pagina).
 */
export default function useLocalStorage<T>(key: string, initialValue: T) {
  // Inizializzazione "lazy": la funzione viene eseguita una sola volta, al primo render
  const [value, setValue] = useState<T>(() => {
    try {
      const saved = localStorage.getItem(key);
      return saved !== null ? (JSON.parse(saved) as T) : initialValue;
    } catch {
      return initialValue;
    }
  });

  // Effetto collaterale: sincronizza lo stato con un sistema esterno (il browser)
  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue] as const;
}
