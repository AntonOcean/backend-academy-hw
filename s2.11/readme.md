## Cassandra
### Модель данных отталкивается от запроса
### Перфоманс на запись
### Отсутствует реляционное моделирование => Денормализация и дублирование
### Выбор ключа партиции - consistent hash

https://medium.com/geekculture/system-design-solutions-when-to-use-cassandra-and-when-not-to-496ba51ef07a

https://hub.docker.com/r/bitnami/cassandra/

Увеличить размер памяти для докера, иначе кластер из 3 нод падает
```buildoutcfg
colima start --cpu 4 --memory 8
```

```buildoutcfg
docker info
```

Поиск конфига внутри контейнера
```buildoutcfg
find . -name cassandra.yaml
```

Забираем конфиг 
```buildoutcfg
docker cp seminar11_dbq-3_1:/opt/bitnami/cassandra/conf/cassandra.yaml .
```

Правим авторизацию
```buildoutcfg
authenticator: 'AllowAllAuthenticator'
```

Прокидываем конфиг
```buildoutcfg
docker cp ./conf/cassandra.yaml seminar11_dbq-1_1:/opt/bitnami/cassandra/conf/cassandra.yaml
docker cp ./conf/cassandra.yaml seminar11_dbq-2_1:/opt/bitnami/cassandra/conf/cassandra.yaml
docker cp ./conf/cassandra.yaml seminar11_dbq-3_1:/opt/bitnami/cassandra/conf/cassandra.yaml
```

Теперь можем убить любой узел и работоспособность будет!

Подлючение в контейнер
```buildoutcfg
docker exec -it seminar11-dbq-3-1 bash
```

Авторизация в утилите для запуска команд в БД
```buildoutcfg
cqlsh -u cassandra -p cassandra
```