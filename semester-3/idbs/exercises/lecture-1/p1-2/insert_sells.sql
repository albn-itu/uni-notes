SET SCHEMA 'lecture1';

CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;

do $$
begin
    for count in 1..100 loop
        INSERT INTO sells (coffee_id, coffeehouse_id, price) VALUES (
            random_between(1, 5),
            random_between(1, 6),
            random_between(1, 50)
        );
    end loop;
end; $$