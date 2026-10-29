# Sportbook

---

## Frontend

Avviare il server di sviluppo frontend con:

```sh
npm run dev            # terminale 1 — Vite su :5173, proxy /api -> :3000
```

---

## Backend (simulato)

Il progetto ha una dipendenza, json-server, che espone il file persone.json come REST API.

```sh
npm run db:build     # genera db.json da src/data/persone.json (rifallo se cambi i dati)
npm run server        # terminale 2 — json-server su :3000
```
