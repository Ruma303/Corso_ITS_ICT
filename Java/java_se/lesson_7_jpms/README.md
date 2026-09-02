# Struttura base

```
lesson_7_jpms % tree .
.
├── codice.md
├── Modul1
│   ├── Modul1.iml
│   └── src
│       ├── com
│       │   └── library
│       │       └── api
│       │           ├── Catalogo.java
│       │           └── package-info.java
│       └── module-info.java
├── Modul2
│   ├── Modul2.iml
│   └── src
│       ├── com
│       │   └── library
│       │       └── app
│       │           ├── MainConServiceLoader.java
│       │           ├── MainSenzaServiceLoader.java
│       │           └── package-info.java
│       └── module-info.java
└── Modul3
    ├── Modul3.iml
    └── src
        ├── com
        │   └── library
        │       └── impl
        │           ├── CatalogoImpl.java
        │           ├── CatalogoImpl2.java
        │           └── package-info.java
        └── module-info.java
```

# Con ServiceLoader

>Spostarsi al branch: "con_ServiceLoader"

---

## Modul1

### package-info.java

```java
package com.library.api;
```

### module-info.java

```java
module com.library.api {
	exports com.library.api; // Errore: The package com.library.api does not exist or is empty
}
```

### Catalogo.java

```java
package com.library.api;

public interface Catalogo {
	void aggiungiLibro(String titolo);
}
```

### Modul1.iml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$">
      <sourceFolder url="file://$MODULE_DIR$/src" isTestSource="false" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>
```

---

## Modul2

### package-info.java

```java
package com.library.app;
```

### module-info.java

```java
module com.library.app {
    // Tutti hanno bisogno dell'API per conoscere i metodi da chiamare
    requires com.library.api; // Errore: com.library.api cannot be resolved to a module (Java 8389908)
    
    // ======================================================================
    // APPROCCIO 1: STATICO (Per eseguire MainSenzaServiceLoader)
    // Deommentare la riga sotto se vogliamo istanziare le classi direttamente.
    // ======================================================================
    // requires com.library.impl; 
    
    // ======================================================================
    // APPROCCIO 2: DINAMICO (Per eseguire MainConServiceLoader)
    // Diciamo a Java che useremo questo servizio tramite ServiceLoader.
    // ======================================================================
    uses com.library.api.Catalogo; // Errore: The type com.library.api.Catalogo is not accessible (Java 16778666)
}
```

### MainSenzaServiceLoader.java

```java
package com.library.app;

import com.library.api.Catalogo;

// ======================================================================
// APPROCCIO 1: STATICO. 
// Per far funzionare questo codice, decommentare:
// 1. "exports com.library.impl;" nel module-info di Modul3
// 2. "requires com.library.impl;" nel module-info di Modul2
// ======================================================================
/*
import com.library.impl.CatalogoImpl;

public class MainSenzaServiceLoader {
    public static void main(String[] args) {
        System.out.println("Creazione diretta e vecchio stile dell'istanza concreta");
        
        // Accoppiamento forte: la classe Main DEVE conoscere CatalogoImpl a tempo di compilazione
        Catalogo cat = new CatalogoImpl();
        cat.aggiungiLibro("Java 9 Moduli 2");
    }
}
*/
```

### MainConServiceLoader.java

```java
package com.library.app;

import java.util.ServiceLoader;
import com.library.api.Catalogo;

// NOTA BENE: Nessun import da com.library.impl! Il disaccoppiamento è totale.

public class MainConServiceLoader {

	public static void main(String[] args) {
		System.out.println("Creazione dinamica tramite ServiceLoader");

		// 1. Chiediamo al ServiceLoader di cercare tutti i moduli che forniscono "Catalogo"
		ServiceLoader<Catalogo> loader = ServiceLoader.load(Catalogo.class);

		// 2. Opzione A: Eseguiamo il metodo su TUTTE le implementazioni trovate (le proverà entrambe)
		System.out.println("\n--- Ciclare su tutte le implementazioni trovate ---");
		for (Catalogo cat : loader) {
			cat.aggiungiLibro("Java 9 Moduli 2");
		}

		// 3. Opzione B: Se servisse solo una specifica, prendere la prima disponibile
		System.out.println("\n--- Usare della prima implementazione disponibile ---");
		Catalogo singolaIstanza = loader.findFirst()
				.orElseThrow(() -> new RuntimeException("Nessun modulo di implementazione trovato!"));
		
		singolaIstanza.aggiungiLibro("Esempio Singolo");
	}
}
```

### Modul2.iml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$">
      <sourceFolder url="file://$MODULE_DIR$/src" isTestSource="false" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
    <orderEntry type="module" module-name="Modul1" />
  </component>
</module>
```

---

## Modul3

### package-info.java

```java
package com.library.impl;
```

### module-info.java

