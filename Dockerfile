FROM ubuntu:20.04
MAINTAINER Osamah Alqaisi osamah.alqaisi@my.utsa.edu

WORKDIR /opencv

RUN apt-get update; \
    apt-get install -y --no-install-recommends python3-opencv; \
    apt-get clean -qq; \
    rm -rf /var/lib/apt/lists/*

CMD ["python3","-c","'import cv2; print(cv2.getBuildInformation())'"]

RUN rm -r /usr/share/doc/libnettle7
