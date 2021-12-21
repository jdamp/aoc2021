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

-- A three-measurement sliding window as defined as:
-- w(i) = d(i) + d(i+1) + d(i+2), where d(i) is the depth in column i.
-- Therefore, the difference of neighbouring windows can be simply expressed
-- as w(i+1)-w(i) = [d(i+1) + d(i+2) + d(i+3)] - [d(i) + d(i+1) + d(i+2)] = d(i+3) - d(i)

WITH lagDepths AS(
    SELECT depth as di3, LAG(depth, 3) OVER (ORDER BY id ASC) as di
    FROM day01.depths
)
SELECT COUNT(*) FROM lagDepths WHERE di3-di > 0;
