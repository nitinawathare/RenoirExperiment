
#!/bin/bash
SERVER_LIST=ipList

while read REMOTE_SERVER
do
	# ssh -o StrictHostKeyChecking=no -l nitin14 $REMOTE_SERVER&
	echo $REMOTE_SERVER " : " $(ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "geth version" ) &
	
done < $SERVER_LIST

