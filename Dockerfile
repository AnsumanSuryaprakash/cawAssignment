FROM python:3.7

ENV Secret_Key='{"k":"lpP4SKGoTvZpDRZaOkRA6cNZD70V_1264iH1jOm7CCY","kty":"oct"}'
WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 9090

ENTRYPOINT ["python3"]
CMD ["/app/app.py"]

