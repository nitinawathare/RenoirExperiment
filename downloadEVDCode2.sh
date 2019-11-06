#!/bin/bash

cd gitRepoRenoir
cd go-renoir
git checkout Renoir_Implementation
git pull origin Renoir_Implementation

make clean
#echo "making code************************************"
make
#echo "END making code************************************"
killall geth
sudo cp build/bin/geth /usr/local/bin
cd ../..
