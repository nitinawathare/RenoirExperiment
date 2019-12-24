#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
        # ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup sh /home/ubuntu/gitRepoRenoir/installGo.sh" &
        # ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "export PATH=$PATH:/usr/local/go/bin"
        echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "geth version") &
done < $SERVER_LIST

