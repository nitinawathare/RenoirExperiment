#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	echo $REMOTE_SERVER " : " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo geth --exec 'admin.peers.forEach(function(value){console.log(value.enode+\"\t\"+value.name+\"\n\")})' attach ipc:/ssd/.ethereum/geth.ipc") &

done < $SERVER_LIST	
