FROM python:3-onbuild
MAINTAINER funkydorian

RUN mkdir /etugra
VOLUME /etugra
WORKDIR /etugra

CMD python -m pip install zeep
ENV  PYTHONPATH .:/usr/local/lib/python3.5

CMD ["python","./etugra.py","secinitd.log"]