# Practical SQL 2nd Edition

Practical SQL is for people who encounter data in their everyday lives and want to learn how to analyze, manage, and transform it. This book was written with people new to programming in mind, so the early chapters cover key basics about databases, data, and SQL syntax.

## Introduction

### Structured Query Language (SQL)

SQL is a widely used programming language for managing data and database systems. Because SQL is a mature language that’s been around for decades, it’s ingrained in many modern systems.

1. Using a robust SQL database system allows you to work with terabytes of data, multiple related tables, and thousands of columns.

2. It gives you fine-grained control over the structure of your data, leading to efficiency, speed,
and—most important—accuracy.

3. SQL is also an excellent adjunct to programming languages used in the data sciences, such as R and Python.

4. SQL is useful beyond data analysis.

### PostgreSQL

PostgreSQL, or simply Postgres, is a robust application that can handle large amounts of data.

1. It’s free.

2. It’s available for Windows, macOS, and Linux operating systems.

3. Its SQL implementation aims to closely follow the SQL standard.

4. It’s widely used, so finding help online is easy.

5. It’s available in cloud computing environments such as Amazon Web Services and Google Cloud.

The good news is that the fundamental concepts and much of the core SQL syntactical conventions of PostgreSQL will work across databases.

## Chapter 1: Setting Up Your Coding Environment

### Database Management System (DBMS)

***PostgreSQL*** is a ***Database Management System (DBMS)***, which means it’s software that allows you to define, manage, and query databases.

When you installed PostgreSQL, it created a ***Database Server***—an instance of the application running on your computer—that includes a default database called ***postgres***.

```sql
-- Check installation and the version of PostgreSQL:
SELECT version();
```

### pgAdmin

With pgAdmin, you get a graphical interface where you can configure multiple aspects of your PostgreSQL server and databases, and— most appropriately for this book—use a SQL query tool for writing,
running, and saving queries.

## Chapter 2: Creating Your First Database And Table

SQL is more than just a means for extracting knowledge from data. It’s also a language for defining the structures that hold data so we can
organize relationships in the data.

### Creating a Database

A ***Database*** is a collection of objects that includes tables, functions, and much more, and this is where your actual data will lie. We use the SQL language (as well as pgAdmin) to manage objects and data
stored in the database.

```sql
-- Create a database called analysis:
CREATE DATABASE analysis;
```

### Creating a Table

A ***Table*** is a collection of related data held in a structured format within a database. We use SQL to define the structure of a table and how each table might relate to other tables in the database.

When you create a table, you assign a name to each ***column*** (sometimes referred to as a ***field*** or ***attribute***) and assign each column a data type. These are the values the column will accept—such as text, integers, decimals, and dates—and the definition of the data type is one way SQL enforces the
***integrity of data***.

Data stored in a table can be accessed and analyzed, or queried, with ***SQL statements***.

```sql
-- Create a table called teachers in the analysis database:
CREATE TABLE teachers (
    id bigserial,
    first_name varchar(50),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);
```

### Inserting Rows Into a Table

Text and dates require ***quotes***; numbers, including integers and decimals, don’t
require quotes.

```sql
-- Inserts teacher data into the table.
INSERT INTO
    teachers (
        first_name,
        last_name,
        school,
        hire_date,
        salary
        )
VALUES 
    ('Jane', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
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
```

## Chapter 3: Beginning Data Exploration With **SELECT**

A **SELECT** statement can be simple, retrieving everything in a single table, or it can be complex enough to link dozens of tables while handling multiple
calculations and filtering by exact criteria.

### Basic **SELECT** Syntax

The ***asterisk*** following the **SELECT** keyword is a ***wildcard***, which is like a standing for a value: it doesn’t represent anything in particular and instead represents everything that value could possibly be.

The **FROM** keyword indicates you want the query to return data from a particular table. The semicolon after the table name tells PostgreSQL it’s the ***end of the query*** statement.

```sql
-- Basic SELECT syntax:
SELECT * FROM teachers;

-- Open table in pgAdmin:
TABLE teachers;
```

Often, it’s more practical to limit the columns the query retrieves, especially with large databases, so you don’t have to wade through excess information. You can do this by naming columns, separated by commas, right after the **SELECT** keyword.

```sql
-- Querying a Subset of Columns
SELECT 
    hire_date,
    first_name,
    school
FROM
    teachers;
```

### Sorting Data With **ORDER BY**

In SQL, we order the results of a query using a clause containing the keywords **ORDER BY** followed by the name of the column or columns to ***sort***.

By default, **ORDER BY** sorts values in ***ascending order***, but here I sort in ***descending order*** by adding the **DESC** keyword.

The **ORDER BY** clause also accepts ***numbers*** instead of column names, with the number identifying the sort column according to its position in the
**SELECT** clause.

```sql
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
```

### Using **DISTINCT** To Find Unique Values

To understand the range of values in a column, we can use the **DISTINCT** keyword as part of a query that eliminates duplicates and ***shows only unique values***.

This is a helpful first step toward assessing data quality.

```sql
-- Using DISTINCT to find unique values
SELECT DISTINCT
    salary
FROM
    teachers
ORDER BY
    salary DESC;
```

The **DISTINCT** keyword also works on more than one column at a time. If we add a column, the query returns each ***unique pair of values***.

This technique gives us the ability to ask, ***“For each x in the table, what are all the y values?”***

### Filtering Rows With **WHERE**

The **WHERE** clause allows you to ***find rows*** that match a specific value, a range of values, or multiple values based on criteria supplied via an operator—a keyword that lets us perform math, comparison, and logical
operations.

```sql
-- Filtering rows with WHERE
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    salary BETWEEN 45000 AND 50000;
```

### Filtering Rows With **LIKE** and **ILIKE**

The **LIKE** operator, which is part of the **ANSI SQL standard**, is ***case sensitive***. The **ILIKE** operator, which is a **PostgreSQL-only implementation**, is ***case insensitive***.

- **Percent sign (%)**: A wildcard matching ***one or more*** characters.
- **Underscore (_)**: A wildcard matching ***just one*** character.

```sql
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
```

### Combining Operators with **AND** and **OR**

Comparison operators become even more useful when we ***combine them***. To do this, we connect them using the logical operators **AND** and **OR** along
with, if needed, parentheses.

Because we connect the two conditions using **AND**, ***both must be true*** for a row to meet the criteria in the **WHERE** clause and be returned in the query results.

```sql
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
```

When we connect conditions using **OR**, ***only one of the conditions must be true*** for a row to meet the criteria of the **WHERE** clause.

```sql
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
```

When we place statements inside parentheses, those ***are evaluated as a group*** before being combined with other criteria.

### Putting All Together

