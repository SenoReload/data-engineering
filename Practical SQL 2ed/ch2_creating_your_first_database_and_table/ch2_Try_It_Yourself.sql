-- Create a table called teachers in the analysis database:
CREATE TABLE teachers (
	id bigserial,
	first_name varchar(50),
	last_name varchar(50),
	school varchar(50),
	hire_date date,
	salary numeric
);

-- Inserts teacher data into the table.
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Jane', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
       ('John', 'Doe', 'Alamo Street', '2010-06-30', 39100),
       ('Alice', 'Richards', 'Manuel Salazar Street', '2005-06-30', 40000),
       ('Mary', 'Simpson', 'Main Street', '2000-12-03', 43000),
       ('David', 'Smith', 'Jackson Drive', '1995-03-15', 45000),
       ('Helen', 'Andrews', 'North East Avenue', '1997-07-02', 43000),
       ('Richard', 'Doe', 'West Drive', '2000-08-09', 45000),
       ('Susan', 'Brown', 'Central Avenue', '2002-09-30', 47000),
       ('Joseph', 'Duncan', 'West Street', '1993-05-30', 50000),
       ('Andrew', 'Peters', 'Alamo Street', '2009-06-30', 39000)
;