# Struttura full stack 

Con la struttura reale, **eBuy è già un monorepo** (due backend, un frontend, un database). Non serve nessun tool particolare: uv resta confinato alla cartella Python, perché i workspace uv servono solo per più progetti Python. Questo però cambia alcune cose rispetto a quanto ti ho scritto prima.


## 1. Un solo `docker-compose.yml`

Ne hai due (radice e `code/`). Tieni **quello nella radice**: il database è condiviso e non appartiene a nessun backend. Quello in `code/` va eliminato o ridotto a un `include:` del file principale. Così anche `.env` e `.env.example` stanno nella radice.

Attenzione alle porte: **Adminer su 8080 va in conflitto con il tipico server Java**. Una distribuzione sensata:

| Servizio | Porta |
|---|---|
| Backend Python (FastAPI) | 8000 |
| Backend Java | 8080 |
| Adminer | 8081 |
| Frontend (Vite) | 5173 |
| PostgreSQL | 5432 |

## 2. Chi possiede lo schema del database

Con due backend sullo stesso database, devo correggere un consiglio precedente: "Alembic unica fonte dello schema" non regge, perché Java non può dipendere da uno strumento Python (e viceversa). Le strade sono tre:

- **A. Schema neutro in SQL** (`db/` nella radice, file numerati `001_schema.sql`, `002_seed.sql`), applicato da Postgres all'avvio (`initdb.d`) o da un container Flyway. Entrambi i backend lo consumano e scrivi gli ORM a mano. È la più coerente con "database ispezionabile da chi guarda il portfolio", e la leggibilità su GitHub è massima. Perdi l'autogenerate di Alembic.
- **B. Un database per backend** (`ebuy_py`, `ebuy_java`) nello stesso container, ognuno con il suo strumento di migrazione (Alembic, Flyway). Nessun conflitto e ogni stack resta idiomatico, ma lo schema è duplicato e il frontend vede dati diversi a seconda del backend.
- **C. Alembic proprietario**, Java legge soltanto. Asimmetrica: il backend Java dipende dal Python.

Per il tuo obiettivo (stesso frontend, due implementazioni equivalenti) consiglierei la A. La B è la più semplice da partire e puoi sempre migrarla alla A.

## 3. Il contratto è l'API, non il codice

Il frontend deve funzionare con entrambi i backend, quindi la cosa da condividere è **la specifica OpenAPI**:

- stessi endpoint, stessi DTO, stessi codici di errore nei due backend
- il frontend legge l'URL da una variabile (`VITE_API_URL=http://localhost:8000` oppure `:8080`), così cambi backend senza toccare il codice
- i tipi TypeScript si generano da un solo file `openapi.json` committato in `code/` (o in `docs/`), che fa da riferimento anche per Java
- opzionale, più avanti: uno stesso set di test di contratto lanciato contro entrambe le API

Sul server web Java non devi decidere nulla adesso, ma "JavaSE" puro richiederebbe un framework (Spring Boot è lo standard nelle aziende, Javalin è più leggero). Vale la pena scegliere prima del tirocinio.

## 4. Struttura proposta

```
eBuy/
├── code/
│   ├── python/              <- progetto uv (nome libero, vedi sopra)
│   │   ├── pyproject.toml
│   │   ├── src/ebuy_py/...
│   │   └── test/
│   ├── java/
│   ├── frontend/
│   └── README.md
├── db/                      <- schema e seed neutri (opzione A)
├── docs/
│   ├── analisi/
│   ├── design/
│   │   ├── python/
│   │   └── java/
│   └── prof/
├── docker-compose.yml       <- unico: Postgres + Adminer
├── .env.example
├── .gitignore
├── README.md
└── todo_personal.md
```

Dettagli che cambiano:

- `docs/design/` è meglio diviso per linguaggio, perché la fase di design è riscritta per ognuno.
- Avvio dalla radice senza `cd`: `uv run --directory code/python fastapi dev`. In seguito un `justfile` o `Makefile` nella radice con `just py-dev`, `just java-dev`, `just front`, `just db-up` rende il monorepo comodo da usare.
- Se userai GitHub Actions, un workflow per stack con `paths: ["code/python/**"]`, così i test girano solo dove cambia qualcosa.
- Tutto il resto di quanto scritto prima (layer, repository, `create_app`, test) resta valido, solo dentro `code/python/`. Cambiano gli import se rinomini il package, e il percorso `entrypoint` in `[tool.fastapi]`.

## Ritocchi a questo README

- [ ] aggiungi una sezione "Come avviare": `docker compose up -d`, poi un backend a scelta, poi il frontend
- [ ] indica che i due backend espongono lo **stesso contratto API**, perché è un punto di forza da dichiarare subito
