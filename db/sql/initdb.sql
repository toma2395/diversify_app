-- CREATE DATABASE diversify_db owner "admin";

CREATE SCHEMA volunteer AUTHORIZATION "admin";

CREATE TABLE volunteer.volunteers (
	v_id integer NOT NULL,
	v_name varchar NULL,
	v_surname varchar NULL,
	v_creation_date timestamptz NULL,
	v_city varchar NULL,
	v_country varchar NULL,
	CONSTRAINT volunteers_pk PRIMARY KEY (v_id)
);

CREATE SEQUENCE volunteer.v_volunteer_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1
	NO CYCLE;


INSERT INTO volunteer.volunteers (v_id, v_name,v_surname,v_creation_date,  v_city,v_country)
	VALUES (nextval('volunteer.v_volunteer_seq'),'Adriano','Italiano',current_timestamp, 'Rome','Italy');


INSERT INTO volunteer.volunteers ( v_id, v_name,v_surname,v_creation_date, v_city,v_country)
	VALUES (nextval('volunteer.v_volunteer_seq'),'Jurek','Owsiak',current_timestamp,'Szczecin','Poland');

commit;