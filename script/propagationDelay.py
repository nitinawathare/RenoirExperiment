#!/usr/bin/python


import sys
from collections import defaultdict
from datetime import datetime
import os.path
import math
import numpy as np


transactionDelay = defaultdict(list)
blockDelay = defaultdict(list)

def printFile(fileObj, probabilityDict):
	blkCount = 0
	for key, value in probabilityDict.items():
		blkCount+=value
	for key, value in probabilityDict.items():
		probabilityDict[key] = value/blkCount

	cumulativeValue = 0
	for i in sorted (probabilityDict) :
		fileObj.write(str(i)+","+str(probabilityDict[i])+","+str(round(cumulativeValue+probabilityDict[i],3))+"\n")
		cumulativeValue += probabilityDict[i]


def txPropagation(txFilePath):
	probabilityDict = {}
	fileObj = open("../data/propTxDelay.csv","w+")
	fileObj.write("delay,probability,cumulative\n")

	for root, dirs, files in os.walk(txFilePath+"/transactions"):
	    path = root.split(os.sep)
	    # print((len(path) - 1) * '---', os.path.basename(root))
	    count =0
	    for file in files:
	    
	        filePath = txFilePath+"/transactions/"+file
	    
	        with open(filePath) as f:
	        	for line in f:
	        		data = line.split(' ')
	        		transactionDelay[data[0]].append(data[1])
	        
	        count = count+1
	        if count>60:		
	        	break;
	    
	    for tx, times in transactionDelay.items():
	    	if len(times)>2:
	    		# print(tx+" : "+str(time))
	    		for time in times:
	    			print((int(time)-int(min(times)))/1000000)
	    			if round((int(time)-int(min(times)))/1000000) !=0:
		    			if int(round((int(time)-int(min(times)))/1000000)) not in probabilityDict.keys():
		    				probabilityDict[int(round((int(time)-int(min(times)))/1000000))] = 0
		    			probabilityDict[int(round((int(time)-int(min(times)))/1000000))] +=1

	printFile(fileObj,probabilityDict)



def blockHashPropagation(blkFilePath):
	filePath1 = blkFilePath+"/blockHashInfo"
	with open(filePath1) as f:
		for line in f:
			data = line.split(' ')

			if len(data)!=4 or "enode" in data[0] or len(data[0])>8 or data[0]=="":
				continue
			blockDelay[data[0]].append(data[2])
			# print(transactionDelay)	


def blockPropagation(blkFilePath):
	blockHashPropagation(blkFilePath)
	filePath = blkFilePath+"/blockInfo"
    
	probabilityDict = {}
	fileObj = open("../data/blockPropDelay.csv","w+")
	fileObj.write("delay,probability,cumulative\n")

	with open(filePath) as f:
		for line in f:
			data = line.split(' ')

			if len(data)!=4 or "enode" in data[0] or len(data[0])>8 or data[0]=="":
				continue
			blockDelay[data[0]].append(data[2])
 
	for blk, times in blockDelay.items():
		if len(times)>2:
			# print(tx+" : "+str(time))
			for time in times:
				print((int(time)-int(min(times))))
				if round((int(time)-int(min(times)))/1000000) !=0:
					if int(round((int(time)-int(min(times)))/1000000)) not in probabilityDict.keys():
						probabilityDict[int(round((int(time)-int(min(times)))/1000000))] = 0
					probabilityDict[int(round((int(time)-int(min(times)))/1000000))] +=1

	printFile(fileObj,probabilityDict)



def main(filePath):
	txPropagation(filePath)
	blockPropagation(filePath)

if __name__ == "__main__":

    main(sys.argv[1])
