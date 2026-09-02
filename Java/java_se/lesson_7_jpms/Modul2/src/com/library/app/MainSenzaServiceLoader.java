package com.library.app;

// import com.library.api.Catalogo;
// import com.library.impl.CatalogoImpl;

// ======================================================================
// APPROCCIO 1: STATICO. 
// Per far funzionare questo codice, decommentare:
// 1. "exports com.library.impl;" nel module-info di Modul3
// 2. "requires com.library.impl;" nel module-info di Modul2
// ======================================================================

/*
public class MainSenzaServiceLoader {
    public static void main(String[] args) {
        System.out.println("Creazione diretta e vecchio stile dell'istanza concreta");
        
        // Accoppiamento forte: la classe Main DEVE conoscere CatalogoImpl a tempo di compilazione
        Catalogo cat = new CatalogoImpl();
        cat.aggiungiLibro("Java 9 Moduli 2");
    }
}
*/