CREATE TABLE ip_source (
   ip_hash VARCHAR(1000) PRIMARY KEY NOT NULL,
   ip_adress VARCHAR(100) NOT NULL,
   encryption_algo VARCHAR(1000) NOT NULL,
   modulus VARCHAR(1000) NOT NULL
);
