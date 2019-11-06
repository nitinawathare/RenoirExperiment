#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	echo $REMOTE_SERVER " $1: " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "geth --exec '$1' attach ipc:/home/ubuntu/gitRepoRenoir/.ethereum/geth.ipc") &

done < $SERVER_LIST