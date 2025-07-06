-- Insert tabella collegamento

-- Tratta 1: Milano -> Napoli
INSERT INTO TrattaStazione(tratta_id, stazione_id, ordine, orario_arrivo, orario_partenza) VALUES
(1,2,1,NULL,'8:00:00'), -- Milano
(1,5,2,'9:10:00','9:15:00'), -- Bologna
(1,3,3,'10:00:00', '10:05:00'), -- Firenze
(1,1,4,'11:10:00', '11:15:00'), -- Roma
(1,4,5, '12:30:00', NULL); -- Napoli

-- Tratta 2: Torino -> Venezia
INSERT INTO TrattaStazione (tratta_id, stazione_id, ordine, orario_arrivo, orario_partenza) VALUES
(2, 6, 1, NULL, '07:00:00'),   -- Torino
(2, 2, 2, '08:10:00', '08:15:00'),  -- Milano
(2, 11, 3, '09:45:00', '09:50:00'), -- Verona
(2, 20, 4, '10:30:00', '10:35:00'), -- Padova
(2, 7, 5, '12:15:00', NULL);        -- Venezia

-- Tratta 3: Milano -> Bari
INSERT INTO TrattaStazione (tratta_id, stazione_id, ordine, orario_arrivo, orario_partenza) VALUES
(3, 2, 1, NULL, '07:00:00'),      -- Milano
(3, 5, 2, '08:30:00', '08:35:00'), -- Bologna 
(3, 3, 3, '09:30:00', '09:35:00'), -- Firenze 
(3, 1, 4, '11:00:00', '11:10:00'), -- Roma 
(3, 4, 5, '12:30:00', '12:35:00'), -- Napoli 
(3, 10, 6, '14:30:00', NULL);     -- Bari 

-- Tratta 4: Bari -> Palermo
INSERT INTO TrattaStazione (tratta_id, stazione_id, ordine, orario_arrivo, orario_partenza) VALUES
(4, 10, 1, NULL, '06:00:00'),  -- Bari
(4, 4, 2, '08:15:00', '08:20:00'),  -- Napoli
(4, 16, 3, '10:50:00', '10:55:00'), -- Messina
(4, 9, 4, '13:45:00', NULL);        -- Palermo

-- Tratta 5: Lecce -> Torino
INSERT INTO TrattaStazione (tratta_id, stazione_id, ordine, orario_arrivo, orario_partenza) VALUES
(5, 13, 1, NULL, '06:00:00'),  -- Lecce
(5, 10, 2, '07:50:00', '07:55:00'), -- Bari
(5, 5, 3, '10:30:00', '10:35:00'), -- Bologna
(5, 2, 4, '11:45:00', '11:50:00'), -- Milano
(5, 6, 5, '15:30:00', NULL);       -- Torino
