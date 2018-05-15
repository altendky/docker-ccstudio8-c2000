ARG FROM=altendky/ccstudio$MAJOR_VERSION
FROM $FROM

ARG COMPILER_VERSION=6.4

RUN apt-get install -y python3

COPY docker.py .
RUN python3 docker.py

# workspace folder for CCS
RUN mkdir -p /workspace

WORKDIR /wd
