# Dockerfile

# Author       : Spyder
# Github       : https://github.com/portable36/
# Email        : portable36@gmail.com
# Date         : 01-10-2022
# Main Language: Python

# Download and import main images

# Operating system
FROM debian:latest
# Main package
FROM python:3

# Author info
LABEL MAINTAINER="https://github.com/portable36/SpyPhisher"

# Working directory
WORKDIR SpyPhisher/
# Add files 
ADD . /SpyPhisher

# Installing other packages
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install php openssh-client -y
RUN pip3 install requests bs4
RUN apt-get clean

# Main command
CMD ["python3", "spyphisher.py", "--noupdate"]

## Wanna run it own? Try following commnads:

## "sudo docker build . -t portable36/SpyPhisher:latest", "sudo docker run --rm -it portable36/SpyPhisher:latest"

## "sudo docker pull portable36/SpyPhisher", "sudo docker run --rm -it portable36/SpyPhisher"
