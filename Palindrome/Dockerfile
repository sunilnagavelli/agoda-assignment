FROM ubuntu:18.04

LABEL maintainer="<Sunil Nagavelli>sunilngvli@gmail.com"

RUN \
  apt-get update && \
  apt-get install -y python3

USER ubuntu

COPY IsPalindrome.py /usr/src/app/

WORKDIR /usr/src/app

ENTRYPOINT [ "python3", "./IsPalindrome.py" ]