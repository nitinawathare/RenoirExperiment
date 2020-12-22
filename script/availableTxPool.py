
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
transactionKthBlock = {}
# peerTransListDict = defaultdict(list)
peerSimilarityValues = defaultdict(list)
peerSimilarityValuesTime = defaultdict(list)


peerTransaction = defaultdict(list)
#blockSkipCount = 0
def main(path):
	# print(path)
	filename = path+"/blockInfo"  
	# txPath = path+"/abc.txt"
	# txReceivedFp = open(txPath, "r")
	blockCount = 0
	previousBlockNumber = 1
	blockSkipCount = 0
	# print("path*****"+txPath)
	with open(filename) as f:
		for line in f:
			#print(line)
			count = 0
			transactionCount = 0
			peerSimilarityCount ={}
			transactionDict = {}
			transactionKthBlock = {}
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
			# if  not data[2].startswith("2019"):
			# 	continue

			# print("block : "+data[1])
			# print("*************************")

			#if int(data[0]) < 8502514:
				#print("continue ",end='')
				#print(data[0])
			#	continue
			#else:
			#	blockSkipCount = blockSkipCount+1
			#if blockSkipCount>4:
				#print("break",end='')
				#print(data[0])
			#	break
			# print("enter after")
			if int(data[0]) not in range(8669218, 8669318):
				continue
			# print(str(previousBlockNumber)+" : "+data[0])
			# if blockCount == 0:
			# 	previousBlockTime = data[2]
			# 	print("inside131243 : "+data[0])
			# 	continue

			# if previousBlockNumber != int(data[0]):
			# 	print("inside")
			# 	blockCount = blockCount +1
			# 	continue

			if int(data[0])==8669218:
				currentBlockTime = data[2]
				previousBlockNumber = int(data[0])
				# print("inside")
				continue

			if int(previousBlockNumber) != int(data[0]):
				previousBlockNumber = data[0]
				previousBlockTime = currentBlockTime
				# print("inside1313")

				# print("inside")
				# blockCount = blockCount +1
			currentBlockTime = data[2]
			# print(data[0]+" : "+str(previousBlockTime))
			# print("enter after")
			previousBlockNumber = data[0]
			#print(line)
			# utc_time = datetime.strptime(data[2]+" "+data[3][:-3], "%Y-%m-%d %H:%M:%S.%f")
			epoch_time = data[2]#(utc_time - datetime(1970, 1, 1)).total_seconds()
			# while(1):
			# 	last_pos = txReceivedFp.tell()
			# 	tx = txReceivedFp.readline()
			# 	if tx == '':
			# 		break
			# 	#print("tx : "+tx)
			# 	data1 = tx.split(' ')
			# 	#print("tx : "+tx)
			# 	#print("21**********************"+data1[0]+" "+data1[1]+" "+data1[2])
				
			# 	# if len(data1) < 7:
			# 	#   continue
			# 	#print("21**********************"+data1[0]+" "+data1[1]+" "+data1[2])
			# 	if "+" in data1[0] or "+" in data1[1] or "+" in data1[2]:
   #                  #print("2**********************"+data1[0]+" "+data1[1]+" "+data1[2])
			# 		continue
			# 	if "x" in data1[1] or "x" in data1[2]:
			# 		continue
			# 	if data1[0]=="" or data1[1]=="" or data1[2]=="":
			# 		continue
			# 	# if  not data1[1].startswith("2019"):
			# 	# 	continue
			# 	#try:
			# 	if len(data1[2].split('.')[1])>6:
			# 		data1[2] = data1[2][:-3]
			# 	# utc_time1 = datetime.strptime(data1[1]+" "+data1[2], "%Y-%m-%d %H:%M:%S.%f")
			# 	epoch_time1 = data1[1]#(utc_time1 - datetime(1970, 1, 1)).total_seconds()
			# 	#print(data1[6])
			# 	#print(data1[0],end='')
			# 	#print(" ",end='')
			# 	#if tx.split(" ")[1]<= data[2]:
			# 	#print(epoch_time1, end='')
			# 	#print(" ",end='')
			# 	#print(epoch_time)
			# 	if epoch_time1 <= epoch_time:
			# 		#print("received transaction : "+tx.split(" ")[0])
			# 		# if data[3] in peerTransListDict.keys():
			# 			# peerTransListDict[data[3]] = []
			# 		peerTransListDict[data1[2]].append(data1[0])
			# 	else:
			# 		txReceivedFp.seek(last_pos)
			# 		break

			peerTxPath = path+"/transactions/transactionInfo_"+data[3].rstrip().replace("/","_")
			# print(peerTxPath)
			# if data[3] not in peerTransaction.keys():
			if os.path.exists(peerTxPath) == False:
				continue
			txPoolCount = 0
			with open(peerTxPath) as fBlock:
				for tx in fBlock:
					if tx == '':
						break
					data1 = tx.split(' ')
					txPoolCount = txPoolCount + 1
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

			# print("TxPool count : "+str(txPoolCount))
			# print(str(int(data[2])-int(previousBlockTime)))
			# print(data[3])
			# print(transactionList)
			#print(peerTransListDict.keys())
			blockPath = path+"/blocks/"+data[1]
			# print(blockPath)
			minDiff = 999999999
			blockTxCount = 0
			txPresentCount = 0
			kthIndex = 1
			kthBlockCount = (int(data[2])-int(previousBlockTime)) / 3000 

			while kthIndex < kthBlockCount:
				transactionKthBlock[kthIndex] = 0
				kthIndex = kthIndex + 1
			with open(blockPath) as fBlock:
				for tx in fBlock:
					#print("transaction : "+tx)
					transactionCount = transactionCount+1
					# transactionList = peerTransaction[data[3]]
					# for pair in transactionList:


					blockTxCount = blockTxCount + 1
					# for peer in peerTransListDict.keys():
					if tx.rstrip() in transactionList:
						# print(tx.rstrip())
						# print(tx)
						# if tx.rstrip() == tx1:
						count = count + 1
						if data[3] not in peerSimilarityCount.keys():
							peerSimilarityCount[data[3]] = 0	
						peerSimilarityCount[data[3]] = peerSimilarityCount[data[3]]+1

						kthIndex = 1
						while kthIndex < kthBlockCount:
							if int(previousBlockTime)+(kthIndex)*3000 > int(data[2]):
								endTime = int(data[2])
							else:	
								endTime = int(previousBlockTime)+(kthIndex)*3000
							if int(previousBlockTime)+(kthIndex-1)*3000 < int(transactionDict[tx.rstrip()]) < endTime:
								transactionKthBlock[kthIndex] = transactionKthBlock[kthIndex]+1
							kthIndex = kthIndex + 1
							# print("present")

						if int(epoch_time) - int(transactionDict[tx.rstrip()]) < minDiff:
							minDiff = int(epoch_time) - int(transactionDict[tx.rstrip()])
			# print("block tx count : "+str(blockTxCount)+" txPresentCount : "+str(txPresentCount))
			# print("*************************")
			
			for p, smlr in peerSimilarityCount.items():	
				#print(data[0]+" : "+data[1]+" : "+str(smlr)+" : "+str(transactionCount)+": "+p)
				#print(p[:-50],end='')
				#print(" : ",end='')

				if smlr !=0:
					# print(str(smlr/transactionCount*100)+"% skipped")
					peerSimilarityValuesTime[data[0]].append(minDiff)
					if smlr/transactionCount*100 > 61:
						peerSimilarityValues[data[0]].append(smlr/transactionCount*100)
					if smlr/transactionCount*100 > 99 and len(transactionKthBlock.items()) != 0:
						print(str(blockTxCount), end='')
						print(",", end='')
						print(*transactionKthBlock.values(),sep=',')
				else:
					print("0% skipped")
					peerSimilarityValues[data[0]].append(0)
		
			# previousBlockTime = data[2]	
			#print("end**************************")
		for p, smlr in peerSimilarityValues.items():
			# if len(smlr)>15:
			totol = 0
			# print(p, end='')
			# print(",",end='')

			# print(smlr)
			avgSimilarity = np.mean(smlr)
			stdDev = np.std(smlr)
			confidenceInterVal = 1.984*stdDev/math.sqrt(10)

			total = sum(smlr)/len(smlr) 
			# print(avgSimilarity, end='')
			# print(",",end='')
			
			# print(confidenceInterVal,end='')
			# print(",",end='')

			# print(len(smlr),end='')
			# print(",",end='')


			avgTimeDiff = np.mean(peerSimilarityValuesTime[p])
			stdDev = np.std(peerSimilarityValuesTime[p])
			confidenceInterVal = 1.984*stdDev/math.sqrt(10)

			# print(avgTimeDiff,end='')
			# print(",",end='')
			# print(confidenceInterVal)
			converted_list = [str(element) for element in peerSimilarityValuesTime[p]]
			# print(",".join(converted_list))

		# for p, smlr in peerSimilarityValuesTime.items():
			# print(len(smlr))


if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])







# 8669302
# 8669312
# 8669296
# 8669316
# 8669327
# 8669336
# 8669340
# 8669365
# 8669367
# 8669374
# 8669375
# 8669379
# 8669380
# 8669382
# 8669606
# 8669610
# 8669615
# 8669641
# 8669652
# 8669672
# 8669677
# 8669684
# 8669688
# 8669693
# 8668901
# 8668907
# 8668921
# 8668929
# 8668967
# 8668968
# 8668969
# 8668973
# 8668975
# 8668996
# 8668997
# 8668998
# 8669012
# 8669019
# 8669020
# 8669026
# 8669040
# 8669041
# 8669043
# 8669044
# 8669046
# 8669048
# 8669051
# 8669067
# 8669068
# 8669081
# 8669083
# 8669087
# 8669088
# 8669102
# 8669124
# 8669126
# 8669140
# 8669142
# 8669162
# 8669178
# 8669181
# 8669187