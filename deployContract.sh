SERVER_LIST1=ipList
counter=1

while read REMOTE_SERVER1
do
	# if [ "$1" = "deploy" ]; then
	python3 $HOME/RenoirExperiment10Nodes/deployContract.py $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter&
	counter=$((counter+1))

	# python3 $HOME/RenoirExperiment10Nodes/deployContract.py $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum1&
	# counter=$((counter+1))

	# elif [ "$1" = "send" ]; then
	# 	nohup ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup python3 /home/ubuntu/gitRepoRenoir/sendTransaction.py"&
	
	# elif [ "$1" = "deployevd" ]; then
	# 	ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup python3 /home/ubuntu/gitRepoRenoir/deployEVDContract.py"&

	# elif [ "$1" = "sendevd" ]; then
	# 	nohup ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "nohup python3 /home/ubuntu/gitRepoRenoir/sendEVDTransaction.py"&
	
	# elif [ "$1" = "stop" ]; then
	# 	ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "python3 /home/ubuntu/gitRepoRenoir/stopExperiment.py"&
	# else
	# 	echo "
	# 		'deploy'		To run deployContract.py
	# 		'send'			To run sendTransaction.py
	# 		'deployevd'		To run deployEVDContract.py
	# 		'sendevd'		To run sendEVDTransaction.py
	# 	"
	# 	break
	# fi
done < $SERVER_LIST1