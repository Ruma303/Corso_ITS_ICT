package com.library.app;

import java.util.ServiceLoader;
import com.library.api.Catalogo; // <--- Importiamo SOLO l'interfaccia

public class MainServiceLoader {

	public static void main(String[] args) {
		// Carichiamo il servizio tramite ServiceLoader (Disaccoppiato)
		ServiceLoader<Catalogo> loader = ServiceLoader.load(Catalogo.class);

		// Prendiamo il primo catalogo disponibile (sarà CatalogoImpl)
		Catalogo cat = loader.findFirst()
				.orElseThrow(() -> new RuntimeException("Nessun modulo di implementazione trovato!"));

		// Usiamo l'interfaccia
		cat.aggiungiLibro("Java 9 Moduli", "Unknown");
		System.out.println("Libro aggiunto con successo!");
	}
}