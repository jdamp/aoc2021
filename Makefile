.PHONY: psql
psql: # Open psql shell to DB
	psql postgresql://aoc2021:aoc2021@localhost:5432/aoc2021

.PHONY: reset
reset: # Reset the DB (deletes all data and schema)
	podman-compose down
	podman-compose up -d
