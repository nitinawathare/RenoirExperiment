#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime
import os.path
import math
import numpy as np

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



def calcSimilarity():
	# print(path)
	filename = "kthBlockData"  
	file1 = open("../data/lastReCommitIntervalSimilarity.csv","w+")
	file2 = open("../data/SecondLastReCommitIntervalSimilarity.csv","w+")
	file3 = open("../data/thirdLastReCommitIntervalSimilarity.csv","w+")
	file1.write("similarity,probability,cumulative\n")
	file2.write("similarity,probability,cumulative\n")
	file3.write("similarity,probability,cumulative\n")

	probabilityDict1={}
	probabilityDict2={}
	probabilityDict3={}
	with open(filename) as f:
		for line in f:
			data = line.split(',')
			# print(len(data))
			numOfTransactions = int(data[0])
			sml1 = 100*(numOfTransactions - int(data[len(data)-1]))/numOfTransactions
			if len(data)>2:
				sml2 = 100*(numOfTransactions - int(data[len(data)-1]) - int(data[len(data)-2]))/numOfTransactions
			else:
				sml2 = sml1
			if len(data)>3:
				sml3 = 100*(numOfTransactions - int(data[len(data)-1]) - int(data[len(data)-2]) - int(data[len(data)-3]))/numOfTransactions
			else:
				sml3 = sml2
			print(str(sml1)+","+str(sml2)+","+str(sml3))

			if int(round(sml1)) not in probabilityDict1.keys():
				probabilityDict1[int(round(sml1))] = 0
			probabilityDict1[int(round(sml1))] +=1

			if int(round(sml2)) not in probabilityDict2.keys():
				probabilityDict2[int(round(sml2))] = 0
			probabilityDict2[int(round(sml2))] +=1

			if int(round(sml3)) not in probabilityDict3.keys():
				probabilityDict3[int(round(sml3))] = 0
			probabilityDict3[int(round(sml3))] +=1

	printFile(file1, probabilityDict1)
	printFile(file2, probabilityDict2)
	printFile(file3, probabilityDict3)

# 
transactionDict = {}
transactionList = []
peerTransListDict = defaultdict(list)
peerSimilarityValues = defaultdict(list)
peerSimilarityValuesTime = defaultdict(list)
probabilityDict = {}
probabilityCumulativeDict = {}

peerTransaction = defaultdict(list)

def main(path):

	filename = path+"/blockInfo"  
	blockCount = 0
	previousBlockNumber = 1
	blockSkipCount = 0
	previousEpoch = 1
	fileName = 'kthBlockData'
	file = open(fileName, "w+")
	
	with open(filename) as f:
		for line in f:
			#print(line)
			count = 0
			transactionCount = 0
			peerSimilarityCount ={}
			transactionDict = {}
			transactionList = []
			data = line.split(' ')
			if len(data) < 4:
				continue
			if "+" in data[0] or "+" in data[1] or "+" in data[2] or "+" in data[3]:
				#print("1**********************")
				continue
			if "x" in data[0] or "x" in data[2] or "x" in data[3]:
				continue
			if data[0]=="" or data[1]=="" or data[2]=="" or data[3]=="":
				continue

			if int(data[0]) not in range(8669465, 8669476):
				continue
			if blockCount == 0:
				previousEpoch = int(data[2])
				blockCount +=10
				continue

			previousBlockNumber = data[0]

			epoch_time = data[2]#(utc_time - datetime(1970, 1, 1)).total_seconds()

			peerTxPath = path+"/transactions/transactionInfo_"+data[3].rstrip().replace("/","_")


			if os.path.exists(peerTxPath) == False:
				continue
			with open(peerTxPath) as fBlock:
				for tx in fBlock:
					if tx == '':
						break
					data1 = tx.split(' ')
					
					if "+" in data1[0] or "+" in data1[1] or "+" in data1[2]:
						continue
					if "x" in data1[1] or "x" in data1[2]:
						continue
					if data1[0]=="" or data1[1]=="" or data1[2]=="":
						continue
					epoch_time1 = data1[1]
					if epoch_time1 <= epoch_time:
						# print("going in if")
						transactionList.append(data1[0])
						transactionDict[data1[0]] = epoch_time1
					else:
						# txReceivedFp.seek(last_pos)
						break

			blockPath = path+"/blocks/"+data[1]

			minDiff = 999999999
			with open(blockPath) as fBlock:
				for tx in fBlock:

					transactionCount = transactionCount+1

					if tx.rstrip() in transactionList:
						count = count + 1
						if data[3] not in peerSimilarityCount.keys():
							peerSimilarityCount[data[3]] = 0	
						peerSimilarityCount[data[3]] = peerSimilarityCount[data[3]]+1

						if int(epoch_time) - int(transactionDict[tx.rstrip()]) < minDiff:
							minDiff = int(epoch_time) - int(transactionDict[tx.rstrip()])

			transactionCount = 0
			epochTxCountList = []
			epochTxCount = 0
			with open(blockPath) as fBlock:
				epochTxCountList = []
				for tx in fBlock:
					transactionCount = transactionCount+1
					if tx.rstrip() in transactionList:
						if int(previousEpoch)+3 <= int(epoch_time):
							if int(transactionDict[tx.rstrip()]) < int(previousEpoch)+3:
								epochTxCount +=1
							else:
								epochTxCountList.append(epochTxCount)
								epochTxCount = 0
								previousEpoch +=3
								# epochTxCount.append()
				# print(transactionCount, end='')
				# print(" : ", end='')
				# print(epochTxCountList)

				if(len(epochTxCountList)>0):
					file.write(str(transactionCount))
					for element in epochTxCountList:
						file.write(","+str(element))
					file.write("\n")
			previousEpoch = int(data[2])	




if __name__ == "__main__":
    main(sys.argv[1])
    calcSimilarity()