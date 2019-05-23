#!/bin/bash

echo "Building catkin repo(s)"

mkdir -p $(pwd)/build
mkdir -p $(pwd)/devel
mkdir -p $(pwd)/logs


source /opt/ros/kinetic/setup.bash

catkin init \
&& catkin build \
&& source devel/setup.bash

