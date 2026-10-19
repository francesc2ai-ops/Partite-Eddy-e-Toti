# Partite Toti & Eddy

Una pagina per sapere dove giocano Toti ed Eddy ogni weekend: una scheda per weekend,
con giorno, data, ora, campo e il pulsante Google Maps. Se uno dei due non gioca compare
"Nessuna partita" (o "Riposo").

- **Toti** (pallavolo, Gaffeo): le partite arrivano in automatico dalla pagina del Gaffeo
  (`data/toti.json` indica da dove). Se aggiorni quel calendario, si aggiorna anche qui.
- **Eddy** (calcio, Carugo Academy, Terza Categoria Monza girone B): le partite sono in
  `data/eddy.json`, ricavate dal calendario LND (`data/calendario_terza_monza_girB.pdf`) con
  `scripts/eddy_da_calendario.py`.

## Spostamenti e orari
Per una partita spostata modifica il campo `inizio` (formato `2026-10-25T19:00`) in `data/eddy.json`
direttamente dal sito di GitHub. Dove il calendario indica l'orario federale (O.F.) la pagina mostra
"orario da confermare": quando lo sai, scrivi l'ora in `inizio` e metti `"ora_da_confermare": false`.
