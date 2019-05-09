For Calculations

## COUNT
SELECT COUNT(*) 
FROM fake_apps
WHERE price = 0;

## SUM
SELECT SUM(downloads)
FROM fake_apps;

## AVG
SELECT AVG(price)
FROM fake_apps;

## MAX/MIN
SELECT MAX(price)
FROM fake_apps;

## ROUND
SELECT ROUND(AVG(price),2)
FROM fake_apps;

---

## GROUP BY
-- SELECT price, COUNT(*) 
-- FROM fake_apps
-- WHERE downloads > 20000
-- GROUP BY price;

SELECT category, SUM(downloads)
FROM fake_apps
GROUP BY category;

SELECT category, 
   price,
   AVG(downloads)
FROM fake_apps
GROUP BY 1, 2, 3; :Equilvalent to: GROUP BY category, price, AVG(downloads)

## HAVING (only works for GROUP BY)
When we want to limit the results of a query based on values of the individual rows, use WHERE.
When we want to limit the results of a query based on an aggregate property, use HAVING.

SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(name) > 10;


---
SELECT * AS 'Total # Companies' FROM startups;
SELECT COUNT(name) FROM startups;
SELECT SUM(valuation) AS 'Total Valuation' FROM startups;
SELECT MAX(raised) AS 'Single Company Most $' FROM startups;

SELECT MAX(raised) AS 'Most Raised in Seed'
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded) AS 'Oldest'
FROM startups;

SELECT AVG(valuation) AS 'AVG Valuation'
FROM startups;

SELECT category, ROUND(AVG(valuation), 2) AS 'AVG Valuation By Group'
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

SELECT category, COUNT(*) AS 'Companies per category'
FROM startups
GROUP BY 1
HAVING COUNT(*) > 2
ORDER BY 2 DESC;

SELECT location, AVG(employees) AS 'Average Size, By Location'
FROM startups
GROUP by 1
HAVING AVG(employees) > 500;