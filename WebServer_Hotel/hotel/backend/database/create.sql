-- DROP TABLE
DROP TABLE IF EXISTS PrenotazioneTavolo;
DROP TABLE IF EXISTS PrenotazioneCamera;
DROP TABLE IF EXISTS Tavolo;
DROP TABLE IF EXISTS Camera;
DROP TABLE IF EXISTS Utente;

-- Tabella degli utenti
CREATE TABLE IF NOT EXISTS Utente(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL,
    CodiceFiscale TEXT NOT NULL UNIQUE,
    DataNascita DATE NOT NULL,
    Cellulare TEXT NOT NULL,
    CittaResidenza TEXT NOT NULL
);

-- Camere singole
CREATE TABLE IF NOT EXISTS Camera(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NumeroCamera TEXT NOT NULL UNIQUE,
    Tipo TEXT NOT NULL, -- es. singola, doppia, suite
    Stato TEXT NOT NULL -- libera, occupata, manutenzione
);

-- Prenotazioni camere
CREATE TABLE IF NOT EXISTS PrenotazioneCamera(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idUtente INTEGER NOT NULL,
    idCamera INTEGER NOT NULL,
    DataInizio DATE NOT NULL,
    DataFine DATE NOT NULL,
    FOREIGN KEY (idUtente) REFERENCES Utente(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (idCamera) REFERENCES Camera(id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tavoli singoli
CREATE TABLE IF NOT EXISTS Tavolo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NumeroTavolo TEXT NOT NULL UNIQUE,
    Posizione TEXT NOT NULL, -- interno, esterno
    Stato TEXT NOT NULL -- libero, occupato
);

-- Prenotazioni tavolo
CREATE TABLE IF NOT EXISTS PrenotazioneTavolo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idUtente INTEGER NOT NULL,
    idTavolo INTEGER NOT NULL,
    DataPrenotazione DATE NOT NULL,
    OrarioPrenotazione TIME NOT NULL,
    FOREIGN KEY (idUtente) REFERENCES Utente(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (idTavolo) REFERENCES Tavolo(id) ON DELETE CASCADE ON UPDATE CASCADE
);
