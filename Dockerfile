FROM alpine:3.8

COPY . /address-book/

WORKDIR /address-book/

RUN apk update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache && \
    apk add ca-certificates

RUN pip install -r requirements.txt

#ENV {KEY} {VALUE}

ENV MYSQL_DB mydatabase

ENV MYSQL_USER myuser

ENV MYSQL_PASSWORD myuserpassword

ENV MYSQL_HOST 10.0.245.201

ENV MYSQL_PORT 3306

EXPOSE 8080

ENTRYPOINT ["sh","./entrypoint.sh"]
