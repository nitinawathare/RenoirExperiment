#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	# echo $REMOTE_SERVER " : " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo cat /ssd/renoirData/blockInfo |wc -l") &


	# echo $REMOTE_SERVER " : " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo killall geth") &

	echo $REMOTE_SERVER " : " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo ps -ax | grep geth | wc -l" ) &

done < $SERVER_LIST	
