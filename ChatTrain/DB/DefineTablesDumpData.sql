DROP TABLE if EXISTS Tickets;

CREATE TABLE if NOT EXISTS Tickets(
id INTEGER PRIMARY KEY AUTOINCREMENT,
machine_code TEXT NOT NULL,
service_code TEXT,
customer_username TEXT,
message_text TEXT NOT NULL,
message_sent_date datetime
);