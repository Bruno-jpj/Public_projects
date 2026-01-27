DROP TABLE if EXISTS CustomerMachine;
DROP TABLE if EXISTS Tickets;
DROP TABLE if EXISTS Machine;
DROP TABLE if EXISTS Customers;
DROP TABLE if EXISTS Service;

CREATE TABLE if NOT EXISTS Machine(
id INTEGER PRIMARY KEY AUTOINCREMENT,
code TEXT UNIQUE NOT NULL, -- unique code of the machine, ex. pp21034
buy_date date NOT NULL,
online INTEGER NOT NULL CHECK (online in (0, 1)) -- bool: 1 = true | 0 = false
);
CREATE TABLE if NOT EXISTS Customers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
buyer_name TEXT NOT NULL, -- ex. amazon
username TEXT UNIQUE NOT NULL,
pwd TEXT NOT NULL
);
CREATE TABLE if NOT EXISTS Service(
id INTEGER PRIMARY KEY AUTOINCREMENT,
serv_code TEXT UNIQUE NOT NULL,
serv_pwd TEXT NOT NULL,
is_admin INTEGER NOT NULL CHECK(is_admin in (0,1))
);
CREATE TABLE if NOT EXISTS Tickets(
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER NOT NULL,
service_id INTEGER NOT NULL,
machine_id INTEGER NOT NULL,
opened_date date NOT NULL,
closed_date date,
problem_title TEXT NOT NULL,
problem_text TEXT NOT NULL,
status TEXT NOT NULL CHECK (status in ('closed', 'open', 'working')),

FOREIGN KEY (customer_id) REFERENCES Customers(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY (service_id) REFERENCES Service(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY (machine_id) REFERENCES Machine(id) on DELETE CASCADE on UPDATE CASCADE
);
CREATE TABLE if NOT EXISTS CustomerMachine(
id INTEGER PRIMARY KEY AUTOINCREMENT,
machine_id INTEGER NOT NULL,
customer_id INTEGER NOT NULL,

-- UNIQUE(customer_id, machine_id)

FOREIGN KEY (machine_id) REFERENCES Machine(id) on DELETE CASCADE on UPDATE CASCADE,
FOREIGN KEY (customer_id) REFERENCES Customers(id) on DELETE CASCADE on UPDATE CASCADE
);