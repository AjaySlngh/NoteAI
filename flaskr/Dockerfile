FROM docker.io/python:3.11.4-buster
LABEL maintainer="Ata Noor <>an9965@g.rit.edu>"
LABEL user="Ajay Singh <>aos2500@g.rit.edu"

WORKDIR /flaskr
ADD ./ /flaskr/
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /flaskr/

ENV PYTHONUNBUFFERED True

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--log-level", "info", "--access-logfile", "-", "app:app"]