module com.library.app {
	requires com.library.api;
	
	// DA RIMUOVERE (o commentare) vogliamo il vero disaccoppiamento:
	// requires com.library.impl; // Utilizzare senza ServiceLoader
	
	// Da usare solo con ServiceLoader
	uses com.library.api.Catalogo;
}