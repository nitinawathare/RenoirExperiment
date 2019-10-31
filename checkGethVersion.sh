
#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	# ssh -o StrictHostKeyChecking=no -l user $REMOTE_SERVER&
	echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "go version" ) &
	
done < $SERVER_LIST

