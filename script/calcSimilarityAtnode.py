
#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime
import os.path
import math
import numpy as np




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
	fileObj = open("../data/gethPeerSimilarity.csv","w+")
	fileObj.write("similarity,probability,cumulative\n")

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

			if int(data[0]) not in range(8669465, 8669567):
				continue

			previousBlockNumber = data[0]
			#print(line)
			# utc_time = datetime.strptime(data[2]+" "+data[3][:-3], "%Y-%m-%d %H:%M:%S.%f")
			epoch_time = data[2]#(utc_time - datetime(1970, 1, 1)).total_seconds()

			for filename in os.listdir(path+"/transactions/"):
				# print(filename)

				peerTxPath = path+"/transactions/"+filename
				# print(peerTxPath)

				if os.path.exists(peerTxPath) == False:
					continue
				with open(peerTxPath) as fBlock:
					for tx in fBlock:
						if tx == '':
							break
						data1 = tx.split(' ')
						
						if len(data1)<3:
							continue
						if "+" in data1[0] or "+" in data1[1] or "+" in data1[2]:
							continue
						if "x" in data1[1] or "x" in data1[2]:
							continue
						if data1[0]=="" or data1[1]=="" or data1[2]=="":
							continue
						epoch_time1 = data1[1]
						if epoch_time1 <= epoch_time:
							# print("going in if")
							# if data1[0] not in transactionList:
							transactionList.append(data1[0])
							transactionDict[data1[0]] = epoch_time1
						else:
							# txReceivedFp.seek(last_pos)
							break


			# print(data[3])
			# print(transactionList)
			#print(peerTransListDict.keys())
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

			
			for p, smlr in peerSimilarityCount.items():	
				#print(data[0]+" : "+data[1]+" : "+str(smlr)+" : "+str(transactionCount)+": "+p)
				#print(p[:-50],end='')
				#print(" : ",end='')
				if smlr !=0:

					peerSimilarityValuesTime[data[0]].append(minDiff)
					if smlr/transactionCount*100 > 55:
						peerSimilarityValues[data[0]].append(smlr/transactionCount*100)
				else:
					print("0% skipped")
					peerSimilarityValues[data[0]].append(0)
			

		for p, smlr in peerSimilarityValues.items():

			totol = 0
			# print(p, end='')
			# print(",",end='')

			# print(smlr)
			avgSimilarity = np.mean(smlr)
			stdDev = np.std(smlr)
			confidenceInterVal = 1.984*stdDev/math.sqrt(10)

			total = sum(smlr)/len(smlr) 
			# print(int(round(avgSimilarity)), end='')
			# print(",",end='')
			
			# print(confidenceInterVal,end='')

			# print("")

			avgTimeDiff = np.mean(peerSimilarityValuesTime[p])
			stdDev = np.std(peerSimilarityValuesTime[p])
			confidenceInterVal = 1.984*stdDev/math.sqrt(10)
			if int(round(avgSimilarity)) not in probabilityDict.keys():
				probabilityDict[int(round(avgSimilarity))] = 0
			probabilityDict[int(round(avgSimilarity))] +=1	
			# print(avgTimeDiff,end='')
			# print(",",end='')
			# print(confidenceInterVal)
			converted_list = [str(element) for element in peerSimilarityValuesTime[p]]
			# print(",".join(converted_list))
		blkCount = 0
		for key, value in probabilityDict.items():
			blkCount+=value
		for key, value in probabilityDict.items():
			probabilityDict[key] = value/blkCount

		cumulativeValue = 0
		for i in sorted (probabilityDict) :
			# fileObj.write(str(i)+" "+str(probabilityDict[i])+" "+str(round(cumulativeValue+probabilityDict[i],3))+"\n")
			print(str(i)+" "+str(probabilityDict[i])+" "+str(round(cumulativeValue+probabilityDict[i],3))+"\n")
			cumulativeValue += probabilityDict[i]
		


if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])