#!/bin/bash

cd gitRepoRenoir

sudo apt update
sudo apt install make -y
sudo apt install gcc -y

sudo rm -r go-renoir

ssh-keyscan -H github.com >> ~/.ssh/known_hosts

ssh-add
ssh-add -l
eval `ssh-agent -s`
git clone git+ssh://git@github.com/sourav1547/go-renoir.git


cd go-renoir

git checkout origin/Renoir_Implementation

make clean
#echo "making code************************************"
make
#echo "END making code************************************"
killall geth
sudo cp build/bin/geth /usr/local/bin
cd ../..
