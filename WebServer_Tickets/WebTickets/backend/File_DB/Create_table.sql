DROP TABLE if EXISTS Utente;
DROP TABLE if EXISTS MetodoPagamento;
DROP TABLE if EXISTS TrenoStazione;
DROP TABLE if EXISTS BigliettoAbbonamento;
DROP TABLE if EXISTS Tratta;
DROP TABLE if EXISTS Treno;
DROP TABLE if EXISTS Stazione;
Drop TABLE if EXISTS TrattaStazione;
--
CREATE TABLE if NOT EXISTS Utente(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cognome TEXT NOT NULL,
codicefiscale TEXT NOT NULL,
username TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password TEXT NOT NULL 
);
--
CREATE TABLE if NOT EXISTS MetodoPagamento(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tipo TEXT NOT NULL,
numero_carta INTEGER NOT NULL,
cvv INT NOT NULL,
data_scadenza date,
utente_id INTEGER NOT NULL,
FOREIGN KEY(utente_id) REFERENCES Utente(id) on DELETE CASCADE on UPDATE CASCADE
);
--
CREATE TABLE if NOT EXISTS Treno(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL, -- jazz/rock/
tipo TEXT NOT NULL -- regionale/intercity/freccia rossa
);
--
CREATE TABLE if NOT EXISTS Stazione(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
citta TEXT NOT NULL
);
--
CREATE TABLE if NOT EXISTS TrenoStazione(
id INTEGER PRIMARY KEY AUTOINCREMENT,
orario_arrivo datetime NOT NULL,
orario_partenza datetime NOT NULL,
treno_id INTEGER NOT NULL,
stazione_id INTEGER NOT NULL,
FOREIGN KEY(treno_id) REFERENCES Treno(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY(stazione_id) REFERENCES Stazione(id) on DELETE CASCADE on UPDATE CASCADE
);
--
CREATE TABLE if NOT EXISTS Tratta(
id INTEGER PRIMARY KEY AUTOINCREMENT,
durata time NOT NULL, -- hh:mm:ss
stazione_arrivo INTEGER NOT NULL,
stazione_partenza INTEGER NOT NULL,
FOREIGN KEY(stazione_arrivo) REFERENCES Stazione(id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(stazione_partenza) REFERENCES Stazione(id) ON DELETE CASCADE ON UPDATE CASCADE
);
--
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
--
CREATE TABLE if NOT EXISTS TrattaStazione(
id INTEGER PRIMARY KEY AUTOINCREMENT,
tratta_id INTEGER NOT NULL,
stazione_id INTEGER NOT NULL,
ordine INTEGER NOT NULL, -- es. 1 = partenza, 2 = fermata intermedia, ..., N = arrivo
orario_arrivo time,
orario_partenza time,
FOREIGN KEY(tratta_id) REFERENCES Tratta(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY(stazione_id) REFERENCES Stazione(id) on DELETE CASCADE on UPDATE CASCADE
);