--------------------------------------------------
-- Nazione
--------------------------------------------------

INSERT INTO Nazione(nome)
VALUES ('Italia');

--------------------------------------------------
-- Regioni
--------------------------------------------------

INSERT INTO Regione(nome,nazione) VALUES
('Lazio','Italia'),
('Lombardia','Italia'),
('Veneto','Italia'),
('Emilia-Romagna','Italia');

--------------------------------------------------
-- Citta
--------------------------------------------------

INSERT INTO Citta(id,nome,regione,nazione) VALUES
(1,'Roma','Lazio','Italia'),
(2,'Latina','Lazio','Italia'),
(3,'Viterbo','Lazio','Italia'),
(4,'Milano','Lombardia','Italia'),
(5,'Bergamo','Lombardia','Italia'),
(6,'Brescia','Lombardia','Italia'),
(7,'Padova','Veneto','Italia'),
(8,'Verona','Veneto','Italia'),
(9,'Venezia','Veneto','Italia'),
(10,'Bologna','Emilia-Romagna','Italia'),
(11,'Parma','Emilia-Romagna','Italia'),
(12,'Modena','Emilia-Romagna','Italia');

--------------------------------------------------
-- Aree disciplinari
--------------------------------------------------

INSERT INTO AreaDisciplinare(nome) VALUES
('Informatica'),
('Cybersecurity'),
('Data Science');


--------------------------------------------------
-- Corsi ITS
--------------------------------------------------

INSERT INTO CorsoITS(nome,edizione,area) VALUES
('Full Stack Developer',1,'Informatica'),
('Cyber Security Specialist',1,'Cybersecurity'),
('Data Analyst',1,'Data Science');

--------------------------------------------------
-- Moduli
--------------------------------------------------

INSERT INTO Modulo(codice,nome,ore) VALUES
('DB01','Basi di Dati',60),
('JAVA01','Programmazione Java',80),
('SPR01','Spring Boot',70),
('WEB01','Tecnologie Web',50),
('SEC01','Sicurezza Informatica',60),
('NET01','Networking',40),
('DS01','Data Analysis',50),
('PY01','Python',60),
('AI01','Introduzione AI',30),
('UX01','UX Design',30),
('DEV01','DevOps',40),
('CLD01','Cloud Computing',40);

--------------------------------------------------
-- Persone - Docenti
--------------------------------------------------

INSERT INTO Persona VALUES
('RSSMRA90A01H501A','Mario','Rossi',1),
('VRDLGU92B02G224B','Luigi','Verdi',7),
('BNCNDR87C03F205C','Andrea','Bianchi',4),
('NRRMRC89D04A944D','Marco','Neri',10),
('GLLFNC91E05L781E','Francesca','Galli',8),
('BNCMRA93A01B157I','Mario','Bianchi',6),
('LCULNT94A01L736T','Luca','Lenti',9),
('GUOVLC95A01F257S','Ugo','Veloce',12);

INSERT INTO Docente VALUES
('RSSMRA90A01H501A'),
('VRDLGU92B02G224B'),
('BNCNDR87C03F205C'),
('NRRMRC89D04A944D'),
('GLLFNC91E05L781E'),
('BNCMRA93A01B157I'),
('LCULNT94A01L736T'),
('GUOVLC95A01F257S');

--------------------------------------------------
-- Assegnazione moduli-docenti
--------------------------------------------------

INSERT INTO doc_insegna_modulo VALUES
('RSSMRA90A01H501A','DB01'),
('RSSMRA90A01H501A','JAVA01'),
('RSSMRA90A01H501A','SPR01'),
('RSSMRA90A01H501A','WEB01'),

('VRDLGU92B02G224B','DEV01'),

('BNCNDR87C03F205C','CLD01'),
('BNCNDR87C03F205C','NET01'),

('NRRMRC89D04A944D','SEC01'),

('GLLFNC91E05L781E','DS01'),
('GLLFNC91E05L781E','PY01'),

('BNCMRA93A01B157I','DB01'),

('LCULNT94A01L736T','UX01');

--------------------------------------------------
-- Moduli nei corsi
--------------------------------------------------

INSERT INTO modulo_in_corso VALUES
('DB01','Full Stack Developer',1),
('JAVA01','Full Stack Developer',1),
('SPR01','Full Stack Developer',1),
('WEB01','Full Stack Developer',1),
('DEV01','Full Stack Developer',1),
('CLD01','Full Stack Developer',1),

