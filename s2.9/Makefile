.PHONY: install
install:
	pip install -r ./backend/requirements.txt

.PHONY: run
run:
	uvicorn app.main:app --reload

# docker cp ./nginx/default.conf seminar9-nginx-1:/etc/nginx/conf.d/default.conf
# docker cp ./key.pem seminar9-nginx-1:/etc/nginx/conf/key.pem
# docker cp ./cert.pem seminar9-nginx-1:/etc/nginx/conf/cert.pem
# docker exec -it seminar9-nginx-1 bash

# https://nginx.org/ru/docs/
# nginx -s reload
# nginx -t

# создаем сертификаты
# openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04