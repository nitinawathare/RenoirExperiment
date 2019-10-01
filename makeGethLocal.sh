#!/bin/bash

SERVER_LIST=ipList

while read REMOTE_SERVER
do
    #ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup sh /home/ubuntu/gitRepoEVD/downloadEVDCodeGoEthereumSkip2.sh" &  
    ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sh /home/ubuntu/makeGeth.sh" &
    # ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "ps -ax | grep geth" &  

    # echo $REMOTE_SERVER ":" $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "ps -ax | grep geth | wc -l" ) &

    # ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo killall geth" &  
done < $SERVER_LIST

