DROP TABLE IF EXISTS instructions;

CREATE TABLE instructions (
       direction  varchar(8),
       amount integer NOT NULL
);

\copy instructions (direction, amount) FROM 'day02/input1.txt' USING DELIMITERS ' ';

-- Translate the instructions as follows:
-- forward -> x=x+dx, y=y
-- up      -> x=x,    y=y-dy
-- down    -> x=x,    y=y+dy

WITH velocities_x AS (
     SELECT amount, direction,
          CASE WHEN direction = 'forward' THEN amount
	       ELSE 0 END
	  AS vx
     FROM instructions
), velocities AS (
     SELECT amount, direction, vx,
          CASE WHEN direction = 'down' THEN amount
	       WHEN direction = 'up' THEN -1*amount
               ELSE 0 END
	  AS vy
     FROM velocities_x
)
SELECT SUM(vx)*SUM(vy) from velocities;
