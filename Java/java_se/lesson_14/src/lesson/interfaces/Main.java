package lesson.interfaces;

interface Volante { void vola(); }
interface Nuotante { void nuota(); }

class Anatra implements Volante, Nuotante {
    @Override
    public void vola() {}
    @Override
    public void nuota() {}
}

public class Main {
    static void main(String[] args) {
        Volante v = new Anatra();
        Nuotante n = new Anatra();
        Anatra a = new Anatra();
        // Volante v = new Volante(); Errore
    }
}
