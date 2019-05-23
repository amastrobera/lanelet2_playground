from ubuntu:16.04

# utilities
RUN apt-get update \
    && apt-get install -y \
        wget \
        sudo \
        vim \
        nano \
        gdb \
        valgrind \
        cmake \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# install ROS (kinetic)
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list' \
    && apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 \
    && apt-get update \
    && apt-get install -y ros-kinetic-ros-base \
    && apt-get clean && rm -rf /car/lib/apt/lists/*

# dependencies for lanelet2
RUN apt-get update && apt-get install -y \
            libboost-all-dev \
            libeigen3-dev \
            libgeographic-dev \
            libpugixml-dev \
            libpython-dev \
            libboost-python-dev \
            python-catkin-tools \
            ros-kinetic-catkin \
            ros-kinetic-rosbash \
            ros-kinetic-ros-environment \
        && apt-get clean && sudo rm -rf /var/lib/apt/lists/*

# Python specific
RUN apt-get update && apt-get install -y \
        git \
        python \
        python-pip \
        python3 \
        python3-pip

# create a user
RUN useradd --create-home --groups sudo --shell /bin/bash developer
RUN mkdir -p /etc/sudoers.d \
    && echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer \
        && chmod 0440 /etc/sudoers.d/developer

# environment, dependencies and entry points
USER developer
RUN  mkdir -p /home/developer/workspace \
     && git clone https://github.com/KIT-MRT/mrt_cmake_modules.git \
            /home/developer/workspace/src/mrt_cmake_modules

# Jupyter notebook requirements
RUN sudo pip3 install virtualenv \
    && mkdir -p /home/developer/pyenv \
    && virtualenv -p python3 /home/developer/pyenv \
    && virtualenv -p python2 /home/developer/pyenv

# environment variabes
ADD setup.sh /home/developer/workspace/setup_lanelet2.sh
ENV HOME /home/developer
WORKDIR /home/developer/workspace

