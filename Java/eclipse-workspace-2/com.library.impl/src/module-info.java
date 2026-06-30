module com.library.impl {
    // Aggiungi transitive qui
    requires transitive com.library.api; 
    
    exports com.library.impl; 
    
    provides com.library.api.Catalogo with com.library.impl.CatalogoImpl;
}