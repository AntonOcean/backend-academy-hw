.PHONY: show-nodes
show-nodes:
	PGPASSWORD=adminpassword psql -U postgres -h localhost -p 5432 -d postgres -c "show pool_nodes;"

.PHONY: show-repl
show-repl:
	PGPASSWORD=adminpassword psql -U postgres -h localhost -p 5432 -d postgres -c "SELECT pid,usename,application_name,state,sync_state FROM pg_stat_replication;"