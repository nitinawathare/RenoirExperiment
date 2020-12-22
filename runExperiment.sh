#!/bin/bash

counter=1
var=0
hashPowerVar=0
cacheVar=$((4096*4))
behavior=0
sh setupEthereumLocal.sh
sh staticJsonRead.sh > static.txt
sh addressRead.sh > address.txt
python3 buildGenesis.py > genesis.json
python3 formStaticJson.py 
killall geth; 
SERVER_LIST=ipList

sudo cp $HOME/go-renoir/build/bin/geth /usr/local/bin

while read REMOTE_SERVER
do
cp staticJsonFiles/static.json$((counter-1)) $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/static-nodes.json &
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/transactions
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/blocks
mkdir $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/transactions
mkdir $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/blocks

sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/chaindata/
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/lightchaindata/
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/nodes/
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/ethash/
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/LOCK/
sudo rm -r $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter/geth/transactions.rlp/

geth --datadir $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter init $HOME/RenoirExperiment10Nodes/genesis.json; geth --datadir $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter --rpc --rpcport $((22000+$counter)) --port $((21000+$counter)) --nodiscover --interarrival 15 --verbosity 4 --maxpeers 50  --gcmode archive --cache $cacheVar --hashpower $hashPowerVar --allow-insecure-unlock --unlock 0 --password $HOME/RenoirExperiment10Nodes/gitRepoRenoir/passwords.txt > $HOME/RenoirExperiment10Nodes/gitRepoRenoir/log$counter.txt 2>&1 &
	
	cacheVar=2048
	behavior=0

counter=$((counter+1))
done < $SERVER_LIST

# ******************************************************************

sleep 4s

# sh deployContract.sh
