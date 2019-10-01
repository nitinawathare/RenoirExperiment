#!/bin/bash

cd /home/ubuntu/go-renoir
git checkout dataCollection
git pull origin dataCollection

make clean
#echo "making code************************************"
make
#echo "END making code************************************"
sudo killall geth
sudo cp build/bin/geth /usr/local/bin
cd ../..
