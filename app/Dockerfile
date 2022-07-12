FROM python:3.10
COPY ./ /app

RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE 8080

CMD python serve.py