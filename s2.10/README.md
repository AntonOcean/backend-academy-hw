0. Поднимаем docker-compose up с БДшкам и узнаем подсеть командой 
```buildoutcfg
docker network inspect seminar10_default
```

1. Нужно прокинуть адреса в слейв и мастер через файл pg_hba.conf

```buildoutcfg
host    replication     postgres        172.22.0.2/32           trust
```

2. В мастере сделать настройки для репликации postgresql.conf

```buildoutcfg
wal_level = replica
max_wal_senders = 2
max_replication_slots = 2
hot_standby = on
hot_standby_feedback = on
```

3. Отправляем конфиги в контейнеры с БД
```buildoutcfg
docker cp ./postgres/pg_hba_master.conf seminar10-db-master-1:/var/lib/postgresql/data/pg_hba.conf
docker cp ./postgres/pg_hba_slave.conf seminar10-db-slave-1:/var/lib/postgresql/data/pg_hba.conf
docker cp ./postgres/postgresql_master.conf seminar10-db-master-1:/var/lib/postgresql/data/postgresql.conf
```

```buildoutcfg
SELECT pg_reload_conf();
```

```buildoutcfg
docker restart seminar10-db-slave-1 
docker restart seminar10-db-master-1 
```

4. Запускаем синхронизацию на слейве
```buildoutcfg
docker exec -it seminar10-db-slave-1 bash
```

```buildoutcfg
rm -r /var/lib/postgresql/data
pg_basebackup --host=db-master --username=postgres --pgdata=/var/lib/postgresql/data --wal-method=stream --write-recovery-conf
```

```buildoutcfg
docker restart seminar10-db-slave-1 
```

5. Проверяем в БД что все работает
```buildoutcfg
SELECT pid,usename,application_name,state,sync_state FROM pg_stat_replication;
```