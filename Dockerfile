FROM python:3.6


RUN adduser --disabled-password --gecos '' monpytok


WORKDIR /home/monpytok


COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY app app
COPY test test
COPY utils utils
COPY ModelDir ModelDir
COPY main.py boot.sh ./
RUN  chmod +x boot.sh

ENV  FLASK_APP main.py

RUN  chown -R monpytok:monpytok ./
USER monpytok

EXPOSE 5004
ENTRYPOINT ["./boot.sh"]