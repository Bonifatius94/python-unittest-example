FROM python:3.8-alpine as test

ADD ./requirements.txt /requirements.txt
RUN python -m pip install pip --upgrade
RUN python -m pip install pytest pylint
RUN python -m pip install -r /requirements.txt

ADD ./src /app/src
WORKDIR /app/src
RUN python -m pytest tests
RUN python -m pylint my_module

FROM python:3.8-alpine as runtime

RUN adduser -D worker
USER worker
ENV PATH=$PATH:/home/worker/.local/bin

ADD ./requirements.txt /requirements.txt
RUN python -m pip install pip --upgrade --user
RUN python -m pip install -r /requirements.txt --user

ADD ./src /app/src
WORKDIR /app/src
ENTRYPOINT ["python", "-m", "my_module"]
