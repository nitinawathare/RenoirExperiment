#!/usr/bin/python

import sys
from collections import defaultdict
from datetime import datetime
import os.path
# 
transactionDict = {}
transactionList = []
peerTransListDict = defaultdict(list)
peerSimilarityValues = defaultdict(list)
peerSimilarityValuesTime = defaultdict(list)


peerTransaction = defaultdict(list)
#blockSkipCount = 0
def main(path):
	print(path)
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
			if int(data[0]) not in range(8668894, 8668897):
				continue
			# if previousBlockNumber == data[0]:
			# 	continue

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


			# print(data[3])
			# print(transactionList)
			#print(peerTransListDict.keys())
			blockPath = path+"/blocks/"+data[1]
			# print(blockPath)
			minDiff = 999999999
			with open(blockPath) as fBlock:
				for tx in fBlock:
					#print("transaction : "+tx)
					transactionCount = transactionCount+1
					# transactionList = peerTransaction[data[3]]
					# for pair in transactionList:



					# for peer in peerTransListDict.keys():
					if tx.rstrip() in transactionList:
						# print(tx.rstrip())
						# print(tx)
						# if tx.rstrip() == tx1:
						count = count + 1
						if data[3] not in peerSimilarityCount.keys():
							peerSimilarityCount[data[3]] = 0	
						peerSimilarityCount[data[3]] = peerSimilarityCount[data[3]]+1

						if int(epoch_time) - int(transactionDict[tx.rstrip()]) < minDiff:
							minDiff = int(epoch_time) - int(transactionDict[tx.rstrip()])

			# print("*************************")
			
			for p, smlr in peerSimilarityCount.items():	
				#print(data[0]+" : "+data[1]+" : "+str(smlr)+" : "+str(transactionCount)+": "+p)
				#print(p[:-50],end='')
				#print(" : ",end='')
				if smlr !=0:
					#print(str(smlr/transactionCount*100)+"% skipped")
					peerSimilarityValuesTime[data[0]].append(minDiff)
					if smlr/transactionCount*100 > 50:
						peerSimilarityValues[data[0]].append(smlr/transactionCount*100)
				else:
					print("0% skipped")
					peerSimilarityValues[data[0]].append(0)
			
			#print("end**************************")
		for p, smlr in peerSimilarityValues.items():
			# if len(smlr)>15:
			totol = 0
			print(p, end='')
			print(" : ",end='')

			# print(smlr)
			total = sum(smlr)/len(smlr) 
			print(total, end='')
			print(" : ",end='')
			print(len(smlr))
			print(peerSimilarityValuesTime[p])

		# for p, smlr in peerSimilarityValuesTime.items():
			# print(len(smlr))


if __name__ == "__main__":
    # print(sys.argv[1])
    main(sys.argv[1])
