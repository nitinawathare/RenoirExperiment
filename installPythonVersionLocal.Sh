#!/bin/bash

SERVER_LIST=ipList

var=0
while read REMOTE_SERVER
do
	scp -i quorum2.key installpy3.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/
	ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sh /home/ubuntu/gitRepoRenoir/installpy3.sh"&

done < $SERVER_LIST
