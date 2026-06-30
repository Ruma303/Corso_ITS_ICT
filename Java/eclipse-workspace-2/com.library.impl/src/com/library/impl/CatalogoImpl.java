package com.library.impl;

import java.util.ArrayList;
import java.util.List;

import com.library.api.Catalogo;
import com.library.api.Libro;

public class CatalogoImpl implements Catalogo {
	private List<Libro> libri = new ArrayList<>();

	@Override 
	public void aggiungiLibro(Libro libro) {
		libri.add(libro);
	}
	@Override 
	public void aggiungiLibro(String nomeLibro, String nomeAutore) {
		Libro libro = new Libro(nomeLibro, nomeAutore);
		libri.add(libro);
	}
	
	@Override
	public void stampaCatalogo() {
		
		if (libri != null) return;
		
		for (Libro libro: libri) {
			System.out.println(libro);
		}
	}
	
	@Override 
	public Libro cercaLibro(String nomeLibro) {
		if (libri != null) return null;
		for (Libro libro: libri) {
			if (libro.getTitolo().equalsIgnoreCase(nomeLibro))
				return libro;
		}
		return null;
	}
}
