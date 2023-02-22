FROM python:3.10

WORKDIR /app

COPY ./main.py ./kek.py
COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "kek:app", "--host", "0.0.0.0"]
