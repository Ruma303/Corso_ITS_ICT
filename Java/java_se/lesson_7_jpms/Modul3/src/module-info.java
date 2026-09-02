module com.library.impl {
    // Abbiamo bisogno dell'API per poter implementare l'interfaccia
    requires com.library.api;
    
    // ======================================================================
    // APPROCCIO 1: STATICO (Senza Service Loader)
    // Decommentare la riga sotto per permettere l'uso di "new CatalogoImpl()"
    // ======================================================================
    // exports com.library.impl;
    
    // ======================================================================
    // APPROCCIO 2: DINAMICO (Con Service Loader) - CONSIGLIATO
    // Dichiariamo che forniamo il servizio "Catalogo" tramite due classi.
    // NOTA: In questo approccio, le classi restano INVISIBILI dall'esterno!
    // ======================================================================
    provides com.library.api.Catalogo
        with com.library.impl.CatalogoImpl, com.library.impl.CatalogoImpl2;
}