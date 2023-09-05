FROM python:3.9.10-slim-buster

RUN apt-get update && apt-get install -y python3-dev gcc libpq-dev

COPY . /birthday_wish
WORKDIR /birthday_wish
RUN mkdir -p logs

RUN pip install -r requirements.txt

COPY server-entrypoint.sh /usr/local/bin/server-entrypoint.sh
COPY worker-entrypoint.sh /usr/local/bin/worker-entrypoint.sh
COPY beat-entrypoint.sh /usr/local/bin/beat-entrypoint.sh

RUN chmod +x /usr/local/bin/server-entrypoint.sh
RUN chmod +x /usr/local/bin/worker-entrypoint.sh
RUN chmod +x /usr/local/bin/beat-entrypoint.sh



