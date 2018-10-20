FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install default-jdk -y

WORKDIR /Lino-WebCrawler

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /Lino-WebCrawler

WORKDIR /Lino-WebCrawler/crawler

RUN apt-get update && apt-get install -y mongodb

CMD ["python", "server.py"]
