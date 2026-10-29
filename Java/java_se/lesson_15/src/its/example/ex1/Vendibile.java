package its.example.ex1;

public interface Vendibile {
    double prezzoFinale();

    default String descrizione() {
        return descrizione();
    }
}
