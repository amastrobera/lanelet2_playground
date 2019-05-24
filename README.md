### Working with Lanelet2

This repo contains an an environment to develop with Lanelet2 and all its ancillary tools. 


#### Instal and use

Install Docker for [Windows](https://docs.docker.com/docker-for-windows/install/) or [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/). Then, follow the instructions below. 

Download the repo as:

```
git clone --recursive https://github.com/amastrobera/lanelet2_playground.git
cd lanelet2_playground
git submodule foreach "git checkout master"
```

Install JOSM with the instructions on their [site](https://wiki.openstreetmap.org/wiki/JOSM). You will use it to open or create files to work in the dev env. 

Run the image and go in the dev env.

```
cd ../docker
./build.sh                  # create the dev env
./run.sh                    # enter the dev env
source setup_lanenet2.sh    # build lanelet2 and save python libraries
```

If you see no errors and you can execute `python -c "from lanelet2.core import LaneletMap"` then all went well :)



#### Python notebook

Once inside the docker image you can use a notebook to test the code bits. Notice that Lanelet2 uses a **Python2**, therefore all libraries must be python2 and the jupyter notebook kernel must be python2. To use it just type these commands.

```
source install_jupyter.sh
source ../pyenv/bin/activate        # enter the python virtual env
                                    # not necessary ... pip2 install -r ../requirements.txt
source setup_lanelet2.sh
jupyter notebook &                  # now, open the url and work on the browser
deactivate                          # exit virtual env once finished
```

