FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y --no-install-recommends apt-utils \
  && apt-get install -y python3-pip python3-dev python3.8 python3.8-dev\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

ENV PROJECT_DIR=/django-api-seed
RUN mkdir $PROJECT_DIR
RUN chmod 0777 $PROJECT_DIR
WORKDIR $PROJECT_DIR

COPY . $PROJECT_DIR
RUN rm -rf $PROJECT_DIR/deploy

RUN python -m pip install -r $PROJECT_DIR/requirements/base.txt

COPY deploy/ci/entrypoint.sh $PROJECT_DIR
RUN chmod g+x $PROJECT_DIR/entrypoint.sh

ENTRYPOINT sh $PROJECT_DIR/entrypoint.sh