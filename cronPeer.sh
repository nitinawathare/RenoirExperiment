#!/bin/bash

while true; do
  # Do something

	sh fetchpeers.sh > "testData/peerStats/$(date '+%s')" 
 	sleep 10;
done