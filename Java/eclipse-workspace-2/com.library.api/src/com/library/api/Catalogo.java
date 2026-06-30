package com.library.api;

import java.util.List;

public interface Catalogo {
	public void aggiungiLibro(Libro libro);
	public void aggiungiLibro(String nomeLibro, String nomeAutore);
	public void stampaCatalogo();
	public Libro cercaLibro(String nomeLibro);
}
