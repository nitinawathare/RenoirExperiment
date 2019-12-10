#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
        ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "nohup sh /home/ubuntu/gitRepoRenoir/installGo.sh" 
done < $SERVER_LIST

