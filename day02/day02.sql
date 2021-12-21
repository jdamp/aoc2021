DROP TABLE IF EXISTS instructions;

CREATE TABLE instructions (
       id integer PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
       direction  varchar(8),
       amount integer NOT NULL
);

\copy instructions (direction, amount) FROM 'day02/input1.txt' USING DELIMITERS ' ';

-- Translate the instructions as follows:
-- forward -> x=x+dx, y=y
-- up      -> x=x,    y=y-dy
-- down    -> x=x,    y=y+dy

\echo 'Part 1 results:';
WITH velocities_x AS (
     SELECT amount, direction,
          CASE WHEN direction = 'forward' THEN amount
	       ELSE 0 END
	  AS vx
     FROM instructions
),
velocities AS (
     SELECT amount, direction, vx,
          CASE WHEN direction = 'down' THEN amount
	       WHEN direction = 'up' THEN -1*amount
               ELSE 0 END
	  AS vy
     FROM velocities_x
)
SELECT SUM(vx)*SUM(vy) from velocities;


-- Part 02
WITH instructions_with_aim AS (
     SELECT id, amount, direction,
     	    SUM(
	         CASE WHEN direction = 'down' THEN amount
	    	 WHEN direction = 'up'   THEN -1*amount
		 ELSE 0 END
	    	 ) OVER (order by id)
	    AS aim
     FROM instructions
),
positions_with_aim AS (
     SELECT id, amount, direction, aim,
     	    SUM(
	         CASE WHEN direction = 'forward' THEN amount
		 ELSE 0 END
	    	 ) OVER (order by id)
	    AS horizontal_position,

	    SUM(
	         CASE WHEN direction = 'forward' THEN aim*amount
		 ELSE 0 END
	    	 ) OVER (order by id)
	    AS depth
     FROM instructions_with_aim
)
SELECT horizontal_position * depth FROM positions_with_aim ORDER BY ID DESC LIMIT 1;
