drop table if EXISTS BigliettoAbbonamento;
CREATE TABLE if NOT EXISTS BigliettoAbbonamento(
id INTEGER PRIMARY KEY AUTOINCREMENT,
data_acquisto TEXT DEFAULT(CURRENT_TIMESTAMP),
data_inizio date NOT NULL,
data_fine date NOT NULL,
prezzo REAL NOT NULL,
classe_vagone TEXT NOT NULL,
numero_persone INTEGER NOT NULL,
tipo_abbonamento TEXT,
isbiglietto INT NOT NULL,
isabbonamento INT NOT NULL,
utente_id INTEGER NOT NULL,
treno_id INTEGER NOT NULL,
tratta_id INTEGER NOT NULL,
FOREIGN KEY(utente_id) REFERENCES Utente(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY(treno_id) REFERENCES Treno(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY(tratta_id) REFERENCES Tratta(id) on DELETE CASCADE on UPDATE CASCADE
);