# ARG cuda_version=9.1-devel
# FROM nvidia/cudagl:${cuda_version}
FROM ubuntu:18.04

# https://hub.docker.com/r/nvidia/cudagl/

MAINTAINER Sinan Goo

WORKDIR /bullet3

# Install dependencies
RUN apt update && apt install -y git cmake ffmpeg pkg-config qtbase5-dev libqt5opengl5-dev libassimp-dev libpython3-dev python3-pip

# ipython3

# Install pybullet
RUN git clone https://github.com/bulletphysics/bullet3 /bullet3
RUN python3 setup.py install

# Install C++ API
#RUN mkdir /bullet3/cmake_build && cd /bullet3/cmake_build && cmake .. && make -j8 && make install

RUN apt install -y vim 

RUN pip3 install ipython pika

COPY ./examples /pybullet_examples

