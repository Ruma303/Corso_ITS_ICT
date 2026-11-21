package its.exercise;

/*  LABORATORIO — la coda generica
 *
 *  TODO 7 — rendila generica: CodaLavorazione<T>, e sostituisci Object con T.
 *  TODO 8 — falla implementare Iterable<T>, cosi' si puo' scorrere con il for-each.
 *           Basta restituire l'iterator del Deque interno.
 *
 *  Metodi del Deque che servono: addLast, addFirst, pollFirst, peekFirst, isEmpty, size.
 */
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

public class CodaLavorazione<T> implements Iterable<T> {

    private final Deque<T> elementi = new ArrayDeque<>();

    public void accoda(T elemento)   { elementi.addLast(elemento); }
    public void anticipa(T elemento) { elementi.addFirst(elemento); }
    public T prossimo()              { return elementi.pollFirst(); }
    public T sbircia()               { return elementi.peekFirst(); }
    public boolean vuota()                { return elementi.isEmpty(); }
    public int quanti()                   { return elementi.size(); }

    @Override
    public Iterator<T> iterator() {return elementi.iterator();}
}
