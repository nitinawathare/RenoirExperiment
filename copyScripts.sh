
#!/bin/bash
SERVER_LIST=ipList

#for new VM 


folder=$(date +%d-%m-%Y-%H-%M-%S)		
folderEr=EC$(date +%d-%m-%Y-%H-%M-%S)
var=0

if [ "$1" = "genesis" ]; then
	echo "Received $1 Command"

elif [ "$1" = "createDataFolder" ]; then
	echo "Received $1 Command"

elif [ "$1" = "copyData" ]; then
	echo "Received $1 Command"

elif [ "$1" = "rmDataFolder" ]; then
	echo "Received $1 Command"

elif [ "$1" = "changeOwner" ]; then
	echo "Received $1 Command"

elif [ "$1" = "copySsh" ]; then
	echo "Received $1 Command"

elif [ "$1" = "copyMakeGeth" ]; then
	echo "Received $1 Command"

elif [ "$1" = "copyBasrc" ]; then
	echo "Received $1 Command"

elif [ "$1" = "contAdd" ]; then
	echo "Received $1 Command"

elif [ "$1" = "contGen" ]; then
	echo "Received $1 Command"

elif [ "$1" = "contMem" ]; then
	echo "Received $1 Command"

elif [ "$1" = "pyScripts" ]; then
	echo "Received $1 Command"

elif [ "$1" = 'reset' ]; then
	echo "Received $1 Command"

elif [ "$1" = "copyData" ]; then
	mkdir /home/nitin14/EVDExperimentSetup/$folder
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Mi
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Mc
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Log
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Ex
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Ti
	mkdir /home/nitin14/EVDExperimentSetup/$folder/Ql
	mkdir /home/nitin14/EVDExperimentSetup/$folder/PPt

elif [ "$1" = "copyErr" ]; then
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Mi
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Mc
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Log
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Ex
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Ti
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/Ql
	mkdir /home/nitin14/EVDExperimentSetup/$folderEr/PPt

else
	echo "
	'createDataFolder'			to create initial data folders
	'copyErr'		to copy data in Error Folder
	'copyData'		to copy data in Data folder
	'reset'			to reset Remote 
	'genesis' 		to copy genesis
	'contAdd'		to copy contractAddressList
	'contGen'		to copy General contracts
	'contMem'		to copy Memory based contracts
	'pyScripts'		to copy sendTransaction, deployContract etc.
	"
fi


