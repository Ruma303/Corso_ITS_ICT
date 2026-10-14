package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.util.List;
import java.util.Objects;
import java.util.regex.Pattern;

public record URL(String link) {

    private static final List<Pattern> PATTERNS = List.of(
        Pattern.compile("^https?://[A-Za-z0-9.-]+\\.[A-Za-z]{2,}(?::\\d{1,5})?(?:/[^\\s?#]*)?(?:\\?[^\\s#]*)?(?:#\\S*)?$"),
        Pattern.compile("^(?:www\\.)?[A-Za-z0-9.-]+\\.[A-Za-z]{2,}(?::\\d{1,5})?(?:/[^\\s?#]*)?(?:\\?[^\\s#]*)?(?:#\\S*)?$")
    );

    public URL {
        Objects.requireNonNull(link, "link non può essere nullo");
        link = link.strip();

        if (link.isEmpty())
            throw new VincoloViolatoException("L'URL non può essere vuoto");

        String candidato = link;
        if (PATTERNS.stream().noneMatch(p -> p.matcher(candidato).matches()))
            throw new VincoloViolatoException("URL non valido: " + link);
    }
}