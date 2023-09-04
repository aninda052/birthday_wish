FROM python:3.9.10-slim-buster


COPY . /birthday_wish
WORKDIR /birthday_wish

RUN pip install -r requirements.txt

RUN chmod +x /birthday_wish/server-entrypoint.sh

ENTRYPOINT [ "sh", "server-entrypoint.sh" ]



