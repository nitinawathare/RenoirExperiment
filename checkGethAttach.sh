#!/bin/bash
SERVER_LIST=ipList
counter=1
while read REMOTE_SERVER
do
	# echo $REMOTE_SERVER " $1: " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "geth --exec '$1' attach ipc:/home/ubuntu/gitRepoRenoir/.ethereum/geth.ipc") &
	geth --exec $1 attach ipc:$HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth.ipc
	counter=$((counter+1))
done < $SERVER_LIST