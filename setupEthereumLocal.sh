#!/bin/bash

SERVER_LIST=ipList
counter=1
killall geth
while read REMOTE_SERVER
do
	# ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup sh /home/ubuntu/gitRepoRenoir/setupEthereum.sh" &
	
	sh setupEthereum.sh $counter
	counter=$((counter+1))
done < $SERVER_LIST

# sh staticJsonRead.sh > static.txt