#!/bin/bash
SERVER_LIST=ipList

if [ "$1" = "install" ]; then
	echo "Received $1 Command"

elif [ "$1" = "run" ]; then
	echo "Received $1 Command"
else
	echo "
	'install'		to install packages related to ntps sync
	'run'			run ntp sync
	"
fi

while read REMOTE_SERVER
do
	if [ "$1" = "install" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "nohup sudo apt install ntp -y; nohup sudo service ntp start; nohup timedatectl set-ntp true" &
	elif [ "$1" = "run" ]; then
		ssh -n -i quorum.pub ubuntu@$REMOTE_SERVER "sudo service ntp stop; sudo ntpd -gq; sudo service ntp start" &
	fi
	#echo $REMOTE_SERVER " : " $(ssh -n -i quorum2.key ubuntu@$REMOTE_SERVER "timedatectl | grep 'NTP synchronized: no'") &
done < $SERVER_LIST
