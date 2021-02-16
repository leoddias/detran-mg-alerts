FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN apk del tzdata

RUN echo '0  13  *  *  *    python /usr/src/app/main.py placa renavam' >> /etc/crontabs/root

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

CMD ["sh", "-c", "/docker-entrypoint.sh"]