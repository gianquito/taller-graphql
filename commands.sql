CREATE TABLE gerente (
	dni integer PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	telefono INT NOT NULL
)

CREATE TABLE hotel (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	direccion VARCHAR(100) NOT NULL,
	estrellas integer NOT NULL,
	gerente_fk integer NOT NULL,
	CONSTRAINT hotel_fk FOREIGN KEY (gerente_fk) REFERENCES gerente (dni)
)

CREATE TABLE habitacion (
	id serial PRIMARY KEY,
	numero integer NOT NULL,
	precio integer NOT NULL,
	disponible boolean NOT NULL,
	hotel_fk integer NOT NULL,
	CONSTRAINT habitacion_fk FOREIGN KEY (hotel_fk) REFERENCES hotel (id)
)