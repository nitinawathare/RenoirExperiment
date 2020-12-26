#!/bin/bash

SERVER_LIST=ipList
counter=1
folder=$(date +%d-%m-%Y-%H-%M-%S)

mkdir $HOME/RenoirExperiment10Nodes/$folder
mkdir $HOME/RenoirExperiment10Nodes/$folder/Mi
mkdir $HOME/RenoirExperiment10Nodes/$folder/Mc
mkdir $HOME/RenoirExperiment10Nodes/$folder/Log
mkdir $HOME/RenoirExperiment10Nodes/$folder/Ex
mkdir $HOME/RenoirExperiment10Nodes/$folder/Ti

while read REMOTE_SERVER
do


# mkdir $HOME/RenoirExperiment10Nodes/$folder/Ql
# mkdir $HOME/RenoirExperiment10Nodes/$folder/PPt


cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/miningInfo $HOME/RenoirExperiment10Nodes/$folder/Mi/$counter.dat & 
cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/minersInChain $HOME/RenoirExperiment10Nodes/$folder/Mc/$counter.dat & 
cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/log$counter.txt $HOME/RenoirExperiment10Nodes/$folder/Log/$counter.txt & 
cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/executionTime $HOME/RenoirExperiment10Nodes/$folder/Ex/$counter.txt & 
cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/experimentTimeStats $HOME/RenoirExperiment10Nodes/$folder/Ti/$counter.txt & 
# cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/queuLengthStats $HOME/RenoirExperiment10Nodes/$folder/Ql/$counter.dat & 
# cp $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/processPreviousTime $HOME/RenoirExperiment10Nodes/$folder/PPt/$counter.dat &
counter=$((counter+1))

done < $SERVER_LIST