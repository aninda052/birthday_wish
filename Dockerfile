FROM python:3.9.10-slim-buster

RUN apt-get update && apt-get install -y python3-dev gcc libpq-dev

COPY . /birthday_wish
WORKDIR /birthday_wish

RUN pip install -r requirements.txt

RUN chmod +x /birthday_wish/worker-entrypoint.sh
RUN chmod +x /birthday_wish/beat-entrypoint.sh
RUN chmod +x /birthday_wish/server-entrypoint.sh



