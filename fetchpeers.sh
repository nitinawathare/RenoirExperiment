#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	echo $REMOTE_SERVER " $1: " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo geth --exec '$1' attach ipc:/ssd/.ethereum/geth.ipc") &

done < $SERVER_LIST