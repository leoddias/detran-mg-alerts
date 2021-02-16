FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
RUN chmod +x entry.sh

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN apk del tzdata

RUN echo '*  13  *  *  *    python /usr/src/app/main.py placa renavam' >> /etc/crontabs/root

CMD ["sh", "-c", "/usr/src/app/entry.sh"]