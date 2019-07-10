--- Inner Join: Matches your values specified by "ON" clause
SELECT *
FROM orders
JOIN subscriptions
	ON orders.subscription_id = subscriptions.subscription_id
WHERE subscriptions.description = 'Fashion Magazine';
---

## What if we want to combine two tables and keep some of the un-matched rows? 
## LEFT JOIN
 left join will keep all rows from the first table

SELECT *
FROM newspaper
Left JOIN online
	ON newspaper.id = online.id;
  
--   Where the info in table1 doesn't have a match!
SELECT *
FROM newspaper
Left JOIN online
	ON newspaper.id = online.id
WHERE online.id IS NULL;

---
## Primary keys
None of the values can be NULL.
Each value must be unique (i.e., you can’t have two customers with the same customer_id in the customers table).
A table can not have more than one primary key column.
When the primary key for one table appears in a different table, it is called a foreign key.
Most common types of joins will be joining a foreign key from one table with the primary key from another table.

SELECT *
FROM classes
JOIN students
	ON classes.id = students.class_id;

Primary key is a column that serves a unique identifier for the rows in the table.
Foreign key is a column that contains the primary key to another table.

---
## Cross JOIN
A more common usage of CROSS JOIN is when we need to compare each row of a table to a list of values.
(PERMUTATES!)

SELECT month, COUNT(*) AS 'subscribers'
FROM newspaper
CROSS JOIN months
WHERE start_month <= month AND end_month >= month

GROUP BY month;

---
## UNION: UNION stacks one dataset on top of another.
SQL has strict rules for appending data:
+ Tables must have the same number of columns.
+ The columns must have the same data types in the same order as the first table.

SELECT *
FROM newspaper
UNION
SELECT *
FROM online;

---
## WITH: WITH allows us to define one or more temporary tables that can be used in the final query.
We can then go on to do whatever we want with this temporary table (such as join the temporary table with another table)
Essentially, we are putting a whole first query inside the parentheses () and giving it a name. After that, we can use this name as if it’s a table and write a new query *using* the first query.

WITH previous_query AS (
SELECT customer_id,
   COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers
	ON customers.customer_id = previous_query.customer_id;

---
SELECT *
FROM trips
LEFT JOIN riders
	ON trips.rider_id = riders.id;
  
SELECT *
FROM trips
JOIN cars
	ON trips.car_id = cars.id;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT ROUND(AVG(cost), 2) FROM trips;

SELECT *
FROM riders
WHERE total_trips < 500
UNION 
SELECT *
FROM riders2
WHERE total_trips < 500;

SELECT COUNT(*)
FROM cars
WHERE status = 'active';

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;

