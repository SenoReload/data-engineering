-- Try it yourself
-- 1. The school district superintendent asks for a list of teachers in each
-- school. Write a query that lists the schools in alphabetical order along
-- with teachers ordered by last name A–Z.
SELECT
    school,
    last_name,
    first_name,
    salary,
    hire_date
FROM
    teachers
ORDER BY
    school ASC,
    last_name ASC;

-- 2. Write a query that finds the one teacher whose first name starts with the
-- letter S and who earns more than $40,000.
SELECT
    *
FROM
    teachers
WHERE
    first_name ILIKE 's%'
    AND salary > 40000;
ORDER BY
    salary DESC;

-- 3. Rank teachers hired since January 1, 2010, ordered by highest paid to lowest.
SELECT
    *
FROM
    teachers
WHERE
    hire_date >= '2010-01-01'
ORDER BY
    salary DESC;