('SEC01','Cyber Security Specialist',1),
('NET01','Cyber Security Specialist',1),
('DB01','Cyber Security Specialist',1),
('CLD01','Cyber Security Specialist',1),

('DS01','Data Analyst',1),
('PY01','Data Analyst',1),
('DB01','Data Analyst',1),
('AI01','Data Analyst',1);

--------------------------------------------------
-- Persone - Studenti
--------------------------------------------------

INSERT INTO Persona VALUES
('FRRLCU00A10H501X','Luca','Ferri',1),
('RSSNNA99B60E472Y','Anna','Russo',2),
('MRTPLA01C15M082K','Paolo','Moretti',3),
('CNTCHR00D58F205P','Chiara','Conti',4),
('VLLGRG99E23A794N','Giorgio','Villa',5),
('GRCLNE01T30B157Q','Elena','Greco',6),
('TSTMRT00B52G224M','Marta','Testa',7),
('MRNLSS98L13L781R','Alessio','Marini',8),
('PLLFRC99M54L736D','Federica','Pellegrini',9),
('CSTDVD00H01A944V','Davide','Costa',10),
('FNTSRA01C59G337J','Sara','Fontana',11),
('RCCMTT00P09F257B','Matteo','Ricci',12),
('LNELRA99D45H501F','Laura','Leone',1),
('GRRGLI01R48E472T','Giulia','Guerra',2),
('RVASMN00T12M082C','Simone','Riva',3),
('SPSMRC99A17F205W','Marco','Esposito',4),
('DLCVNT00B66A794G','Valentina','De Luca',5),
('MRTSFN01E02B157L','Stefano','Martini',6),
('BRNMHL01S50G224H','Michela','Bruni',7),
('ZRRMHL89E21L781Z','Michele','Zarri',8),
('PRGDRA91A30L736U','Dario','Peregrini',9),
('CLNLNU88B62A944A','Luana','Coleno',10),
('FRFSRN02C43G337E','Serena','Farfio',11),
('RTNMSM89P10F257I','Massimo','Rotondi',12),
('LNULGU88T01H501O','Luigi','Launi',1),
('PCAGLI91R17E472S','Giulio','Pace',2),
('RVARNT96P09M082K','Renato','Riva',3),
('GGLCRL95L45F205D','Carla','Giglioli',4),
('DBRDRN97M48A794Y','Adriana','De Bruni',5),
('VRIBRN93R23B157P','Bruno','Veri',6);

--------------------------------------------------
-- Studenti
--------------------------------------------------

INSERT INTO Studente VALUES
('FRRLCU00A10H501X','MAT001','2000-01-10','Full Stack Developer',1),
('RSSNNA99B60E472Y','MAT002','1999-02-20','Full Stack Developer',1),
('MRTPLA01C15M082K','MAT003','2001-03-15','Full Stack Developer',1),
('CNTCHR00D58F205P','MAT004','2000-04-18','Full Stack Developer',1),
('VLLGRG99E23A794N','MAT005','1999-05-23','Full Stack Developer',1),
('GRCLNE01T30B157Q','MAT006','2001-11-30','Full Stack Developer',1),
('PCAGLI91R17E472S','MAT026','1991-10-17','Full Stack Developer',1),
('RVARNT96P09M082K','MAT027','1996-09-09','Full Stack Developer',1),
('GGLCRL95L45F205D','MAT028','1995-07-05','Full Stack Developer',1),
('DBRDRN97M48A794Y','MAT029','1997-08-08','Full Stack Developer',1),
('VRIBRN93R23B157P','MAT030','1993-10-23','Full Stack Developer',1),

('TSTMRT00B52G224M','MAT007','2000-02-12','Cyber Security Specialist',1),
('MRNLSS98L13L781R','MAT008','1998-07-13','Cyber Security Specialist',1),
('PLLFRC99M54L736D','MAT009','1999-08-14','Cyber Security Specialist',1),
('CSTDVD00H01A944V','MAT010','2000-06-01','Cyber Security Specialist',1),
('FNTSRA01C59G337J','MAT011','2001-03-19','Cyber Security Specialist',1),
('RCCMTT00P09F257B','MAT012','2000-09-09','Cyber Security Specialist',1),
('BRNMHL01S50G224H','MAT019','2001-11-10','Cyber Security Specialist',1),
('ZRRMHL89E21L781Z','MAT020','1989-05-21','Cyber Security Specialist',1),
('PRGDRA91A30L736U','MAT021','1991-01-30','Cyber Security Specialist',1),

