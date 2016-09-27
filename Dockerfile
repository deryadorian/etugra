FROM python:3-onbuild
MAINTAINER funkydorian

RUN mkdir /etugra

COPY ./etugra.py /tmp

VOLUME /etugra
VOLUME /timestamps
VOLUME /log
WORKDIR /etugra

CMD python -m pip install zeep
ENV  PYTHONPATH .:/usr/local/lib/python3.5

<<<<<<< HEAD
CMD ["python","/tmp/etugra.py","-t"]
=======
CMD ["python","./etugra.py","-t"]
>>>>>>> ea9652640da1cd80b7f452ccb6d52be91033f9b0
