module com.library.app {
    requires com.library.api; // Il Main ha bisogno di conoscere l'interfaccia Catalogo e Libro
    
    // Se usi il ServiceLoader (visto nella foto precedente):
    uses com.library.api.Catalogo; 
}