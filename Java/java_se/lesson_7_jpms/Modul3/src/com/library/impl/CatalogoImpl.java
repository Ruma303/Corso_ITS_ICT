package com.library.impl;

import com.library.api.Catalogo;

public class CatalogoImpl implements Catalogo{
	@Override
	public void aggiungiLibro(String titolo) {
		System.out.println("Aggiunto: " + titolo);
	}
}
