package com.library.app;

import java.util.ServiceLoader;
import com.library.api.Catalogo;

// NOTA BENE: Nessun import da com.library.impl! Il disaccoppiamento è totale.

public class MainConServiceLoader {

	public static void main(String[] args) {
		System.out.println("Creazione dinamica tramite ServiceLoader");

		// 1. Chiediamo al ServiceLoader di cercare tutti i moduli che forniscono "Catalogo"
		ServiceLoader<Catalogo> loader = ServiceLoader.load(Catalogo.class);

		// 2. Opzione A: Eseguiamo il metodo su TUTTE le implementazioni trovate (le proverà entrambe)
		System.out.println("\n--- Ciclare su tutte le implementazioni trovate ---");
		for (Catalogo cat : loader) {
			cat.aggiungiLibro("Java 9 Moduli 2");
		}

		// 3. Opzione B: Se servisse solo una specifica, prendere la prima disponibile
		System.out.println("\n--- Usare della prima implementazione disponibile ---");
		Catalogo singolaIstanza = loader.findFirst()
				.orElseThrow(() -> new RuntimeException("Nessun modulo di implementazione trovato!"));
		
		singolaIstanza.aggiungiLibro("Esempio Singolo");
	}
}