module com.library.impl {
	requires com.library.api;
	
	// Senza Service Loader
	//exports com.library.impl;
	
	// Con Service Loader
	provides com.library.api.Catalogo
	with com.library.impl.CatalogoImpl, com.library.impl.CatalogoImpl2;	
}