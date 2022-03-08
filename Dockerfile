# container image that runs your code
FROM debian:bullseye

#Install additional packages
RUN apt-update --quiet \
    && apt-install -y python3 python3-pip

# Copies your code file from your action repository to the file system path '/' of the container
COPY get_wifi_password.py /get_wifi_password.py

# Code file to execute when the docker container startsup
ENTRYPOINT ["/get_wifi_password.py"]
