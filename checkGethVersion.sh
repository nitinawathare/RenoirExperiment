
#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	# ssh -o StrictHostKeyChecking=no -l user $REMOTE_SERVER&
	echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "go version" ) &
	
done < $SERVER_LIST


# ~/gitRepoRenoir/readWrite8/0x00001be9f3c329d2418c748345d0ac7560646c985d445f32a2ce1609cffc93ff