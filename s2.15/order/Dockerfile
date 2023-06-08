FROM python:3.10

COPY . /home
RUN pip3 install fastapi
RUN pip3 install sqlalchemy
RUN pip3 install uvicorn
RUN pip3 install psycopg2
RUN pip3 install pika
WORKDIR /home

CMD python3 order/main.py