```java
module com.library.impl {
    // Abbiamo bisogno dell'API per poter implementare l'interfaccia
    requires com.library.api; // Errore: com.library.api cannot be resolved to a module (Java 8389908)
    
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
```

### CatalogoImpl.java

```java
package com.library.impl;

import com.library.api.Catalogo;

public class CatalogoImpl implements Catalogo{
	@Override
	public void aggiungiLibro(String titolo) {
		System.out.println("Aggiunto: " + titolo);
	}
}
```

### CatalogoImpl2.java

```java
package com.library.impl;

import com.library.api.Catalogo;

public class CatalogoImpl2 implements Catalogo {
	@Override
	public void aggiungiLibro(String titolo) {
		System.out.println("Aggiunto tramite Service Loader: " + titolo);
	}
}
```

### Modul3.iml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<module type="JAVA_MODULE" version="4">
  <component name="NewModuleRootManager" inherit-compiler-output="true">
    <exclude-output />
    <content url="file://$MODULE_DIR$">
      <sourceFolder url="file://$MODULE_DIR$/src" isTestSource="false" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
    <orderEntry type="module" module-name="Modul1" />
  </component>
</module>
```

---

# IntelliJ

## Abilitare Module Path in IntelliJ

Per far funzionare correttamente il progetto JPMS con il `ServiceLoader`, devi fare un paio di regolazioni rapide in quella schermata e impostare una dipendenza a Runtime.

---

### 1. Modifica nella finestra "Edit Configuration" (dallo screenshot)

* **Nel menu a tendina `-cp Modul2**`: Cliccaci sopra e cambialo in **`-p Modul2`** (ovvero `--module-path` invece di Classpath).
* *Se non vedi `-p`, seleziona semplicemente la voce relativa al modulo `Modul2*`.


* Fatto questo, clicca su **Apply**.

---

### 2. Il trucco per ServiceLoader su IntelliJ (Fondamentale!)

Poiché `Modul2` non ha un `requires com.library.impl` (giustamente, per mantenere il disaccoppiamento), IntelliJ di default **non include `Modul3` nel `--module-path**` quando avvii `MainConServiceLoader`. Per dirgli di caricarlo comunque a runtime:

1. Apri **File** $\rightarrow$ **Project Structure** $\rightarrow$ **Modules**.
2. Seleziona **Modul2** e vai sulla scheda **Dependencies**.
3. Clicca sul tasto **`+`** $\rightarrow$ **Module Dependency** e seleziona **Modul3**.
4. Nella colonna **Scope** a destra di `Modul3`, cambia il valore da `Compile` a **`Runtime`**.
5. Clicca **Apply** e poi **OK**.

---

### Perché questo passaggio è necessario?

Impostando lo scope a **`Runtime`**:

* **In compilazione:** `Modul2` continua a non vedere `Modul3` (rispettando le regole del JPMS e del `module-info.java`).
* **In esecuzione:** IntelliJ aggiunge `Modul3` al `--module-path`. Quando il `ServiceLoader` cercherà l'interfaccia `Catalogo`, troverà le implementazioni dentro `Modul3` ed eseguirà il programma con successo.

Ora puoi cliccare su **Run**!

![[docs/Pasted image 20260819165027.png]]

---

## Risultato finale

```
Creazione dinamica tramite ServiceLoader

--- Ciclare su tutte le implementazioni trovate ---
Aggiunto: Java 9 Moduli 2
Aggiunto tramite Service Loader: Java 9 Moduli 2

--- Usare della prima implementazione disponibile ---
Aggiunto: Esempio Singolo
```

Il risultato in console è la prova regina che l'architettura a servizi e il disaccoppiamento JPMS stanno funzionando alla perfezione.

Ecco cosa dimostra esattamente l'output che hai ottenuto:

* **Disaccoppiamento riuscito:** `Modul2` ha compilato senza conoscere le classi concrete di `Modul3` (grazie allo Scope `Runtime` che hai impostato), ma a tempo di esecuzione la JVM ha trovato e caricato tutto tramite `ServiceLoader`.
* **Scoperta dinamica:** Il ciclo `for (Catalogo cat : loader)` ha individuato ed eseguito sia `CatalogoImpl` (*"Aggiunto:"*) sia `CatalogoImpl2` (*"Aggiunto tramite Service Loader:"*), ovvero entrambe le classi dichiarate nella direttiva `provides ... with` di `Modul3`.
* **Selezione singola:** Il metodo `.findFirst()` ha pescato correttamente la prima classe disponibile senza sollevare l'eccezione di fallback.

Per quanto riguarda il menu a tendina con la dicitura **`-cp Modul2`**: è del tutto normale. IntelliJ mostra l'etichetta grafica `-cp`, ma non appena selezioni il modulo `Modul2` e rileva la presenza del file `module-info.java`, in background converte automaticamente l'istruzione da Classpath a Module-path (`--module-path`).

---
