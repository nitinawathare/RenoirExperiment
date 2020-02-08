#!/bin/bash

SERVER_LIST=ipList


while read REMOTE_SERVER
do
	#echo $REMOTE_SERVER
	ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "cat /home/ubuntu/gitRepoRenoir/contractAddress" &
	#echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "cat /home/ubuntu/gitRepoRenoir/contractAddress") & 
	#ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/contractAddress" &
	#scp -i quorum2.key downloadEVDCodeGoEthereumSkip2.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &
done < $SERVER_LIST
