FROM python:3.10

COPY . /home
RUN pip3 install sqlalchemy
RUN pip3 install psycopg2
RUN pip3 install pika
WORKDIR /home
RUN apt-get update && apt-get install -y netcat
RUN chmod +x delivery/wait.sh

CMD delivery/wait.sh