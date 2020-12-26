SERVER_LIST1=ipList
counter=1

while read REMOTE_SERVER1
do
	# if [ "$1" = "deploy" ]; then
	python3 $HOME/RenoirExperiment10Nodes/sendTransaction.py $HOME/RenoirExperiment10Nodes/gitRepoRenoir/.ethereum$counter&
	counter=$((counter+1))

done < $SERVER_LIST1