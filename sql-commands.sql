CREATE EXTENSION pgcrypto;


DROP TABLE IF EXISTS ers_reimbursement;
DROP TABLE IF EXISTS ers_users CASCADE;

CREATE TABLE ers_users(
	user_id SERIAL PRIMARY KEY UNIQUE,
	username VARCHAR(20) UNIQUE NOT NULL,
	password VARCHAR UNIQUE NOT NULL,
	first_name VARCHAR,
	last_name VARCHAR,
	email VARCHAR UNIQUE,
	role VARCHAR,
	CONSTRAINT chk_role CHECK (role in ('finance_manager', 'employee'))
);

CREATE TABLE ers_reimbursement(
	reimb_id SERIAL PRIMARY KEY UNIQUE,
	reimb_amount NUMERIC,
	submitted TIMESTAMP,
	resolved TIMESTAMP,
	status 	VARCHAR DEFAULT 'pending',
	CONSTRAINT chk_status CHECK (status in ('pending', 'approved', 'denied')),
	reimb_type VARCHAR,
	CONSTRAINT chk_reimb_type CHECK (reimb_type in ('lodging', 'travel', 'food', 'other')),
	description VARCHAR,
	receipt VARCHAR,
	reimb_author INTEGER,
	CONSTRAINT fk_reimb_auth FOREIGN KEY (reimb_author) REFERENCES ers_users(user_id),
	reimb_resolver INTEGER,
	CONSTRAINT fk_reimb_resolve FOREIGN KEY (reimb_resolver) REFERENCES ers_users(user_id)
);



INSERT INTO ers_users (username, password, first_name, last_name, role)
VALUES 
	('bob45', crypt('babyz', gen_salt('bf')), 'Bob', 'Wehadababyitsaboy', 'finance_manager'),	
	('paladin1', crypt('lawfulstupid', gen_salt('bf')), 'Caerlin', 'Eltac', 'employee'), 
	('Moonswordsftw', crypt('dumbelf', gen_salt('bf')), 'Elwy', 'Iwannamoonsword', 'employee'),
	('Catsrule', crypt('kitty', gen_salt('bf')), 'Carver', 'Runechilde', 'employee');



SELECT * FROM ers_users;
SELECT * FROM ers_reimbursement;

TRUNCATE TABLE ers_reimbursement;
TRUNCATE TABLE ers_users CASCADE;

SELECT * FROM ers_reimbursement WHERE reimb_author = 2 AND status = 'pending';

