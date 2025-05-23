DROP TABLE if EXISTS Utente;
DROP TABLE if EXISTS MetodoPagamento;
DROP TABLE if EXISTS TrenoStazione;
DROP TABLE if EXISTS Biglietto;
DROP TABLE if EXISTS Stazione;
DROP TABLE if EXISTS Tratta;
DROP TABLE if EXISTS Treno;

-- 1. Utente
CREATE TABLE if NOT EXISTS Utente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
	cognome TEXT NOT NULL,
	codicefiscale TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
	username TEXT NOT NULL,
    pwd TEXT NOT NULL
);

-- 2. MetodoPagamento
CREATE TABLE if NOT EXISTS MetodoPagamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    numero_carta TEXT,
    scadenza TEXT,
    FOREIGN KEY (utente_id) REFERENCES Utente(id) ON DELETE CASCADE on UPDATE CASCADE
);

-- 3. Stazione
CREATE TABLE if NOT EXISTS Stazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    citta TEXT NOT NULL
);

-- 4. Tratta
CREATE TABLE if NOT EXISTS Tratta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stazione_partenza_id INTEGER NOT NULL,
    stazione_arrivo_id INTEGER NOT NULL,
    durata INTEGER,
    FOREIGN KEY (stazione_partenza_id) REFERENCES Stazione(id) ON DELETE CASCADE on UPDATE CASCADE,
    FOREIGN KEY (stazione_arrivo_id) REFERENCES Stazione(id) ON DELETE CASCADE on UPDATE CASCADE
);

-- 5. Treno
CREATE TABLE if NOT EXISTS Treno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,  -- es: regionale, AV, ecc.
    richiede_nominativo INT NOT NULL DEFAULT 0
);

-- 6. TrenoStazione (tabella ponte per molti-a-molti)
CREATE TABLE if NOT EXISTS TrenoStazione (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    treno_id INTEGER NOT NULL,
    stazione_id INTEGER NOT NULL,
    orario_arrivo TEXT,
    orario_partenza TEXT,
    ordine_di_passaggio INTEGER,
    FOREIGN KEY (treno_id) REFERENCES Treno(id) ON DELETE CASCADE on UPDATE CASCADE,
    FOREIGN KEY (stazione_id) REFERENCES Stazione(id) ON DELETE CASCADE on UPDATE CASCADE
);

-- 7. Biglietto
CREATE TABLE if NOT EXISTS Biglietto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utente_id INTEGER NOT NULL,
    treno_id INTEGER NOT NULL,
    tratta_id INTEGER NOT NULL,
    nominativo TEXT,  -- può essere NULL se il treno non lo richiede
    data_acquisto TEXT NOT NULL,
    data_viaggio TEXT NOT NULL,
    prezzo REAL NOT NULL,
    tipo_biglietto TEXT,
    FOREIGN KEY (utente_id) REFERENCES Utente(id) ON DELETE CASCADE on UPDATE CASCADE,
    FOREIGN KEY (treno_id) REFERENCES Treno(id) ON DELETE CASCADE on UPDATE CASCADE,
    FOREIGN KEY (tratta_id) REFERENCES Tratta(id) ON DELETE CASCADE on UPDATE CASCADE
);
