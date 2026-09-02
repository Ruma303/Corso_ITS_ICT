module com.library.app {
    // Tutti hanno bisogno dell'API per conoscere i metodi da chiamare
    requires com.library.api;
    
    // ======================================================================
    // APPROCCIO 1: STATICO (Per eseguire MainSenzaServiceLoader)
    // Deommentare la riga sotto se vogliamo istanziare le classi direttamente.
    // ======================================================================
    // requires com.library.impl;
    
    // ======================================================================
    // APPROCCIO 2: DINAMICO (Per eseguire MainConServiceLoader)
    // Diciamo a Java che useremo questo servizio tramite ServiceLoader.
    // ======================================================================
    uses com.library.api.Catalogo;
}