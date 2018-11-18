#!/usr/bin/env bash

#################
# Let's install some Nautilus prereqs.
# Are you ready?
################

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev
###
# OpenCV4 is pretty cool. Let's install it.
###
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0-alpha.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0-alpha.zip

unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-4.0.0-alpha opencv
mv opencv_contrib-4.0.0-alpha opencv_contrib

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

source ~/.bashrc

mkvirtualenv cv -p python3
workon cv

pip install numpy

cd ~/opencv
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
            -D INSTALL_PYTHON_EXAMPLES=ON \
                -D INSTALL_C_EXAMPLES=OFF \
                    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
                        -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
                            -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig
workon cv
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.cpython-35m-x86_64-linux-gnu.so cv2.so
cd ~

#########
# Clone the Git Repo
#########
sudo apt-get install git #I'm pretty sure git is installed by default, but better to be on the safe side
git clone https://isaacaddis@bitbucket.org/isaacaddis/rov2019.git
