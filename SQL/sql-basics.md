## Columns, rows, all within relations

## Select
Fetches/Queries data

## CREATE TABLE

## ALTER TABLE - For adding/updating new columns
---
## INSERT INTO - Adds new row into table

## UPDATE - For updating/editing rows

## DELETE FROM - deleting rows

## Constraints
+ Primary Key
+ Unique
+ Not Null
+ Default

## Example
CREATE TABLE friends (
id INTEGER,
name TEXT,
birthday DATE);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Jane Doe', '1990-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Adam', '1991-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Lek', '1991-45-30');

UPDATE friends
SET name = 'Jane Smith'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE id = 1;
UPDATE friends
SET email = 'adam@codecademy.com'
WHERE id = 2;
UPDATE friends
SET email = 'lek@codecademy.com'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT * FROM friends;