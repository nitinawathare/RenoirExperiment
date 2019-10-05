
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
	
else
	echo "
	'createDataFolder'			to create initial data folders
	'copyData'				to copy data in Data folder
	"
fi


while read REMOTE_SERVER
do
	 #ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo rm -r gitRepoEVD" 
	 #ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "mkdir gitRepoEVD" 
 	#scp -i quorum.pub addressRead.py staticJsonRead.py staticJsonRead1.py passwords.txt installGo.sh downloadEVDCode.sh downloadEVDCode2.sh setupEthereum.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/&

	# mkdir ~/VMQuorumNode/Node$REMOTE_SERVER
	# ssh -o StrictHostKeyChecking=no -l sourav $REMOTE_SERVER&

	if [ "$1" = "genesis" ]; then
		scp -i quorum.pub genesis.json ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/&
		
	elif [ "$1" = "copyData" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo mv renoirData data_$(date +%d-%m-%Y_%H:%M:%S)" &

	elif [ "$1" = "createDataFolder" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo mkdir /ssd/renoirData/; sudo mkdir /ssd/renoirData/blocks; sudo mkdir /ssd/renoirData/transactions" &

	elif [ "$1" = "rmDataFolder" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo rm -r /ssd/renoirData/" &

	elif [ "$1" = "changeOwner" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo chown -R ubuntu /ssd/renoirData/; sudo chmod 777 /ssd/renoirData/;" &

	elif [ "$1" = "copySsh" ]; then
		scp -i quorum.pub /home/nitin14/RenoirExperiment/id_rsa ubuntu@$REMOTE_SERVER:/home/ubuntu/.ssh/ &

	elif [ "$1" = "copyMakeGeth" ]; then
		scp -i quorum.pub /home/nitin14/RenoirExperiment/makeGeth.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	elif [ "$1" = "copyBasrc" ]; then
		scp -i quorum.pub /home/nitin14/RenoirExperiment/.bashrc ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	elif [ "$1" = "go" ]; then
		scp -i quorum.pub /home/nitin14/RenoirExperiment/installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/ &

	fi

	#scp -i quorum.pub installpy3.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/ &
	#scp -i quorum.pub installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/
    #scp -i quorum.pub installGo.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/
	#scp -i quorum.pub downloadEVDCode.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/
	#scp -i quorum.pub setupEthereum.sh ubuntu@$REMOTE_SERVER:/home/ubuntu/gitRepoEVD/
	 
	#ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "geth --datadir /home/ubuntu/gitRepoEVD/.ethereum init /home/ubuntu/gitRepoEVD/genesis.json"

	var=$((var+1))
done < $SERVER_LIST