# container image that runs your code
FROM debian:latest 


LABEL Sohil Patel (sohil43patel@gmail.com)

#Install additional packages
RUN apt update --quiet && apt install -y python3 python3-pip

RUN apt-get install sudo
# Copies your code file from your action repository to the file system path '/' of the container
COPY get_wifi_password.py /get_wifi_password.py

RUN cd /

# Code file to execute when the docker container startsup
ENTRYPOINT ["python3", "/get_wifi_password.py"]
#CMD [ "python", "get_wifi_password.py" ]
