#!/usr/bin/env python3
"""Genera data/eddy.json dal calendario LND Terza Categoria Monza girone B (trascritto qui sotto)."""
import json
from datetime import date, timedelta
from pathlib import Path

# Campi: (campo, indirizzo, giorno: "sab"/"dom", ora o None = orario federale)
CAMPI = {
    "CARUGO ACADEMY": ("Campo Sportivo Comunale", "Via delle Ginestre 5, Carugo (CO)", "dom", "15:00"),
    "BRIGANTIA CALCIO": ("C.S. Comunale", "Via S. Caterina da Siena 1, Sovico (MB)", "sab", "20:00"),
    "CABIATE": ("C.S. Comunale - Campo A", "Via Bruno Buozzi 30, Cabiate (CO)", "dom", "15:00"),
    "FOOTBALL SESTO 2025": ("Comunale S. Pertini n.1", "Via Giovanni Boccaccio 285, Sesto San Giovanni (MI)", "dom", "18:30"),
    "SERENISSIMA S.PIO X": ("Comunale \"D. Crippa\" - Campo 1", "Via dei Lavoratori 27, Cinisello Balsamo (MI)", "dom", "15:00"),
    "SPORTINZONA MELINA": ("C.S. Comunale \"Cameroni\"", "Via Bechi 2, Milano", "sab", "20:00"),
    "STELLA AZZURRA AROSIO": ("Campo \"Franco Nigro\"", "Piazza della Chiesa 1, Arosio (CO)", "dom", None),
    "STELLA AZZURRA 56": ("Oratorio San Luigi Gonzaga", "Viale Rinascita, Cinisello Balsamo (MI)", "dom", "17:30"),
    "CAMPAGNOLA DON BOSCO": ("C.S. Comunale - Campo n.1", "Via G. Deledda 24, Lissone (MB)", "dom", None),
    "DESIO ACADEMY S. G.": ("C.S. Comunale", "Via S. Caterina da Siena 1, Sovico (MB)", "dom", "18:00"),
    "INVERIGO": ("Campo \"Pietro Rossini\"", "Via Magellano, Briosco (MB)", "dom", "15:00"),
    "MILANO GUARDIANS": ("Campo \"Breda\" B", "Via XX Settembre 162, Sesto San Giovanni (MI)", "dom", "19:00"),
    "NOVESE GUNNERS": ("C.S. Comunale n.2", "Via G. Brodolini 2, Nova Milanese (MB)", "dom", None),
    "SAN FRUTTUOSO CALCIO": ("C.S. Comunale della Boscherona", "Via della Boscherona, Monza (MB)", "dom", None),
    "SAN MARCO O.S.F.": ("Parrocchia Sacra Famiglia n.1", "Piazza Sacra Famiglia 1, Cinisello Balsamo (MI)", "dom", "14:00"),
}
NOMI = {"STELLA AZZURRA AROSIO": "Stella Azzurra Arosio", "BRIGANTIA CALCIO": "Brigantia Calcio", "DESIO ACADEMY S. G.": "Desio Academy San Giorgio",
        "CABIATE": "Cabiate", "CAMPAGNOLA DON BOSCO": "Campagnola Don Bosco", "SAN MARCO O.S.F.": "San Marco O.S.F.", "MILANO GUARDIANS": "Milano Guardians",
        "FOOTBALL SESTO 2025": "Football Sesto 2025", "INVERIGO": "Inverigo", "SERENISSIMA S.PIO X": "Serenissima S. Pio X", "SPORTINZONA MELINA": "Sportinzona Melina Miele",
        "SAN FRUTTUOSO CALCIO": "San Fruttuoso Calcio", "STELLA AZZURRA 56": "Stella Azzurra 56", "NOVESE GUNNERS": "Novese Gunners"}

# giornata: (data andata, data ritorno, avversario, Carugo in casa all'andata?) ; None = riposo
G = [
    (1, "2026-09-13", "2027-01-10", "STELLA AZZURRA AROSIO", False),
    (2, "2026-09-20", "2027-01-17", "BRIGANTIA CALCIO", True),
    (3, "2026-09-27", "2027-01-24", "DESIO ACADEMY S. G.", False),
    (4, "2026-10-04", "2027-01-31", "CABIATE", True),
    (5, "2026-10-11", "2027-02-07", "CAMPAGNOLA DON BOSCO", False),
    (6, "2026-10-18", "2027-02-14", "SAN MARCO O.S.F.", True),
    (7, "2026-10-25", "2027-02-21", "MILANO GUARDIANS", False),
    (8, "2026-11-01", "2027-02-28", "FOOTBALL SESTO 2025", True),
    (9, "2026-11-08", "2027-03-07", "INVERIGO", False),
    (10, "2026-11-15", "2027-03-14", "SERENISSIMA S.PIO X", True),
    (11, "2026-11-22", "2027-03-21", None, None),
    (12, "2026-11-29", "2027-04-04", "SPORTINZONA MELINA", True),
    (13, "2026-12-06", "2027-04-11", "SAN FRUTTUOSO CALCIO", False),
    (14, "2026-12-13", "2027-04-18", "STELLA AZZURRA 56", False),
    (15, "2026-12-20", "2027-04-25", "NOVESE GUNNERS", True),
]

partite = []
for g, da, dr, avv, casa_andata in G:
    for gior, dstr, rit in ((g, da, False), (g + 15, dr, True)):
        dom = date.fromisoformat(dstr)
        if avv is None:
            partite.append({"giornata": gior, "inizio": dom.isoformat() + "T15:00", "riposo": True})
            continue
        casa = casa_andata if not rit else not casa_andata
        ospitante = "CARUGO ACADEMY" if casa else avv
        campo, ind, giorno, ora = CAMPI[ospitante]
        d = dom - timedelta(days=1) if giorno == "sab" else dom
        partite.append({
            "giornata": gior,
            "inizio": d.isoformat() + "T" + (ora or "15:00"),
            "ora_da_confermare": ora is None,
            "casa": casa,
            "avversario": NOMI[avv],
            "campo": campo,
            "indirizzo": ind,
        })
partite.sort(key=lambda p: p["inizio"])
out = {
    "nome": "Eddy", "squadra": "Carugo Academy", "sport": "Calcio",
    "campionato": "Terza Categoria Monza · Girone B",
    "_nota": "Generato da scripts/eddy_da_calendario.py dal calendario LND. Per uno spostamento modifica qui inizio (AAAA-MM-GGTHH:MM). ora_da_confermare = orario federale.",
    "partite": partite,
}
Path(__file__).resolve().parent.parent.joinpath("data", "eddy.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(partite), "righe (", sum(1 for p in partite if p.get("riposo")), "riposi )")
