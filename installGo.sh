#!/bin/bash

# mkdir gitRepoEVD
cd gitRepoRenoir
# install golang
GOREL=go1.9.3.linux-amd64.tar.gz
wget -q https://dl.google.com/go/$GOREL
tar xfz $GOREL
sudo rm -r /usr/local/go
sudo mv go /usr/local/go
rm -f $GOREL
export PATH=$PATH:/usr/local/go/bin
echo 'PATH=$PATH:/usr/local/go/bin' >> /home/$USER/.bashrc
echo $PATH
# chmod a+x /home/$USER/.bashrc PS1='$ ' source /home/$USER/.bashrc 
# . /home/ubuntu/.bashrc
cd ..
