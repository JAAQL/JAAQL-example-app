FROM jaaql/jaaql-middleware-python:latest

ENV INSTALL_PATH /my-project
COPY . $INSTALL_PATH

RUN ./pypy3.7-v7.3.5-linux64/bin/pypy -mpip install -r $INSTALL_PATH/requirements.txt
