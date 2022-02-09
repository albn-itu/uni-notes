

# Lecture 3

- Division

  - Exam question guaranteed

  - An SQL pattern

  - ```sql
    SELECT coffee
    FROM sells
    GROUP BY coffee
    HAVING count(cofeehouse) = (SELECT COUNT(*) FROM coffeehouses)
    ```

- Joins

  - Natural joins

    - Assumes '=' on all columns of same name
    - Removes duplicate columns
    - Basically don't use.

  - Cross joins

    - Removes no columns
    - Has no join condition
    - Rarely the right thing to do

  - Join syntax

    - ```sql
      -- ANSI syntax, the clearer more readable version
      SELECT *
      FROM likes l
      	JOIN drinkers d
      	ON l.drinker = d.name;
      	
      -- The old inferior syntax
      SELECT *
      FROM likes l, drinkers d
      WHERE l.drinker = d.name
      ```

  - Self join

    - A pattern
    - Produce all combinations of itself

- NULL

  - Represents no, missing or inapplicable values. Basically, undefined,NA,none, etc....

  - ```sql
    SELECT *
    FROM drinkers d
    	LEFT OUTER JOIN likes l ON l.drinker = d.name
    -- Who like now coffee: WHERE coffee IS NULL
    ```

- Set operations

  - Union
    - Unions 2 queries, basically "or"
  - Intersect
    - Get the intersection between 2 queries, basically "and"
  - Except
    - Eliminate rows from one query, that is in a different query, basically "not in"
  - Set operators usually remove duplicates, to keep them use the keyword "ALL"
  - IN and NOT IN

- Subqueries

- Views

  - Code reuse