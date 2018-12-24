FROM alpine:3.8

COPY . /address-book/

WORKDIR /address-book/

RUN apk update \
    && apk add py-pip \
    && apk add ca-certificates

RUN pip install -r requirements.txt

#ENV {KEY} {VALUE}

ENV MYSQL_DB contacs

ENV MYSQL_USER myuser

ENV MYSQL_PASSWORD myuserpassword

ENV MYSQL_HOST 10.0.245.201

ENV MYSQL_PORT 3306

EXPOSE 8080

ENTRYPOINT ["python3 manage.py runserver 0.0.0.0:8000"]
