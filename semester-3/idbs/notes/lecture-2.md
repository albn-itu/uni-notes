

# Lecture 2

## SELECT

- ```sql
  SELECT # desired attributes
  FROM # one or more tables
  WHERE # a condition is met
  ```

- ```sql
  SELECT coffeehouse
  FROM Sells
  WHERE coffee LIKE 'Blue%' AND price > 100
  ```

- ```sql
  SELECT Drinkers.name, Cofeehouses.address
  FROM Frequents F
  	join Cofeehouses H on F.cofeehouse = H.name
  ```

- ```sql
  SELECT Drinkers.address, Cofeehouses.address
  FROM Frequents F
  	join Cofeehouses H on F.cofeehouse = H.name
  	join Drinkers D on F.drinker = D.name
  ```

- ```sql
  SELECT coffeehouse, max(price) as pr
  FROM Sells
  GROUP BY cofeehouse
  WHERE price = pr
  ```

- ```sql
  SELECT coffeehouse, count(*) as c, avg(price)
  FROM Sells
  GROUP BY coffeehouse
  HAVING c > 2
  ```

- 



## Joins



## Aggregation