('LNELRA99D45H501F','MAT013','1999-04-05','Data Analyst',1),
('GRRGLI01R48E472T','MAT014','2001-10-08','Data Analyst',1),
('RVASMN00T12M082C','MAT015','2000-12-12','Data Analyst',1),
('SPSMRC99A17F205W','MAT016','1999-01-17','Data Analyst',1),
('DLCVNT00B66A794G','MAT017','2000-02-26','Data Analyst',1),
('MRTSFN01E02B157L','MAT018','2001-05-02','Data Analyst',1),
('CLNLNU88B62A944A','MAT022','1988-02-22','Data Analyst',1),
('FRFSRN02C43G337E','MAT023','2002-03-03','Data Analyst',1),
('RTNMSM89P10F257I','MAT024','1989-09-10','Data Analyst',1),
('LNULGU88T01H501O','MAT025','1988-12-01','Data Analyst',1);

--------------------------------------------------
-- Esami superati
--------------------------------------------------

INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','DB01',7);
INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','JAVA01',8);
INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','SPR01',9);
INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','WEB01',10);
INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','DEV01',6);
INSERT INTO esame_superato VALUES ('FRRLCU00A10H501X','CLD01',7);

INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','DB01',8);
INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','JAVA01',9);
INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','SPR01',10);
INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','WEB01',6);
INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','DEV01',7);
INSERT INTO esame_superato VALUES ('RSSNNA99B60E472Y','CLD01',8);

INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','DB01',9);
INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','JAVA01',10);
INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','SPR01',6);
INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','WEB01',7);
INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','DEV01',8);
INSERT INTO esame_superato VALUES ('MRTPLA01C15M082K','CLD01',9);

INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','DB01',10);
INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','JAVA01',10);
INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','SPR01',10);
INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','WEB01',10);
INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','DEV01',10);
INSERT INTO esame_superato VALUES ('CNTCHR00D58F205P','CLD01',10);

INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','DB01',6);
INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','JAVA01',7);
INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','SPR01',8);
INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','WEB01',9);
INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','DEV01',10);
INSERT INTO esame_superato VALUES ('VLLGRG99E23A794N','CLD01',6);

INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','DB01',7);
INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','JAVA01',8);
INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','SPR01',9);
INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','WEB01',10);
INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','DEV01',6);
INSERT INTO esame_superato VALUES ('GRCLNE01T30B157Q','CLD01',7);

INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','DB01',8);
INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','JAVA01',9);
INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','SPR01',10);
INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','WEB01',6);
INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','DEV01',7);
INSERT INTO esame_superato VALUES ('TSTMRT00B52G224M','CLD01',8);

INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','DB01',9);
INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','JAVA01',10);
INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','SPR01',6);
INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','WEB01',7);
INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','DEV01',8);
INSERT INTO esame_superato VALUES ('MRNLSS98L13L781R','CLD01',9);

INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','DB01',10);
INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','JAVA01',6);
INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','SPR01',7);
INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','WEB01',8);
INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','DEV01',9);
INSERT INTO esame_superato VALUES ('PLLFRC99M54L736D','CLD01',10);

INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','DB01',6);
INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','JAVA01',7);
INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','SPR01',8);
INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','WEB01',9);
INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','DEV01',10);
INSERT INTO esame_superato VALUES ('CSTDVD00H01A944V','CLD01',6);

INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','DB01',7);
INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','JAVA01',8);
INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','SPR01',9);
INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','WEB01',10);
INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','DEV01',6);
INSERT INTO esame_superato VALUES ('FNTSRA01C59G337J','CLD01',7);

INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','DB01',8);
INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','JAVA01',9);
INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','SPR01',10);
INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','WEB01',6);
INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','DEV01',7);
INSERT INTO esame_superato VALUES ('RCCMTT00P09F257B','CLD01',8);

INSERT INTO esame_superato VALUES ('LNELRA99D45H501F','DB01',9);
INSERT INTO esame_superato VALUES ('LNELRA99D45H501F','SEC01',10);
INSERT INTO esame_superato VALUES ('LNELRA99D45H501F','NET01',6);
INSERT INTO esame_superato VALUES ('LNELRA99D45H501F','CLD01',7);

INSERT INTO esame_superato VALUES ('GRRGLI01R48E472T','DB01',10);
INSERT INTO esame_superato VALUES ('GRRGLI01R48E472T','SEC01',6);
INSERT INTO esame_superato VALUES ('GRRGLI01R48E472T','NET01',7);
INSERT INTO esame_superato VALUES ('GRRGLI01R48E472T','CLD01',8);

