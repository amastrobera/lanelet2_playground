#!/bin/bash

source /home/developer/pyenv/bin/activate
pip2 install ipykernel jupyter
pip2 install rosdep # required to build lanelet2
python2 -m ipykernel install --user --name python2 --display-name "Python 2"
deactivate
