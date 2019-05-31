FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install default-jdk -y

ADD install-poppler.sh .

RUN chmod +x install-poppler.sh

RUN ./install-poppler.sh

WORKDIR /Lino-WebCrawler

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /Lino-WebCrawler/crawler

EXPOSE 5010

CMD ["python", "server.py"]
