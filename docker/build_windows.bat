#!/usr/bin/env bash

set img=lanelet2-playground

echo "building %img% ..."

docker build -t %img% .


