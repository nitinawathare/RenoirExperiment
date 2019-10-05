#!/bin/bash

SERVER_LIST=ipList

while read REMOTE_SERVER
do

    ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo rm -r /ssd/.ethereum/* ; nohup sudo geth --datadir /ssd/.ethereum/ --cache 10240 --syncmode full --gcmode archive --rpc --rpcaddr 0.0.0.0 --verbosity 4 --maxpeers 700 --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3 > /ssd/renoirData/log.txt 2>&1" &

done < $SERVER_LIST