while read REMOTE_SERVER
do
	 #ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo rm -r gitRepoRenoir" 
	 #ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "mkdir gitRepoRenoir" 
 	# scp -i quorum2.key addressRead.py staticJsonRead.py staticJsonRead1.py passwords.txt installGo.sh downloadEVDCode.sh downloadEVDCode2.sh setupEthereum.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/&

	# mkdir ~/VMQuorumNode/Node$REMOTE_SERVER
	# ssh -o StrictHostKeyChecking=no -l nitin14 $REMOTE_SERVER&

	if [ "$1" = "genesis" ]; then
		scp -i quorum2.key genesis.json ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/&
		
	elif [ "$1" = "copyData" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo mv renoirData data_$(date +%d-%m-%Y_%H:%M:%S)" &

	elif [ "$1" = "script" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo rm -r gitRepoRenoir; mkdir gitRepoRenoir" 
	 	# ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo rm -r gitRepoRenoir"
	 	ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "cd gitRepoRenoir; sudo mkdir blocks; mkdir transactions; mkdir transactionsRW" &
 		echo "copy"
 		scp -i quorum2.key addressRead.py staticJsonRead.py staticJsonRead1.py passwords.txt installGo.sh downloadEVDCode.sh downloadEVDCode2.sh setupEthereum.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/&

	elif [ "$1" = "createDataFolder" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo mkdir /ssd/renoirData/; sudo mkdir /ssd/renoirData/blocks; sudo mkdir /ssd/renoirData/transactions" &

	elif [ "$1" = "rmDataFolder" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo rm -r /ssd/renoirData/" &

	elif [ "$1" = "changeOwner" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo chown -R ubuntu /ssd/renoirData/; sudo chmod 777 /ssd/renoirData/;" &

	elif [ "$1" = "copySsh" ]; then
		scp -i quorum2.key /home/nitin14/RenoirExperiment/id_rsa ubuntu@$REMOTE_SERVER:/home/ubuntu/.ssh/ &

	elif [ "$1" = "copyMakeGeth" ]; then
		scp -i quorum2.key /home/nitin14/RenoirExperiment/makeGeth.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	elif [ "$1" = "copyBasrc" ]; then
		scp -i quorum2.key /home/nitin14/RenoirExperiment/.bashrc ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	elif [ "$1" = "go" ]; then
		scp -i quorum2.key /home/nitin14/RenoirExperiment/installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	elif [ "$1" = "downLoadScript" ]; then
		scp -i quorum2.key downloadEVDCodeGoEthereumSkip.sh downloadEVDCodeGoEthereumSkip2.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/&

	elif [ "$1" = "contAdd" ]; then
		scp -i quorum2.key contractAddressList ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/&

	elif [ "$1" = "contGen" ]; then
		scp -i quorum2.key matrixMultiplication.sol cpuheavy.sol emptyLoop.sol ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &

	elif [ "$1" = "contMem" ]; then
		scp -i quorum2.key matrixMemory.sol sortMemory.sol emptyLoop.sol ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &

	elif [ "$1" = "pyScripts" ]; then
		scp -i quorum2.key sendTransaction.py deployContract.py ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &
		scp -i quorum2.key sendEVDTransaction.py deployEVDContract.py ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &
		
	elif [ "$1" = "reset" ]; then
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/queuLengthStats" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/processPreviousTime" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/miningInfo" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/minersInChain" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/log.txt" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/executionTime" &
		ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "> /home/ubuntu/gitRepoRenoir/experimentTimeStats" &

	elif [ "$1" = "copyErr" ]; then
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/miningInfo /home/nitin14/EVDExperimentSetup/$folderEr/Mi/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/minersInChain /home/nitin14/EVDExperimentSetup/$folderEr/Mc/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/log.txt /home/nitin14/EVDExperimentSetup/$folderEr/Log/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/executionTime /home/nitin14/EVDExperimentSetup/$folderEr/Ex/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/experimentTimeStats /home/nitin14/EVDExperimentSetup/$folderEr/Ti/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/queuLengthStats /home/nitin14/EVDExperimentSetup/$folderEr/Ql/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/processPreviousTime /home/nitin14/EVDExperimentSetup/$folderEr/PPt/$var.dat & 

	elif [ "$1" = "copyData" ]; then 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/miningInfo /home/nitin14/EVDExperimentSetup/$folder/Mi/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/minersInChain /home/nitin14/EVDExperimentSetup/$folder/Mc/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/log.txt /home/nitin14/EVDExperimentSetup/$folder/Log/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/executionTime /home/nitin14/EVDExperimentSetup/$folder/Ex/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/experimentTimeStats /home/nitin14/EVDExperimentSetup/$folder/Ti/$var.txt & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/queuLengthStats /home/nitin14/EVDExperimentSetup/$folder/Ql/$var.dat & 
		scp -r -i quorum2.key ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/processPreviousTime /home/nitin14/EVDExperimentSetup/$folder/PPt/$var.dat &

	fi

	#scp -i quorum2.key installpy3.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/ &
	#scp -i quorum2.key installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/
    #scp -i quorum2.key installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/
	#scp -i quorum2.key downloadEVDCode.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/
	#scp -i quorum2.key setupEthereum.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoRenoir/
	 
	#ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "geth --datadir /home/ubuntu/gitRepoRenoir/.ethereum init /home/ubuntu/gitRepoRenoir/genesis.json"

	var=$((var+1))
done < $SERVER_LIST