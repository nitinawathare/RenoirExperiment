
#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	# ssh -o StrictHostKeyChecking=no -l nitin14 $REMOTE_SERVER&

	echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "geth version" ) &

	# echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo pip3 install web3==4.9.0" ) &
	echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "sudo iptables -F" ) &

	
done < $SERVER_LIST

