DROP SCHEMA IF EXISTS day01 CASCADE;
CREATE SCHEMA day01;

CREATE TABLE day01.depths (
       id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       depth integer NOT NULL
);
\COPY day01.depths (depth) FROM 'day01/input1.txt';


SELECT COUNT(d1.id)
FROM day01.depths d1
INNER JOIN day01.depths d2
      ON (d1.id = d2.id-1)
WHERE d2.depth-d1.depth > 0;
      
