FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install default-jdk -y

WORKDIR /Lino-WebCrawler

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /Lino-WebCrawler/crawler

EXPOSE 5000

CMD ["python", "server.py"]