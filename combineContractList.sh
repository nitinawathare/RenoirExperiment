#!/bin/bash

SERVER_LIST1=ipList
counter=1

while read REMOTE_SERVER1
do
	# if [ "$1" = "deploy" ]; then
	cat $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/contractAddress
	counter=$((counter+1))

done < $SERVER_LIST1