#!/bin/bash
SERVER_LIST=ipList
counter=1
while read REMOTE_SERVER

do
    #ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup sh /home/ubuntu/gitRepoEVD/startScript.sh"&
	#echo "inside **********2"
	# ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "python3 /home/ubuntu/gitRepoRenoir/addressRead.py"
	python3 $HOME/RenoirExperiment10Nodes/addressRead.py $counter $HOME
	counter=$((counter+1))
	#echo "inside **********1"
done < $SERVER_LIST