INSERT INTO esame_superato VALUES ('RVASMN00T12M082C','DB01',6);
INSERT INTO esame_superato VALUES ('RVASMN00T12M082C','SEC01',7);
INSERT INTO esame_superato VALUES ('RVASMN00T12M082C','NET01',8);
INSERT INTO esame_superato VALUES ('RVASMN00T12M082C','CLD01',9);

INSERT INTO esame_superato VALUES ('SPSMRC99A17F205W','DB01',7);
INSERT INTO esame_superato VALUES ('SPSMRC99A17F205W','SEC01',8);
INSERT INTO esame_superato VALUES ('SPSMRC99A17F205W','NET01',9);
INSERT INTO esame_superato VALUES ('SPSMRC99A17F205W','CLD01',10);

INSERT INTO esame_superato VALUES ('DLCVNT00B66A794G','DB01',8);
INSERT INTO esame_superato VALUES ('DLCVNT00B66A794G','SEC01',9);
INSERT INTO esame_superato VALUES ('DLCVNT00B66A794G','NET01',10);
INSERT INTO esame_superato VALUES ('DLCVNT00B66A794G','CLD01',6);

INSERT INTO esame_superato VALUES ('MRTSFN01E02B157L','DB01',9);
INSERT INTO esame_superato VALUES ('MRTSFN01E02B157L','SEC01',10);
INSERT INTO esame_superato VALUES ('MRTSFN01E02B157L','NET01',6);
INSERT INTO esame_superato VALUES ('MRTSFN01E02B157L','CLD01',7);

INSERT INTO esame_superato VALUES ('BRNMHL01S50G224H','DB01',10);
INSERT INTO esame_superato VALUES ('BRNMHL01S50G224H','SEC01',6);
INSERT INTO esame_superato VALUES ('BRNMHL01S50G224H','NET01',7);
INSERT INTO esame_superato VALUES ('BRNMHL01S50G224H','CLD01',8);

INSERT INTO esame_superato VALUES ('ZRRMHL89E21L781Z','DB01',6);
INSERT INTO esame_superato VALUES ('ZRRMHL89E21L781Z','SEC01',7);
INSERT INTO esame_superato VALUES ('ZRRMHL89E21L781Z','NET01',8);
INSERT INTO esame_superato VALUES ('ZRRMHL89E21L781Z','CLD01',9);

INSERT INTO esame_superato VALUES ('PRGDRA91A30L736U','DB01',7);
INSERT INTO esame_superato VALUES ('PRGDRA91A30L736U','SEC01',8);
INSERT INTO esame_superato VALUES ('PRGDRA91A30L736U','NET01',9);
INSERT INTO esame_superato VALUES ('PRGDRA91A30L736U','CLD01',10);

INSERT INTO esame_superato VALUES ('CLNLNU88B62A944A','DB01',8);
INSERT INTO esame_superato VALUES ('CLNLNU88B62A944A','DS01',9);
INSERT INTO esame_superato VALUES ('CLNLNU88B62A944A','PY01',10);

INSERT INTO esame_superato VALUES ('FRFSRN02C43G337E','DB01',9);
INSERT INTO esame_superato VALUES ('FRFSRN02C43G337E','DS01',10);
INSERT INTO esame_superato VALUES ('FRFSRN02C43G337E','PY01',6);

INSERT INTO esame_superato VALUES ('RTNMSM89P10F257I','DB01',9);
INSERT INTO esame_superato VALUES ('RTNMSM89P10F257I','DS01',9);
INSERT INTO esame_superato VALUES ('RTNMSM89P10F257I','PY01',9);

INSERT INTO esame_superato VALUES ('LNULGU88T01H501O','DB01',9);
INSERT INTO esame_superato VALUES ('LNULGU88T01H501O','DS01',9);
INSERT INTO esame_superato VALUES ('LNULGU88T01H501O','PY01',9);

INSERT INTO esame_superato VALUES ('PCAGLI91R17E472S','DB01',7);
INSERT INTO esame_superato VALUES ('PCAGLI91R17E472S','DS01',8);
INSERT INTO esame_superato VALUES ('PCAGLI91R17E472S','PY01',9);

INSERT INTO esame_superato VALUES ('RVARNT96P09M082K','DB01',8);
INSERT INTO esame_superato VALUES ('RVARNT96P09M082K','DS01',9);
INSERT INTO esame_superato VALUES ('RVARNT96P09M082K','PY01',10);
-- ***** FINE *****
