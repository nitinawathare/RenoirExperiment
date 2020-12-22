#!/bin/bash



echo $1

# killall geth

cd gitRepoRenoir 

sudo rm -r .ethereum$1
# sudo rm -r .ethereum1

mkdir .ethereum$1
# mkdir .ethereum1


IPAddress="$(ifconfig eno1| grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')"
echo $IPAddress

nohup geth --datadir .ethereum$1/ 2>> .ethereum$1/setup.log &
sleep 3s
echo "[\"$(cat .ethereum$1/setup.log | grep -oEi '(enode.*@)'| head -1)127.0.0.1:"$((21000+$1))"?discport=0&raftport="$((23000+$1))"\"]" >> .ethereum$1/static-nodes.json

# killall geth

# nohup geth --datadir .ethereum1/ 2>> .ethereum1/setup.log &

# sleep 3s

# echo "[\"$(cat .ethereum$1/setup.log | grep -oEi '(enode.*@)'| head -1)"${IPAddress}":21001?discport=0&raftport=23001\"]" >> .ethereum$1/static-nodes.json


killall geth
sudo rm -r .ethereum$1/geth/chaindata/ #.ethereum/geth/chaindata/
# sudo rm -r .ethereum1/geth/chaindata/

geth --datadir .ethereum$1 --password passwords.txt account new
# geth --datadir .ethereum1 --password passwords.txt account new

cd ..

