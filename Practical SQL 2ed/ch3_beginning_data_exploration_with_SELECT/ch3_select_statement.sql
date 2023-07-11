-- Basic SELECT syntax:
SELECT * FROM teachers;

-- Open table in pgAdmin:
TABLE teachers;

-- Querying a Subset of Columns
SELECT hire_date, first_name, school  FROM teachers;

-- Sorting data with ORDER BY
SELECT
    first_name,
    school,
    salary
FROM
    teachers
ORDER BY
    salary DESC;

-- Sorting data with ORDER BY (using column position)
SELECT
    first_name,
    school,
    salary
FROM
    teachers
ORDER BY
    3 ASC;

-- Sorting multiple columns with ORDER BY
SELECT
    first_name,
    school,
    salary
FROM
    teachers
ORDER BY
    salary DESC,
    first_name ASC;

-- Using DISTINCT to find unique values
SELECT DISTINCT
    salary
FROM
    teachers
ORDER BY
    salary DESC;

-- Filtering rows with WHERE
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    salary BETWEEN 45000 AND 50000;

-- Using LIKE and ILIKE with WHERE
-- LIKE is case sensitive
SELECT
    *
FROM
    teachers
WHERE 
    first_name LIKE 'j%h_';
-- ILIKE is case insensitive
SELECT
    *
FROM
    teachers
WHERE 
    first_name ILIKE 'j%h_';

-- Combining Operators with AND
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    salary >= 39000
    AND first_name ILIKE 'j%';

-- Combining Operators with OR
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    (salary >= 45000 AND salary <= 50000)
    OR first_name ILIKE 'j%';

-- Putting All Together
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    (salary >= 45000 AND salary <= 49000)
    OR first_name ILIKE 'j%'
ORDER BY
    salary DESC;