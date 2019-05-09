## ${Table} AS ${alias}

## SELECT DISTINCT: Queries unique values

## WHERE: Restricts ${variable} ${comparison} ${value}
All below are "WHERE" oerators.
---
## LIKE
+ WHERE name LIKE 'se_en'
+ Underscore is our wildcard
+ % is a wildcard as well, for any number of characters preceding/trailing

## IS NULL
SELECT name
FROM movies
WHERE imdb_rating IS NULL;

## BETWEEN: filter the result set within a certain range. The values can be numbers, text or dates.
+ Exclusive for text, but inclusive for numbers

## AND/OR: Boolean opeartor for WHERE
SELECT *
FROM movies
WHERE year < 1985
  AND genre = 'horror';
---

## ORDER BY
+ Options: ASC, DESC
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;

## LIMIT: Speicifies number of rows query returns
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;

## CASE (& WHEN, ELSE, END)
SELECT name,
 CASE
  WHEN genre = 'romance' OR genre = 'comedy' THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;

SELECT *,
  CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'NewReview'
FROM nomnom;