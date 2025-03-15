FROM alpine:3.21

WORKDIR /app
VOLUME /app/data

CMD ["uwsgi", "--ini", "uwsgi.ini"]

ENV PYTHONPATH=/app

RUN apk update && apk add \
        python3 \
        uwsgi-python3 \
        py3-psutil
        # these are needed for psutil install
        # gcc linux-headers musl-dev python3-dev

COPY uwsgi.ini /app

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy

COPY linux_rest_api/ /app/linux_rest_api
