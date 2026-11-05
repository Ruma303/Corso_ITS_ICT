# Installazioni

Da terminale digitare:

```sh
npm create vite@latest
```

Seguire la procedura di installazione. Nel nostro caso abbiamo installato:

1. React (con compilatore Vite)
2. TypeScript
3. ESLint

Ulteriori installazioni opzionali di seguito.


## Installazione di Bootstrap CSS

Da terminale digitare:

```sh
npm install -D bootstrap
```

Poi importare in `main.tsx` queste librerie

```javascript
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
```

## Installazione FontAwesome

FontAwesome è una libreria di icone molto comune. Si possono importare come semplici tag HTML o installare le dipendenze per una migliore integrazione con React. Noi seguiremo questa seconda strada.

```sh
npm install @fortawesome/fontawesome-free
```

Importare nel main.ts

```ts
import '@fortawesome/fontawesome-free/css/all.min.css'
```

## Server locale json-server

```sh
npm install -D json-server
```

## Installazione SASS/SCSS

Da terminale digitare:

```sh
npm install -D sass
```